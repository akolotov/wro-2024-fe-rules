import time

from configuration.constants import constants
from configuration.settings import settings
from llms import ChatModel
from helper import read_file_content
from data_structures.responses.assistant import BaseAssistantResponse
from data_structures.report import Report, Metadata, CombinedAssistantReport
from data_structures.inputs.assistant import AssistantRequest
from data_structures.inputs.documents import ContextualDocument, DocumentsForContext
from .transformers.to_xml.assistant import format_input
from .transformers.to_json.assistant import parse_response, parse_verification
from data_structures.responses.assistant import FirstAssistantResponse, SubsequentAssistantResponse, VerificationAssistantResponse, FirstResponseRule, SubsequentResponseRule
from llms.types import LLMDataFormat

class AssistantAgent:
    def __init__(self, section_filename: str):
        summary_document = ContextualDocument(source=constants.summary_file, content=read_file_content(settings.rules_path / constants.summary_file), index=1)

        section_files = [section_filename]
        if section_filename in constants.dependant_sections:
            section_files.extend(constants.dependant_sections[section_filename])

        section_documents = []
        for n, filename in enumerate(section_files):
            section_documents.append(ContextualDocument(source=filename, content=read_file_content(settings.rules_path / filename), index=n+2))

        documents_for_context = DocumentsForContext(documents=[summary_document, *section_documents])

        if len(section_files) > 1:
            section_filenames_string = ", ".join([f"`{filename}`" for filename in section_files[:-1]])
            section_filenames_string += f" and `{section_files[-1]}`"
            section_filenames_string = f"files {section_filenames_string}"
        else:
            section_filenames_string = f"the file `{section_files[0]}`"

        prompt_template = read_file_content(settings.prompts_path / constants.assistant_system_prompt_file)
        system_prompt = prompt_template.format(
            documents_for_context=documents_for_context.serialize(format=LLMDataFormat.XML),
            summary_filename=constants.summary_file,
            section_filenames=section_filenames_string
        )

        self.section_filename = section_filename
        self.model = ChatModel(system_prompt)

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

        prompt_template = read_file_content(settings.prompts_path / prompt_file)
        prompt_content = prompt_template.format(
            xml_input=format_input(request)
        )                

        # Measure the duration of the generate_response call
        start_time = time.time()
        res = self.model.generate_response(prompt_content)
        duration = time.time() - start_time

        # Parse the base response
        base_response = parse_response(res.response)

        # Create metadata instance
        metadata = Metadata(
            prompt_token_count=res.metadata.prompt_token_count,
            candidates_token_count=res.metadata.candidates_token_count,
            total_token_count=res.metadata.total_token_count,
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

        prompt_content = read_file_content(settings.prompts_path / prompt_file)

        # Measure the duration of the generate_response call
        start_time = time.time()
        res = self.model.generate_response(prompt_content)
        duration = time.time() - start_time

        # Parse the base response
        response = parse_verification(res.response)

        # Create metadata instance
        metadata = Metadata(
            prompt_token_count=res.metadata.prompt_token_count,
            candidates_token_count=res.metadata.candidates_token_count,
            total_token_count=res.metadata.total_token_count,
            duration=duration
        )

        return Report[VerificationAssistantResponse](
            metadata=metadata,
            response=response
        )
