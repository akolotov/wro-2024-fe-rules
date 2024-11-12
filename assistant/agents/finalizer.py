import time
from configuration.constants import constants
from llms import ChatModel
from helper import read_file_content
from .transformers.to_json.finalizer import parse
from .transformers.to_xml.assistant import format_input
from data_structures.inputs.assistant import AssistantRequest
from data_structures.responses.finalizer import FinalizerResponse
from data_structures.report import Report, Metadata

class FinalizerAgent:
    def __init__(self):
        prompt_path = constants.prompts_path / constants.finalizer_prompt_file
        summary_path = constants.rules_path / constants.summary_file
        annotations_path = constants.rules_path / constants.annotations_file

        prompt_template = read_file_content(prompt_path)
        summary_content = read_file_content(summary_path)
        annotations_content = read_file_content(annotations_path)

        system_prompt = prompt_template.format(
            summary_filename=constants.summary_file,
            summary_file_content=summary_content,
            annotations_filename=constants.annotations_file,
            annotations_file_content=annotations_content
        )

        self.model = ChatModel(system_prompt)

    def process_question(self, request: AssistantRequest) -> Report[FinalizerResponse]:
        formatted_question = format_input(request)

        # Measure the duration of the generate_response call
        start_time = time.time()
        res = self.model.generate_response(formatted_question)
        duration = time.time() - start_time

        parsed_response = parse(res.response)

        # Create metadata instance
        metadata = Metadata(
            prompt_token_count=res.metadata.prompt_token_count,
            candidates_token_count=res.metadata.candidates_token_count,
            total_token_count=res.metadata.total_token_count,
            duration=duration
        )

        # Create and return the report
        return Report[FinalizerResponse](
            metadata=metadata,
            response=parsed_response
        )
