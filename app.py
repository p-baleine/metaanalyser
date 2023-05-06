import logging
import os
# from typing import Optional, Tuple
import gradio as gr
from langchain.chat_models import ChatOpenAI

from metaanalyser.chains import SRSectionChain, SROverviewChain, SROutlintChain
from metaanalyser.paper import search_on_google_scholar, create_papers_vectorstor


logger = logging.getLogger(__name__)
logging.basicConfig()
logging.getLogger("metaanalyser").setLevel(level=logging.DEBUG)


def run(query: str):
    llm = ChatOpenAI(temperature=0)
    papers = search_on_google_scholar(query)
    db = create_papers_vectorstor(papers)
    overview_chain = SROverviewChain(llm=llm, verbose=True)
    outline_chain = SROutlintChain(llm=llm, verbose=True)
    section_chain = SRSectionChain(
        llm=llm,
        paper_store=db,
        verbose=True
    )

    overview = overview_chain.run({"query": query, "papers": papers})
    outline = outline_chain.run({"query": query, "papers": papers, "overview": overview})

    sections_as_md = []

    for section_idx in range(len(outline.sections)):
        # TODO: 入れ子のセクションに対応する
        sections_as_md.append(section_chain.run({
            "section_idx": section_idx,
            "section_level": 2,
            "query": query,
            "papers": papers,
            "overview": overview,
            "outline": outline
        }))

    sr = f"# {overview.title}\n\n{overview.overview}\n\n## Table of contents\n\n{outline}\n\n"
    sr += "\n\n".join(sections_as_md)
    sr += "\n\n## References\n"

    papers_citation_id_map = {p.citation_id: p for p in papers}
    citations = []

    for citation_id in outline.citations_ids:
        citation = papers_citation_id_map[int(citation_id)]
        citations.append(f"[^{citation_id}]: [{citation.mla_citiation.snippet}]({citation.link})")

    sr += "\n\n".join(citations)

    return sr


def set_openai_api_key(api_key: str):
    os.environ["OPENAI_API_KEY"] = api_key


def set_serpapi_api_key(api_key: str):
    os.environ["SERPAPI_API_KEY"] = api_key


# block = gr.Blocks(css=".gradio-container {background-color: lightgray}")
block = gr.Blocks()

with block:
    with gr.Row():
        gr.Markdown("""
        <h2><center>metaanalyser demo</center></h2>
        Generate a systematic review for your query based on Google Scholar search results. It will take a few minutes to output the results.
        """)

        openai_api_key_textbox = gr.Textbox(
            placeholder="Paste your OpenAI API key (sk-...)",
            show_label=False,
            lines=1,
            type="password",
        )
        serpai_api_key_textbox = gr.Textbox(
            placeholder="Paste your SerpApi API key",
            show_label=False,
            lines=1,
            type="password",
        )

    with gr.Row():
        query = gr.Textbox(
            label="Query",
            placeholder="the query for Google Scholar",
            lines=1,
        )
        submit = gr.Button(value="Send", variant="secondary").style(full_width=False)

    gr.Examples(
        examples=[
            "llm agent OR llm tool integration",
        ],
        inputs=query,
    )

    with gr.Row():
        output = gr.Markdown("It will take a few minutes to output the results...")

    gr.HTML(
        "<center>Powered by <a href='https://github.com/hwchase17/langchain'>LangChain 🦜️🔗</a></center>"
    )

    submit.click(fn=run, inputs=query, outputs=output)
    openai_api_key_textbox.change(
        set_openai_api_key,
        inputs=[openai_api_key_textbox],
    )
    serpai_api_key_textbox.change(
        set_serpapi_api_key,
        inputs=[serpai_api_key_textbox],
    )



block.launch(debug=True)
