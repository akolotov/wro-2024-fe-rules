from typing import List
from pydantic import Field, field_validator
from .base import BaseResponse

# Class below describe the response structure of the router agent:
# <brainstorm>
#   <chain_of_thoughts>The chain of thoughts and reasoning why the corresponding sections of the rules are going to be chosen</chain_of_thoughts>
#   <sections>
#     <filename>The request must first be forwarded to the expert responsible for this section.</filename>
#     <filename>(Optional) The request must be forwarded to the expert responsible for this section in the second turn.</filename>
#     <filename>(Optional) The request must be forwarded to the expert responsible for this section in the third turn.</filename>
#     <filename>(Optional) The request must be forwarded to the expert responsible for this section in the fourth turn.</filename>
#     <filename>(Optional) The request must be forwarded to the expert responsible for this section in the fifth turn.</filename>
#   </sections>
# </brainstorm>

class RouterResponse(BaseResponse):
    """
    Pydantic model for the router agent's response structure.
    Includes validation, documentation, and examples.
    """
    # override the base class field to redefine the description
    chain_of_thought: str = Field(
        ...,
        description="The chain of thoughts and reasoning why the corresponding sections of the rules are going to be chosen.",
        min_length=1
    )

    sections: List[str] = Field(
        ...,
        description="List of filenames representing sections to forward the request to, in order of processing.",
        min_items=1,
        max_items=5
    )

    @field_validator('sections')
    def validate_sections(cls, v):
        if not 1 <= len(v) <= 5:
            raise ValueError("Must have between 1 and 5 sections")
        return v

    class Config:
        json_schema_extra = {
            "example": {
                "chain_of_thought": "1. Analyzed the question content\n2. Identified relevant rule sections\n3. Determined processing order",
                "sections": [
                    "01-registration.md",
                    "02-qualification.md",
                    "03-finals.md"
                ]
            }
        }
