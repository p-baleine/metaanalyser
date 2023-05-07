import logging
import os
import gradio as gr
from langchain.chat_models import ChatOpenAI

from metaanalyser.chains import SRChain


logger = logging.getLogger(__name__)
logging.basicConfig()
logging.getLogger("metaanalyser").setLevel(level=logging.DEBUG)


def run(query: str, chain: SRChain):
    if "OPENAI_API_KEY" in os.environ or "SERPAPI_API_KEY" not in os.environ:
        raise gr.Error(f"Please paste your OpenAI (https://platform.openai.com/) key and SerpAPI (https://serpapi.com/) key to use.")

    llm = ChatOpenAI(temperature=0)
    chain = SRChain(llm=llm, verbose=True)
    return chain.run({"query": query})


def set_openai_api_key(api_key: str):
    os.environ["OPENAI_API_KEY"] = api_key


def set_serpapi_api_key(api_key: str):
    os.environ["SERPAPI_API_KEY"] = api_key


block = gr.Blocks()

with block:
    with gr.Row():
        gr.Markdown("""
        <h2><center>Metaanalyser demo</center></h2>
        Generate a systematic review for your query based on Google Scholar search results. See [README](https://github.com/p-baleine/metaanalyser) for details
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
