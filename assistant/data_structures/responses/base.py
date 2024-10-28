from pydantic import BaseModel, Field

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