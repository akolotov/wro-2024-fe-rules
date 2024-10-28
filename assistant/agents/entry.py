import time
from configuration.constants import constants
from llms import gemini
from helper import read_file_content
from .transformers.to_json.entry import parse
from .transformers.to_xml.common import format_input
from data_structures.inputs.common import UserRequest
from data_structures.responses.entry import EntryResponse
from data_structures.report import Report, Metadata

class EntryAgent:
    def __init__(self):
        prompt_path = constants.prompts_path / constants.entry_prompt_file
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

        self.model = gemini.GeminiModel(system_prompt)

    def process_question(self, input: str) -> Report[EntryResponse]:
        user_request = UserRequest(request=input)
        formatted_question = format_input(user_request)

        # Measure the duration of the generate_response call
        start_time = time.time()
        raw_text_response, usage_metadata = self.model.generate_response(formatted_question)
        duration = time.time() - start_time

        parsed_response = parse(raw_text_response)

        # Create metadata instance
        metadata = Metadata(
            prompt_token_count=usage_metadata.prompt_token_count,
            candidates_token_count=usage_metadata.candidates_token_count,
            total_token_count=usage_metadata.total_token_count,
            duration=duration
        )

        # Create and return the report
        return Report[EntryResponse](
            metadata=metadata,
            response=parsed_response
        )
