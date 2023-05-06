import logging
from langchain.base_language import BaseLanguageModel
from langchain.chains.llm import LLMChain
from langchain.callbacks.manager import CallbackManagerForChainRun
from langchain.output_parsers import RetryWithErrorOutputParser
from langchain.prompts.base import BasePromptTemplate
from langchain.schema import BaseOutputParser, OutputParserException
from typing import Any, Dict, List, Optional

logger = logging.getLogger(__name__)


class SRBaseChain(LLMChain):

    def _call(
        self,
        inputs: Dict[str, Any],
        run_manager: Optional[CallbackManagerForChainRun] = None,
    ) -> Dict[str, str]:
        response = self.generate(inputs, run_manager=run_manager)
        # トークンの利用状況を確認したい
        logger.info(f"LLM utilization: {response.llm_output}")
        return self.create_outputs(response)[0]

    def _acall(
        self,
        inputs: Dict[str, Any],
        run_manager: Optional[CallbackManagerForChainRun] = None,
    ) -> Dict[str, str]:
        response = self.agenerate(inputs, run_manager=run_manager)
        logger.info(f"LLM utilization: {response.llm_output}")
        return self.create_outputs(response)[0]


def maybe_retry_with_error_output_parser(
        llm: BaseLanguageModel,
        input_list: List[Dict[str, str]],
        output: Dict[str, str],
        output_parser: BaseOutputParser,
        output_key: str,
        prompt: BasePromptTemplate,
):
    retry_parser = RetryWithErrorOutputParser.from_llm(
        parser=output_parser,
        llm=llm,
    )

    try:
        output_text = output_parser.parse(output[output_key])
    except OutputParserException as e:
        logger.warning(f"An error occurred on parsing output, retrying parse, {e}")

        output_text = retry_parser.parse_with_prompt(
            output[output_key],
            prompt.format_prompt(**(input_list[0]))
        )

    return {output_key: output_text}
