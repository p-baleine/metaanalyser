from langchain.output_parsers import PydanticOutputParser
from langchain.prompts import (
    ChatPromptTemplate,
    PromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from pydantic import BaseModel, Field
from typing import List


class Overview(BaseModel):

    title: str = Field(description="title of the systematic review")
    main_points: List[str] = Field(description="main points that make up the systematic review")
    overview: str = Field(description="overview of the systematic review")

    def __str__(self):
        points = "\n  - ".join(self.main_points)
        return f"""
Title: {self.title}
Points:
  - {points}
Overview: {self.overview}
""".strip()

    def _repr_html_(self):
        main_points = "".join([f"<li>{p}</li>" for p in self.main_points])

        return (
            "<div>"
            f"  <div><span style=\"font-weight: bold\">Title:</span>"
            f"    <span style=\"margin-left: 5px\">{self.title}</span>"
            f"  </div>"
            f"  <div><span style=\"font-weight: bold\">Main points:</span>"
            f"    <ul style=\"margin: 0 10px\">{main_points}</ul>"
            f"  </div>"
            f"  <div><span style=\"font-weight: bold\">Overview:</span>"
            f"    <span style=\"margin-left: 5px\">{self.overview}</span>"
            f"  </div>"
            "</div>"
        )


output_parser = PydanticOutputParser(pydantic_object=Overview)

system_template = "You are a research scientist and intereseted in {categories}. You are working on writing a systematic review regarding \"{query}\"."
system_prompt = SystemMessagePromptTemplate.from_template(system_template)

human_template = """Write an overview of the systematic review based on the summary of the following list of paper abstracts.

-----
{abstracts}
-----

This overview should serve as a compass for you as you construct the outline of the systematic review and write down its details.

Assuming that the readers of this systematic review will not be familiar with the field. In order to make it easy for readers who are not familiar with this field to understand, list the main points briefly (approximately 30 words maximum) based on the following points.

- Motivation for this field and the problem this field are trying to solve
- Historical background of this field
- Future development of this field

Based on these main points, provide an overview of the systematic review regarding {query} you will write.

Finally, write the title of the systematic review you are going to write based on this overview.

{format_instructions}"""
human_prompt = HumanMessagePromptTemplate(
    prompt=PromptTemplate(
        template=human_template,
        input_variables=["abstracts", "query"],
        partial_variables={
            "format_instructions": output_parser.get_format_instructions()
        }
    )
)

OVERVIEW_PROMPT = ChatPromptTemplate.from_messages([system_prompt, human_prompt])
