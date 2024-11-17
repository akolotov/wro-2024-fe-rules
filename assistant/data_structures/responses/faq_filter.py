import json
from pydantic import Field
from typing import Any

from google.ai.generativelanguage_v1beta.types import content

from .base import BaseResponse
from llms.types import LLMEngine

class FAQFilterResponse(BaseResponse):
    """
    Pydantic model for the FAQ filter assistant agent's response structure.
    Includes validation, documentation, and examples.
    """
    question: str = Field(
        ...,
        description="The FAQ question that is most relevant to the user's question.",
    )

    applicable: bool = Field(
        ...,
        description="False, if the question is not applicable to the 'Questions and answers' part otherwise True.",
    )

    answer: str = Field(
        ...,
        description="The answer found in the FAQ part of the rules.",
    )

    class Config:
        json_schema_extra = {
            "example": {
                "question": "Ho w many laps are required in the Open Challenge?",
                "applicable": True,
                "chain_of_thought": "1. Analyzed question context\n2. Reviewed relevant rules\n3. Formulated response",
                "answer": "According to section 3.1 of the rules, teams must complete 3 laps in the Open Challenge."
            }
        }

    @classmethod
    def llm_schema(cls, engine: LLMEngine) -> Any:
        if engine == LLMEngine.GEMINI:
            return content.Schema(
                type=content.Type.OBJECT,
                required=["chain_of_thought", "applicable", "question", "answer"],
                properties={
                    "chain_of_thought": content.Schema(
                        type=content.Type.STRING,
                    ),
                    "applicable": content.Schema(
                        type=content.Type.BOOLEAN,
                    ),
                    "question": content.Schema(
                        type=content.Type.STRING,
                    ),
                    "answer": content.Schema(
                        type=content.Type.STRING,
                    ),
                },
            )
        else:
            raise ValueError(f"Unsupported engine: {engine}")
        
    @classmethod
    def deserialize(cls, response: str, engine: LLMEngine) -> "FAQFilterResponse":
        if engine == LLMEngine.GEMINI:
            data = json.loads(response)

            return FAQFilterResponse(
                chain_of_thought=data["chain_of_thought"],
                question=data["question"],
                applicable=data["applicable"],
                answer=data["answer"]
            )
                
        else:
            raise ValueError(f"Unsupported engine: {engine}")