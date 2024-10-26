from dataclasses import dataclass, field
from typing import Optional, List
from typing_extensions import Annotated
from pydantic import BaseModel, Field, field_validator

class UserRequestInterpretation(BaseModel):
    """
    Pydantic model for a single interpretation of the user's question.
    Includes validation and detailed field descriptions.
    """
    content: str = Field(
        ...,
        description="A possible interpretation of the user's question",
        min_length=1,
        example="How many laps are in the Open Challenge?"
    )
    confidence_score: Optional[float] = Field(
        None,
        description="Confidence score for this interpretation (0-1)",
        ge=0,
        le=1
    )

    class Config:
        json_schema_extra = {
            "example": {
                "content": "How many laps are in the Open Challenge?",
                "confidence_score": 0.95
            }
        }

class EntryResponse(BaseModel):
    """
    Pydantic model for the complete response structure.
    Includes validation, documentation, and examples.
    """
    chain_of_thought: str = Field(
        ...,
        description="The step-by-step reasoning process.",
        min_length=1
    )
    
    original_user_question: str = Field(
        ...,
        description="The exact question as provided by the user, preserved for context.",
        min_length=1
    )
    
    interpretations: Optional[List[UserRequestInterpretation]] = Field(
        None,
        description="List of possible interpretations of the user's question, with confidence scores. Empty if the question is not related to the competition rules."
    )
    
    chosen_interpretation: Optional[UserRequestInterpretation] = Field(
        None,
        description="The most probable interpretation selected by the secretary. None if the question is not related to the competition rules."
    )

    reformulation_request: Optional[str] = Field(
        None,
        description="A reformulation request in the language of the original question if the question is not related to the competition rules. None if the question is related to the competition rules."
    )

    @field_validator('interpretations')
    def validate_interpretations(cls, v):
        if v and len(v) != 3:
            raise ValueError("Must be 3 interpretations")
        return v

    class Config:
        json_schema_extra = {
            "example": {
                "chain_of_thought": "1. Analyzed question context\n2. Identified key terms\n3. Selected most likely interpretation",
                "original_user_question": "How many laps are in the Open Challenge?",
                "interpretations": [
                    {"content": "Asking about number of laps are in the Open Challenge?", "confidence_score": 0.95},
                    {"content": "How many laps the vehicle could drive to get minimal point in the Obstacle Challenge", "confidence_score": 0.40},
                    {"content": "Asking about number of laps are in the Obstacle Challenge", "confidence_score": 0.05}
                ],
                "chosen_interpretation": {
                    "content": "Asking about number of laps are in the Open Challenge?",
                    "confidence_score": 0.95
                },
                "reformulation_request": None
            }
        }

class FAQResponse:
    """Structured response format for FAQ entries with reasoning and language support."""
    
    chain_of_thoughts: Annotated[
        str,
        "Chain of thoughts with reasoning why adjustments to the question and answer are needed."
    ]
    
    title: Annotated[
        str,
        "A title for the FAQ section of the rules"
    ]
    
    user_input: Annotated[
        str,
        "The original input from the user"
    ]
    
    question: Annotated[
        str,
        "Question original or adjusted if the need for adjustments was discovered"
    ]
    
    answer: Annotated[
        str,
        "Answer original or adjusted if the need for adjustments was discovered. In English."
    ]
    
    localized_answer: Annotated[
        Optional[str],
        "Answer translated to the language of the user. Only included if the answer is not in the user's language."
    ] = None

# class FAQPydanticResponse(BaseModel):
#     """Structured response format for FAQ entries with reasoning and language support."""
    
#     chain_of_thoughts: str = Field(
#         description="Chain of thoughts with reasoning why adjustments to the question and answer are needed."
#     )
    
#     title: str = Field(
#         description="A title for the FAQ section of the rules"
#     )
    
#     user_input: str = Field(
#         description="The original input from the user"
#     )
    
#     question: str = Field(
#         description="Question original or adjusted if the need for adjustments was discovered"
#     )
    
#     answer: str = Field(
#         description="Answer original or adjusted if the need for adjustments was discovered. In English."
#     )
    
#     localized_answer: Optional[str] = Field(
#         None,
#         description="Answer translated to the language of the user. Only included if the answer is not in the user's language."
#     )
