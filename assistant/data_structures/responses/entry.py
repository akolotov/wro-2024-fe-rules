from typing import Optional, List
from pydantic import BaseModel, Field, field_validator
from .base import BaseResponse

# Classes below describe the response structure of the entrypoint agent:
# <response>
#     <chain_of_thoughts>
#         Your reasoning process  
#     </chain_of_thoughts>  
#     <originalUserQuestion>
#         The original question text  
#     </originalUserQuestion>  
#     <reformulationRequest>
#         The reformulation request text in the lenguage of the original question
#     </reformulationRequest>  
# </response>
# 
# OR
#
# <response>
#     <chain_of_thoughts>
#         Your reasoning process  
#     </chain_of_thoughts>
#     <originalUserQuestion>
#         The original question text  
#     </originalUserQuestion>  
#     <interpretations>
#         <interpretation index="1">  
#             First of the three interpretations of the question  
#         </interpretation>
#         <interpretation index="2">  
#             Second of the three interpretations of the question  
#         </interpretation>
#         <interpretation index="3">  
#             Third of the three interpretations of the question  
#         </interpretation>
#     </interpretations>
#     <chosenInterpretation>
#         The most probable interpretation of the question  
#     </chosenInterpretation>
# </response>
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

class EntryResponse(BaseResponse):
    """
    Pydantic model for the complete response structure.
    Includes validation, documentation, and examples.
    """
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