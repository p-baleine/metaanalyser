import functools
import logging
import tiktoken
from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import SpacyTextSplitter
from langchain.vectorstores import FAISS
from tqdm.auto import tqdm
from typing import List

from .paper import Paper

logger = logging.getLogger(__name__)


def create_papers_vectorstor(
        papers: List[Paper],
        tiktoken_encoder_model_name: str = "gpt-3.5-turbo",
        chunk_size: int = 150,
        chunk_overlap: int = 10,
) -> FAISS:
    splitter = SpacyTextSplitter.from_tiktoken_encoder(
        model_name=tiktoken_encoder_model_name,
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
    )
    enc = tiktoken.encoding_for_model(tiktoken_encoder_model_name)

    def format_text(text):
        return functools.reduce(
            lambda text, special_token: text.replace(special_token, ""),
            list(enc.special_tokens_set),
            text
        ).replace("\n", " ")

    logger.info(
        f"Creating vector store,"
        f" {tiktoken_encoder_model_name=}"
        f", {chunk_size=}, {chunk_overlap=}"
    )

    docs = splitter.create_documents(
        [format_text(p.text) for p in tqdm(papers)],
        metadatas=[
            {
                'google_scholar_result_id': p.google_scholar_result_id,
                'title': p.title,
                'link': p.link,
                'nb_cited': p.nb_cited,
                'citation_id': p.citation_id,
                'entry_id': p.entry_id,
                'published': str(p.published),
                'primary_category': p.primary_category,
                'categories': ", ".join(p.categories),
                'doi': p.doi,
                'citiation': p.mla_citiation.snippet,
            } for p in papers
        ]
    )

    embeddings = OpenAIEmbeddings()
    db = FAISS.from_documents(docs, embeddings)

    logger.info(
        f"Vector store is created from {len(papers)} papers,"
        f" document size={len(docs)}"
    )

    return db
