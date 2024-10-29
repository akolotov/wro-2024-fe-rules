from pydantic import Field
from .base import BaseResponse

class BaseAssistantResponse(BaseResponse):
    """
    Pydantic model for the assistant agent's response structure.
    Includes validation, documentation, and examples.
    """
    question: str = Field(
        ...,
        description="The user's question",
        min_length=1
    )
    
    answer: str = Field(
        ...,
        description="Your answer.",
        min_length=1
    )

# Class below describes the response structure of the assistant agent:
# <brainstorm>
#   <question>The interpretation of the user's question with the highest rank</question>
#   <chain_of_thoughts>Chain of thoughts and reasoning to conclude the answer.</chain_of_thoughts>
#   <answer>Your answer</answer>
# </brainstorm>
class FirstAssistantResponse(BaseAssistantResponse):
    # override the base class field to redefine the description
    question: str = Field(
        ...,
        description="The interpretation of the user's question with the highest rank",
        min_length=1
    )

    # override the base class field to redefine the description
    chain_of_thought: str = Field(
        ...,
        description="Chain of thoughts and reasoning to conclude the answer.",
        min_length=1
    )
    
    class Config:
        json_schema_extra = {
            "example": {
                "question": "How many laps are required in the Open Challenge?",
                "chain_of_thought": "1. Analyzed question context\n2. Reviewed relevant rules\n3. Formulated response",
                "answer": "According to section 3.1 of the rules, teams must complete 3 laps in the Open Challenge."
            }
        }

# Class below describes the response structure of the assistant agent:
# <brainstorm>
#   <question>The adjusted version of the user's question if new adjustments were introduced or the unmodified version from the previous experts.</question>
#   <chain_of_thoughts>Chain of thoughts and reasoning to conclude the required adjustments in the response from the previous experts.</chain_of_thoughts>
#   <answer>Your answer.</answer>
# <brainstorm>
class SubsequentAssistantResponse(BaseAssistantResponse):
    # override the base class field to redefine the description
    question: str = Field(
        ...,
        description="The adjusted version of the user's question if new adjustments were introduced or the unmodified version from the previous experts",
        min_length=1
    )

    # override the base class field to redefine the description
    chain_of_thought: str = Field(
        ...,
        description="Chain of thoughts and reasoning to conclude the required adjustments in the response from the previous experts",
        min_length=1
    )
    
    class Config:
        json_schema_extra = {
            "example": {
                "question": "How many laps are required in the Open Challenge?",
                "chain_of_thought": "1. Reviewed previous expert interpretation\n2. Analyzed response accuracy\n3. Determined no adjustments needed",
                "answer": "According to section 3.1 of the rules, teams must complete 3 laps in the Open Challenge."
            }
        }

# Class below describes the response structure of the assistant agent verification:
# <brainstorm>
#   <chain_of_thoughts>Chain of thoughts and reasoning to conclude the about required adjustments</chain_of_thoughts>
#   <answer>Answer original or adjusted if the need for adjustments was discovered.</answer>
# <brainstorm>
class VerificationAssistantResponse(BaseResponse):
    # override the base class field to redefine the description
    chain_of_thought: str = Field(
        ...,
        description="Chain of thoughts and reasoning to conclude the about required adjustments.",
        min_length=1
    )

    answer: str = Field(
        ...,
        description="Answer original or adjusted if the need for adjustments was discovered.",
        min_length=1
    )

    class Config:
        json_schema_extra = {
            "example": {
                "chain_of_thought": "1. Reviewed previous expert interpretation\n2. Analyzed response accuracy\n3. Determined no adjustments needed",
                "answer": "According to section 3.1 of the rules, teams must complete 3 laps in the Open Challenge."
            }
        }
