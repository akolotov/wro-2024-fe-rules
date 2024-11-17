from configuration.constants import constants
from configuration.gemini import gemini_settings
from data_structures.responses.base import BaseResponse

from .gemini import initialize as initialize_gemini, BaseChatModel as GeminiModel
from .types import ChatModelConfig, RawChatModelResponse, LLMEngine, DeserializedChatModelResponse
from .exceptions import GenerationError, UnexpectedFinishReason

def initialize():
    initialize_gemini(api_key=gemini_settings.api_key)

class ChatModel(GeminiModel):
    def __init__(self, system_prompt: str):
        super().__init__(ChatModelConfig(
                llm_model_name=gemini_settings.model,
                temperature=constants.generation_temperature,
                system_prompt=system_prompt
            )
        )

    def generate_response(self, prompt: str, response_class: BaseResponse = None) -> RawChatModelResponse:
        if response_class:
            res = self._generate_response(prompt, response_schema=response_class.llm_schema(LLMEngine.GEMINI))
        else:
            res = self._generate_response(prompt)

        if res.success:
            if response_class:
                return DeserializedChatModelResponse(
                    success=True,
                    response=response_class.deserialize(res.response, LLMEngine.GEMINI),
                    metadata=res.metadata
                )
            else:
                return RawChatModelResponse(
                    success=True,
                    response=res.response,
                    metadata=res.metadata
                )
        else:
            if res.failure_reason[0] == "Error generating response":
                raise GenerationError(f"{res.failure_reason[0]}: {res.failure_reason[1]}")
            else:
                raise UnexpectedFinishReason(res.failure_reason[1])

class ChatModelWithSchema(GeminiModel):
    def __init__(self, system_prompt: str, response_class: BaseResponse):
        super().__init__(ChatModelConfig(
                llm_model_name=gemini_settings.model,
                temperature=constants.generation_temperature,
                system_prompt=system_prompt,
                response_schema=response_class.llm_schema(LLMEngine.GEMINI)
            )
        )

        self._response_class = response_class

    def generate_response(self, prompt: str) -> RawChatModelResponse:
        res = self._generate_response(prompt)

        if res.success:
            return DeserializedChatModelResponse(
                success=True,
                response=self._response_class.deserialize(res.response, LLMEngine.GEMINI),
                metadata=res.metadata
            )
        else:
            if res.failure_reason[0] == "Error generating response":
                raise GenerationError(f"{res.failure_reason[0]}: {res.failure_reason[1]}")
            else:
                raise UnexpectedFinishReason(res.failure_reason[1])


