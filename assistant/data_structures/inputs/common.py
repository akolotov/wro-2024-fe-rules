from pydantic import BaseModel, Field

class UserRequest(BaseModel):
    """
    Pydantic model for the user's question.
    """
    request: str = Field(
        ...,
        description="The user's question",
        example="How many laps are in the Open Challenge?"
    )