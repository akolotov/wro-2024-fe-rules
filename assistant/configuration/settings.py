from pydantic_settings import BaseSettings
from pydantic import Field
from pathlib import Path

class Settings(BaseSettings):
    prompts_path: Path = Field(default=Path("../prompts/gemini/team"), env="PROMPTS_PATH")
    rules_path: Path = Field(default=Path("../rules"), env="RULES_PATH")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        extra = "ignore"

# Create a single settings instance to be used throughout the application
settings = Settings() 