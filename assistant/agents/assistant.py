import time
from configuration.constants import constants
from llms import gemini
from helper import read_file_content
from data_structures.responses.assistant import BaseAssistantResponse
from data_structures.report import Report, Metadata, CombinedAssistantReport
from data_structures.inputs.assistant import AssistantRequest
from .transformers.to_xml.assistant import format_input
from .transformers.to_json.assistant import parse_response, parse_verification
from data_structures.responses.assistant import FirstAssistantResponse, SubsequentAssistantResponse, VerificationAssistantResponse

class AssistantAgent:
    def __init__(self, section_filename: str):
        prompt_path = constants.prompts_path / constants.assistant_system_prompt_file
        summary_path = constants.rules_path / constants.summary_file
        section_rules_path = constants.rules_path / section_filename

        prompt_template = read_file_content(prompt_path)
        summary_content = read_file_content(summary_path)
        section_rules_content = read_file_content(section_rules_path)

        system_prompt = prompt_template.format(
            summary_filename=constants.summary_file,
            summary_file_content=summary_content,
            section_filename=section_filename,
            section_file_content=section_rules_content
        )

        self.section_filename = section_filename
        self.model = gemini.GeminiModel(system_prompt)

    def brainstorm_contribution(self, request: AssistantRequest) -> CombinedAssistantReport[BaseAssistantResponse]:
        proposal = self._proposal(request)
        print(f"proposal.response? {request.response}")
        verification = self._verification(request.response is not None)

        if request.response:
            return CombinedAssistantReport[SubsequentAssistantResponse](
                proposal=proposal,
                verification=verification
            )
        else:
            return CombinedAssistantReport[FirstAssistantResponse](
                proposal=proposal,
                verification=verification
            )
        
    def _proposal(self, request: AssistantRequest) -> Report[BaseAssistantResponse]:
        if request.response:
            prompt_file = constants.assistant_next_general_prompt_file
            if self.section_filename in constants.special_assistant_prompts_files:    
                prompt_file = constants.special_assistant_prompts_files[self.section_filename][1]
        else:
            prompt_file = constants.assistant_first_general_prompt_file
            if self.section_filename in constants.special_assistant_prompts_files:
                prompt_file = constants.special_assistant_prompts_files[self.section_filename][0]

        prompt_template = read_file_content(constants.prompts_path / prompt_file)
        prompt_content = prompt_template.format(
            xml_input=format_input(request)
        )                

        # Measure the duration of the generate_response call
        start_time = time.time()
        raw_text_response, usage_metadata = self.model.generate_response(prompt_content)
        duration = time.time() - start_time

        # Parse the base response
        base_response = parse_response(raw_text_response)

        # Create metadata instance
        metadata = Metadata(
            prompt_token_count=usage_metadata.prompt_token_count,
            candidates_token_count=usage_metadata.candidates_token_count,
            total_token_count=usage_metadata.total_token_count,
            duration=duration
        )

        # Convert base response to appropriate type
        if request.response:
            response = SubsequentAssistantResponse(
                question=base_response.question,
                chain_of_thought=base_response.chain_of_thought,
                answer=base_response.answer
            )
            return Report[SubsequentAssistantResponse](
                metadata=metadata,
                response=response
            )
        else:
            response = FirstAssistantResponse(
                question=base_response.question,
                chain_of_thought=base_response.chain_of_thought, 
                answer=base_response.answer
            )
            return Report[FirstAssistantResponse](
                metadata=metadata,
                response=response
            )

    def _verification(self, is_subsequent: bool) -> Report[VerificationAssistantResponse]:
        if is_subsequent:
            prompt_file = constants.assistant_next_verification_prompt_file
        else:
            prompt_file = constants.assistant_first_verification_prompt_file

        prompt_content = read_file_content(constants.prompts_path / prompt_file)

        # Measure the duration of the generate_response call
        start_time = time.time()
        raw_text_response, usage_metadata = self.model.generate_response(prompt_content)
        duration = time.time() - start_time

        # Parse the base response
        response = parse_verification(raw_text_response)

        # Create metadata instance
        metadata = Metadata(
            prompt_token_count=usage_metadata.prompt_token_count,
            candidates_token_count=usage_metadata.candidates_token_count,
            total_token_count=usage_metadata.total_token_count,
            duration=duration
        )

        return Report[VerificationAssistantResponse](
            metadata=metadata,
            response=response
        )
