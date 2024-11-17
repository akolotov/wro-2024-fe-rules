from pydantic import BaseModel, Field
from typing import Any

from google.ai.generativelanguage_v1beta.types import content

from llms.types import LLMEngine

class BaseResponse(BaseModel):
    """
    Pydantic model for the complete response structure.
    Includes validation, documentation, and examples.
    """
    chain_of_thought: str = Field(
        ...,
        description="The step-by-step reasoning process.",
        min_length=1
    )

    class Config:
        json_schema_extra = {
            "example": {
                "chain_of_thought": "1. Analyzed question context\n2. Identified key terms\n3. Selected most likely interpretation",
            }
        }

    @classmethod
    def llm_schema(cls, _engine: LLMEngine) -> Any:
        raise NotImplementedError("LLM schema not implemented for this response")
    
    @classmethod
    def deserialize(cls, _response: str, _engine: LLMEngine) -> "BaseResponse":
        raise NotImplementedError("Deserialization not implemented for this response")