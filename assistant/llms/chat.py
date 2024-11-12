import google.generativeai as genai
from configuration.constants import constants
from google.generativeai import protos
from configuration.gemini import gemini_settings

from .gemini import initialize as initialize_gemini, BaseChatModel as GeminiModel
from .types import ChatModelConfig, RawChatModelResponse
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

    def generate_response(self, prompt: str) -> RawChatModelResponse:
        res = self._generate_response(prompt)

        if res.success:
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


