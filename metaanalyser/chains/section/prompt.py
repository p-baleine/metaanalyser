from langchain.prompts import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)


system_template = """You are a research scientist and intereseted in {categories}. You are working on writing a systematic review regarding \"{query}\".

The outline of the systematic review is as follows:

-----
Title: {title}
{outline}"""
system_prompt = SystemMessagePromptTemplate.from_template(system_template)

human_template = """Write the "{section_title}" section of this systematic review based on the following list of snippets or abstracts of relative papers.

-----
{snippets}
-----

This systematic review should adhere to the following overview:

{overview}

Write the "{section_title}" section with respect to this overview. Write the text in markdown format. The title of this section should bu suffixed with {section_level} level markdown title (`{md_title_suffix}`). The text of the section should be based on a snippet or abstact and should be clearly cited. The citation should be written at the end of the sentence in the form `[^cite_id]`."""
human_prompt = HumanMessagePromptTemplate.from_template(human_template)

SECTION_PROMPT = ChatPromptTemplate.from_messages([
    system_prompt,
    human_prompt,
])
