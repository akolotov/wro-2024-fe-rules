import time
from configuration.constants import constants
from llms import gemini
from helper import read_file_content
from data_structures.responses.assistant import BaseAssistantResponse
from data_structures.report import Report, Metadata, CombinedAssistantReport
from data_structures.inputs.assistant import AssistantRequest
from .transformers.to_xml.assistant import format_input
from .transformers.to_json.assistant import parse_response, parse_verification
from data_structures.responses.assistant import FirstAssistantResponse, SubsequentAssistantResponse, VerificationAssistantResponse, FirstResponseRule, SubsequentResponseRule

class AssistantAgent:
    def __init__(self, section_filename: str):
        summary_content = read_file_content(constants.rules_path / constants.summary_file)

        section_rules_content = read_file_content(constants.rules_path / section_filename)

        if section_filename in constants.dependant_sections:
            dependant_section_filename = constants.dependant_sections[section_filename][0]
            dependant_section_rules_content = read_file_content(constants.rules_path / dependant_section_filename)

            prompt_template = read_file_content(constants.prompts_path / constants.assistant_system_multi_section_prompt_file)

            system_prompt = prompt_template.format(
                summary_filename=constants.summary_file,
                summary_file_content=summary_content,
                section_filename=section_filename,
                section_file_content=section_rules_content,
                dependant_section_filename=dependant_section_filename,
                dependant_section_file_content=dependant_section_rules_content
            )
        else:
            prompt_template = read_file_content(constants.prompts_path / constants.assistant_system_prompt_file)

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
        if proposal.response.applicable:
            verification = self._verification(request.response is not None)
        else:
            verification = None

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
        print(f"-- Proposal will be generated")
        
        if request.response:
            prompt_file = constants.assistant_next_general_prompt_file
            if self.section_filename in constants.special_assistant_prompts_files:    
                prompt_file = constants.special_assistant_prompts_files[self.section_filename][1]
        else:
            prompt_file = constants.assistant_first_general_prompt_file
            if self.section_filename in constants.special_assistant_prompts_files:
                prompt_file = constants.special_assistant_prompts_files[self.section_filename][0]

        print(f"-- {prompt_file} will be used")

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
            if base_response.relevant_rules:
                relevant_rules = []
                for rule in base_response.relevant_rules:
                    relevant_rules.append(SubsequentResponseRule(
                        section=rule.section,
                        id=rule.id,
                        content=rule.content,
                        explanation=rule.explanation
                    ))
            else:
                relevant_rules = None

            response = SubsequentAssistantResponse(
                question=base_response.question,
                relevant_rules=relevant_rules,
                chain_of_thought=base_response.chain_of_thought,
                applicable=base_response.applicable,
                answer=base_response.answer,
            )
            return Report[SubsequentAssistantResponse](
                metadata=metadata,
                response=response
            )
        else:
            if base_response.relevant_rules:
                relevant_rules = []
                for rule in base_response.relevant_rules:
                    relevant_rules.append(FirstResponseRule(
                        section=rule.section,
                        id=rule.id,
                        content=rule.content,
                        explanation=rule.explanation
                    ))
            else:
                relevant_rules = None

            response = FirstAssistantResponse(
                question=base_response.question,
                relevant_rules=relevant_rules,
                chain_of_thought=base_response.chain_of_thought, 
                applicable=base_response.applicable,
                answer=base_response.answer
            )
            return Report[FirstAssistantResponse](
                metadata=metadata,
                response=response
            )

    def _verification(self, is_subsequent: bool) -> Report[VerificationAssistantResponse]:
        print(f"-- Verification will be generated")

        if is_subsequent:
            prompt_file = constants.assistant_next_verification_prompt_file
        else:
            prompt_file = constants.assistant_first_verification_prompt_file

        print(f"-- {prompt_file} will be used")

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
