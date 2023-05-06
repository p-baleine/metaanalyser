from langchain.base_language import BaseLanguageModel
from langchain.callbacks.manager import CallbackManagerForChainRun
from langchain.prompts.base import BasePromptTemplate
from langchain.vectorstores.base import VectorStore
from typing import Any, Dict, List, Optional

from ...paper import (
    Paper,
    get_abstract_with_token_limit,
    get_categories_string,
)
from ..base import (
    SRBaseChain,
    maybe_retry_with_error_output_parser,
)
from ..outline import Outlint
from ..overview import Overview
from .prompt import SECTION_PROMPT


class SRSectionChain(SRBaseChain):

    paper_store: VectorStore
    prompt: BasePromptTemplate = SECTION_PROMPT
    nb_categories: int = 3
    nb_token_limit: int = 2_000
    nb_max_retry: int = 3

    @property
    def input_keys(self) -> List[str]:
        # TODO: 入れ子に対応する
        return [
            "section_idx",
            "section_level",
            "query",
            "papers",
            "overview",
            "outline"
        ]

    def _call(
        self,
        inputs: Dict[str, Any],
        run_manager: Optional[CallbackManagerForChainRun] = None,
    ) -> Dict[str, str]:
        input_list = get_input_list(
            self.llm,
            self.paper_store,
            inputs["section_idx"],
            inputs["section_level"],
            inputs["query"],
            inputs["papers"],
            inputs["overview"],
            inputs["outline"],
            self.nb_categories,
            self.nb_token_limit,
        )
        return super()._call(input_list, run_manager=run_manager)

    def _acall(
        self,
        inputs: Dict[str, Any],
        run_manager: Optional[CallbackManagerForChainRun] = None,
    ) -> Dict[str, str]:
        input_list = get_input_list(
            self.llm,
            self.paper_store,
            inputs["section_idx"],
            inputs["section_level"],
            inputs["query"],
            inputs["papers"],
            inputs["overview"],
            inputs["outline"],
            self.nb_categories,
            self.nb_token_limit,
        )
        return super()._acall(input_list, run_manager=run_manager)


def get_input_list(
        llm: BaseLanguageModel,
        paper_store: VectorStore,
        section_idx: int,
        section_level: int,
        query: str,
        papers: List[Paper],
        overview: Overview,
        outline: Outlint,
        nb_categories: int,
        nb_token_limit: int,
        max_paper_store_search_size: int = 100,
):
    section = outline.sections[section_idx]
    papers_citation_id_map = {p.citation_id: p for p in papers}
    related_papers = [
        papers_citation_id_map[int(citation_id)]
        for citation_id in section.citation_ids
    ]

    if not related_papers:
        # citation_ids が空なら全部を対象とする
        # FIXME: 全部にしちゃうと溢れちゃうのでは？？
        related_papers = papers

    related_snippets = paper_store.similarity_search(
        f"{section.title} {section.description}",
        k=max_paper_store_search_size,
    )

    # overview が引用している論文の abst は全部 snippet に含める
    # 加えて nb_token_limit に到達するまで vectorstore から関連文章を集める

    def get_snippet(title, citation_id, text):
        text = text.replace("\n", " ")
        return f"""
Title: {title}
citation_id: {citation_id}
Text: {text}
"""

    snippets = [get_snippet(p.title, p.citation_id, p.summary) for p in related_papers]
    total_num_tokens = llm.get_num_tokens("\n".join(snippets).strip())
    idx = 0

    while idx < len(related_snippets):
        snippet = related_snippets[idx]
        snippet_text = get_snippet(
            snippet.metadata["title"],
            snippet.metadata["citation_id"],
            snippet.page_content,
        )
        num_tokens = llm.get_num_tokens(snippet_text)

        if total_num_tokens + num_tokens > nb_token_limit:
            break

        snippets.append(snippet_text)
        total_num_tokens += num_tokens
        idx += 1

    return [{
        "query": query,
        "title": overview.title,
        "overview": overview,
        "section_title": section.title,
        "section_level": section_level,
        "md_title_suffix": "#" * section_level,
        "outline": outline,
        "categories": get_categories_string(papers, nb_categories),
        "snippets": "\n".join(snippets).strip(),
    }]
