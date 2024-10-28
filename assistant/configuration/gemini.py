from pydantic_settings import BaseSettings
from pydantic import Field, field_validator
from dotenv import load_dotenv

load_dotenv()

class GeminiSettings(BaseSettings):
    api_key: str
    model: str = "gemini-1.5-flash-002"

    @field_validator('api_key')
    def api_key_must_not_be_empty(cls, v):
        if not v:
            raise ValueError("GEMINI_API_KEY environment variable is not set")
        return v

    class Config:
        env_prefix = "GEMINI_"

gemini_settings = GeminiSettings()