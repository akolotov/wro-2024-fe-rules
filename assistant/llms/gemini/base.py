import os
from datetime import datetime
import proto
from textwrap import dedent
from typing import Optional
import logging

import google.generativeai as genai
from google.generativeai import protos
from google.ai.generativelanguage_v1beta.types import content, GenerateContentResponse

from ..types import ChatModelConfig, RawChatModelResponse

# From google.ai.generativelanguage_v1beta.types.GenerateContentResponse
# google/ai/generativelanguage_v1beta/types/generative_service.py
class UsageMetadata(proto.Message):
    r"""Metadata on the generation request's token usage.

    Attributes:
        prompt_token_count (int):
            Number of tokens in the prompt. When ``cached_content`` is
            set, this is still the total effective prompt size meaning
            this includes the number of tokens in the cached content.
        cached_content_token_count (int):
            Number of tokens in the cached part of the
            prompt (the cached content)
        candidates_token_count (int):
            Total number of tokens across all the
            generated response candidates.
        total_token_count (int):
            Total token count for the generation request
            (prompt + response candidates).
    """

    prompt_token_count: int = proto.Field(
        proto.INT32,
        number=1,
    )
    cached_content_token_count: int = proto.Field(
        proto.INT32,
        number=4,
    )
    candidates_token_count: int = proto.Field(
        proto.INT32,
        number=2,
    )
    total_token_count: int = proto.Field(
        proto.INT32,
        number=3,
    )

# From google.ai.generativelanguage_v1beta.types.Candidate
# google/ai/generativelanguage_v1beta/types/generative_service.py
class FinishReason(proto.Enum):
    r"""Defines the reason why the model stopped generating tokens.

    Values:
        FINISH_REASON_UNSPECIFIED (0):
            Default value. This value is unused.
        STOP (1):
            Natural stop point of the model or provided
            stop sequence.
        MAX_TOKENS (2):
            The maximum number of tokens as specified in
            the request was reached.
        SAFETY (3):
            The response candidate content was flagged
            for safety reasons.
        RECITATION (4):
            The response candidate content was flagged
            for recitation reasons.
        LANGUAGE (6):
            The response candidate content was flagged
            for using an unsupported language.
        OTHER (5):
            Unknown reason.
        BLOCKLIST (7):
            Token generation stopped because the content
            contains forbidden terms.
        PROHIBITED_CONTENT (8):
            Token generation stopped for potentially
            containing prohibited content.
        SPII (9):
            Token generation stopped because the content
            potentially contains Sensitive Personally
            Identifiable Information (SPII).
        MALFORMED_FUNCTION_CALL (10):
            The function call generated by the model is
            invalid.
    """
    FINISH_REASON_UNSPECIFIED = 0
    STOP = 1
    MAX_TOKENS = 2
    SAFETY = 3
    RECITATION = 4
    LANGUAGE = 6
    OTHER = 5
    BLOCKLIST = 7
    PROHIBITED_CONTENT = 8
    SPII = 9
    MALFORMED_FUNCTION_CALL = 10


class GeminiChatModelConfig(ChatModelConfig):
    """
    Configuration for a Gemini chat model.

    Attributes:
        session_id (str): ID of the session, used to identify the session of several agents
        agent_id (str): ID of the agent, used to identify the agent in the session
        llm_model_name (str): Name of the Gemini model to use (defaults to "gemini-1.5-flash-002")
        temperature (float): Controls randomness in the model's responses. 
            Higher values (e.g., 0.8) make output more random, lower values (e.g., 0.2) make it more focused
        system_prompt (str): Initial system prompt to set model behavior and context
        response_schema (Optional[content.Schema]): Schema defining the expected response format.
            If provided, responses will be formatted as JSON matching this schema.
            Defaults to None.
        max_tokens (Optional[int]): Maximum number of tokens in the response.
        keep_raw_engine_responses (bool): Whether to keep raw LLM responses.
        raw_engine_responses_dir (str): Directory to save raw LLM responses.
    """
    response_schema: Optional[content.Schema] = None
    llm_model_name: str = "gemini-1.5-flash-002"

    class Config:
        arbitrary_types_allowed = True


class GeminiChatModelResponse(RawChatModelResponse):
    response: Optional[str] = None
    metadata: Optional[GenerateContentResponse.UsageMetadata] = None

    class Config:
        arbitrary_types_allowed = True

