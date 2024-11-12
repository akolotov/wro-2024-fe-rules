import time
from configuration.constants import constants
from llms import ChatModel
from helper import read_file_content
from .transformers.to_json.router import parse
from .transformers.to_xml.common import format_input
from data_structures.inputs.common import UserRequest
from data_structures.responses.router import RouterResponse
from data_structures.report import Report, Metadata

class RouterAgent:
    def __init__(self):
        prompt_path = constants.prompts_path / constants.router_prompt_file
        annotations_path = constants.rules_path / constants.annotations_file

        prompt_template = read_file_content(prompt_path)
        annotations_content = read_file_content(annotations_path)

        system_prompt = prompt_template.format(
            annotations_filename=constants.annotations_file,
            annotations_file_content=annotations_content
        )

        self.model = ChatModel(system_prompt)

    def process_question(self, input: str) -> Report[RouterResponse]:
        user_request = UserRequest(request=input)
        formatted_question = format_input(user_request)

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
        return Report[RouterResponse](
            metadata=metadata,
            response=parsed_response
        )
