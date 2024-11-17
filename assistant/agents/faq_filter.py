import time

from configuration.constants import constants
from llms import ChatModel
from helper import read_file_content
from data_structures.inputs.common import UserRequest
from data_structures.responses.faq_filter import FAQFilterResponse
from data_structures.report import Report, Metadata, FAQFilterReport

class FAQFilterAgent:
    def __init__(self):
        prompt_path = constants.prompts_path / constants.faq_filter_system_prompt_file
        summary_path = constants.rules_path / constants.summary_file
        faq_path = constants.rules_path / constants.faq_file

        prompt_template = read_file_content(prompt_path)
        summary_content = read_file_content(summary_path)
        faq_content = read_file_content(faq_path)

        system_prompt = prompt_template.format(
            summary_filename=constants.summary_file,
            summary_file_content=summary_content,
            faq_filename=constants.faq_file,
            faq_file_content=faq_content
        )

        self.model = ChatModel(system_prompt)

    def filter_question(self, input: str) -> FAQFilterReport:
        applicability_report = self._check_applicability(input)
        confirmation_report = self._confirm_applicability()

        return FAQFilterReport(
            handler=applicability_report,
            verification=confirmation_report
        )
    
    def _check_applicability(self, input: str) -> Report[FAQFilterResponse]:
        main_prompt_path = constants.prompts_path / constants.faq_filter_handler_prompt_file
        main_prompt_template = read_file_content(main_prompt_path)

        user_request = UserRequest(request=input)

        prompt_content = main_prompt_template.format(
            user_request=user_request.model_dump_json()
        )

        # Measure the duration of the generate_response call
        start_time = time.time()
        res = self.model.generate_response(prompt_content, response_class=FAQFilterResponse)
        duration = time.time() - start_time

        # Create metadata instance
        metadata = Metadata(
            prompt_token_count=res.metadata.prompt_token_count,
            candidates_token_count=res.metadata.candidates_token_count,
            total_token_count=res.metadata.total_token_count,
            duration=duration
        )

        # Create and return the report
        return Report[FAQFilterResponse](
            metadata=metadata,
            response=res.response
        )

    def _confirm_applicability(self) -> Report[FAQFilterResponse]:
        verification_prompt_path = constants.prompts_path / constants.faq_filter_verification_prompt_file
        verification_prompt = read_file_content(verification_prompt_path)

        # Measure the duration of the generate_response call
        start_time = time.time()
        res = self.model.generate_response(verification_prompt, response_class=FAQFilterResponse)
        duration = time.time() - start_time

        # Create metadata instance
        metadata = Metadata(
            prompt_token_count=res.metadata.prompt_token_count,
            candidates_token_count=res.metadata.candidates_token_count,
            total_token_count=res.metadata.total_token_count,
            duration=duration
        )

        # Create and return the report
        return Report[FAQFilterResponse](
            metadata=metadata,
            response=res.response
        )