class BaseChatModel:
    """A wrapper class for the Gemini generative model that maintains conversation history.

    This class provides an interface to interact with Google's Gemini model while
    maintaining the conversation history between prompts and responses.

    Attributes:
        model: The underlying Gemini generative model instance
        _history: List of conversation turns between user and model
    """

    def __init__(self, config: ChatModelConfig):
        """Initialize a new BaseChatModel instance.

        Args:
            config (ChatModelConfig): Configuration for the chat model
        """
        generation_config = genai.types.GenerationConfig(
            temperature=config.temperature if config.temperature is not None else 1.0,
            top_p=0.95,
            top_k=40,
            max_output_tokens=config.max_tokens,
        )

        if config.response_schema:
            generation_config.response_schema = config.response_schema
            generation_config.response_mime_type = "application/json"

        self._generation_config = generation_config

        self.model = genai.GenerativeModel(
            model_name=config.llm_model_name,
            system_instruction=config.system_prompt
        )

        self._history: list[protos.Content] = []

        self._session_id = config.session_id
        self._agent_id = config.agent_id
        self._keep_raw_engine_responses = config.keep_raw_engine_responses
        self._raw_engine_responses_dir = config.raw_engine_responses_dir

    def _save_response(self, response: dict):
        """Save the raw response from the Gemini model to a file for debugging/logging purposes.

        If enabled via settings, saves the complete model response to a timestamped file
        in a directory structure organized by session ID. The agent_id is included in the 
        filename to distinguish responses from different agents within the same session.

        Args:
            response (dict): The raw response dictionary from the Gemini model
        """

        if self._keep_raw_engine_responses:
            response_dir = os.path.join(
                self._raw_engine_responses_dir, self._session_id)
            os.makedirs(response_dir, exist_ok=True)
            file_path = os.path.join(
                response_dir,
                f"{self._agent_id}_{
                    datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"
            )
            with open(file_path, "w") as f:
                f.write(str(response))

    def _generate_response(self, prompt: str, response_schema: Optional[content.Schema] = None) -> GeminiChatModelResponse:
        """Generate a response from the model based on the given prompt.

        The prompt is added to the conversation history before generating the response.
        The response is also added to the history for context in future interactions,
        but only if generation is successful (finishes with STOP reason).
        If there's an error or unexpected finish reason, the prompt is removed from history.

        Args:
            prompt (str): The input text to send to the model

        Returns:
            GeminiChatModelResponse: The response from the Gemini model

        Raises:
            GeminiModelError: If there is an error generating the response
            GeminiUnexpectedFinishReason: If the model stops for an unexpected reason
        """

        logger = logging.getLogger(self.__class__.__module__)

        # Add prompt to history
        prompt_content = protos.Content(
            parts=[protos.Part(text=dedent(prompt))], role="user")
        self._history.append(prompt_content)

        generation_config = self._generation_config
        if response_schema:
            generation_config.response_schema = response_schema
            generation_config.response_mime_type = "application/json"

        try:
            # Request response from model for the prompt added to history
            response = self.model.generate_content(self._history, generation_config=generation_config)
        except Exception as e:
            # Roll back the prompt from history on error to avoid keeping prompts without
            # responses in history
            self._history.pop()
            logger.error(f"Error generating response: {e}")
            return GeminiChatModelResponse(
                success=False,
                failure_reason=("Error generating response", str(e))
            )

        # Before processing the response, save it to a file as is
        self._save_response(response.candidates[0])

        # Get the finish reason for the response
        finish_reason = FinishReason(response.candidates[0].finish_reason)

        if finish_reason == FinishReason.STOP:
            # Add the response to history to be used as context in future interactions
            self._history.append(response.candidates[0].content)
            return GeminiChatModelResponse(
                success=True,
                response=response.candidates[0].content.parts[0].text,
                metadata=response.usage_metadata
            )
        else:
            # Roll back the prompt from history on error to avoid keeping prompts without
            # responses in history
            self._history.pop()
            logger.error(f"Unexpected finish reason: {finish_reason.name}")
            return GeminiChatModelResponse(
                success=False,
                failure_reason=("Unexpected finish reason", finish_reason.name)
            )
