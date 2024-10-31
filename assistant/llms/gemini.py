import google.generativeai as genai
from configuration.constants import constants
from google.generativeai import protos
from configuration.gemini import gemini_settings

def initialize():
    genai.configure(api_key=gemini_settings.api_key)

class GeminiModel:
    """A wrapper class for the Gemini generative model that maintains conversation history.

    This class provides an interface to interact with Google's Gemini model while
    maintaining the conversation history between prompts and responses.

    Attributes:
        model: The underlying Gemini generative model instance
        _history: List of conversation turns between user and model
    """

    def __init__(self, system_prompt: str):
        """Initialize the Gemini model with system prompt and default settings.

        Args:
            system_prompt: The system instruction prompt to guide model behavior
        """
        self.model = genai.GenerativeModel(
            gemini_settings.model,
            system_instruction=system_prompt,
            generation_config=genai.types.GenerationConfig(
                temperature=constants.generation_temperature,
                top_p=0.95,
                top_k=40,
                max_output_tokens=8192
            )        
        )
        self._history: list[protos.Content] = []

    @property
    def history(self) -> list[protos.Content]:
        """Get the conversation history.

        Returns:
            List of Content objects representing the conversation history
        """
        return self._history

    def generate_response(self, prompt: str) -> tuple[str, dict]:
        """Generate a response from the model given a prompt.

        Adds the prompt and response to conversation history.

        Args:
            prompt: The text prompt to send to the model

        Returns:
            A tuple containing:
                - The generated response text from the model
                - The response metadata dictionary containing token usage:
                    - prompt_token_count
                    - candidates_token_count
                    - total_token_count
        """
        self._history.append(protos.Content(parts=[protos.Part(text=prompt)], role="user"))
        response = self.model.generate_content(self._history)

        self._history.append(response.candidates[0].content)
        return response.candidates[0].content.parts[0].text, response.usage_metadata