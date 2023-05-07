from langchain.output_parsers import PydanticOutputParser
from langchain.prompts import (
    ChatPromptTemplate,
    PromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from pydantic import BaseModel, Field
from typing import List, Optional


class Section(BaseModel):

    title: str = Field(description="title of this section")
    children: Optional[List["Section"]] = Field(description="subsections of this section")
    description: str = Field(description="brief description of this section (approximately 30 words maximum)")
    citation_ids: List[int] = Field(description="citation ids to a paper abstract that this section cites")


class Outlint(BaseModel):

    sections: List[Section] = Field(description="sections that make up this systematic review")
    citations_ids: List[int] = Field(description="citation ids to all paper abstracts cited in this paper")

    def __str__(self):
        def section_string(idx: int, section: Section, indent_level: int):
            result = [f"{idx}. {section.title}: {section.description}"]

            if not section.children:
                return result[0]

            result += [
                section_string(
                    ("    " * (indent_level + 1)) + f"{child_idx}",
                    child,
                    indent_level + 1
                )
                for child_idx, child in enumerate(section.children, start=1)
            ]
            return "\n".join(result)

        return "\n".join([
            section_string(idx, s, 0)
            for idx, s in enumerate(self.sections, start=1)
        ])


output_parser = PydanticOutputParser(pydantic_object=Outlint)

system_template = "You are a research scientist and intereseted in {categories}. You are working on writing a systematic review regarding \"{query}\"."
system_prompt = SystemMessagePromptTemplate.from_template(system_template)

human_template = """Build an outline of the systematic review regarding \"{query}\" based on the following list of paper abstracts.

-----
{abstracts}
-----

The following is an overview of this systematic review. Build the outline of the systematic review according to this overview.

-----
{overview}
-----

Device each section of this outline by citing abstracts from the papers.
The beginning of element of the sections should by titled "Introduction" and last element of the sections should be titled "Conclusion".
It is preferred that sections be divided into more child sections. Each section can have up to two child sections.

{format_instructions}"""
human_prompt = HumanMessagePromptTemplate(
    prompt=PromptTemplate(
        template=human_template,
        input_variables=["query", "abstracts", "overview"],
        partial_variables={
            "format_instructions": output_parser.get_format_instructions()
        }
    )
)

OUTLINE_PROMPT = ChatPromptTemplate.from_messages([system_prompt, human_prompt])
