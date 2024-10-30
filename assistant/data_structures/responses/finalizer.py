from .base import BaseResponse
from pydantic import Field
from typing import Optional

# Class below describes the response structure of the finalizer agent:
# <faq>
#   <chain_of_thoughts>Chain of thoughts with reasoning why adjustments to the question and answer are needed.</chain_of_thoughts>
#   <title>A title for the FAQ section of the rules</title>
#   <user_input>The original input from the user.</user_input>
#   <question>Question original or adjusted if the need for adjustments was discovered.</question>
#   <answer>Answer original or adjusted if the need for adjustments was discovered. In English.</answer>
#   [Include only if the answer is not in the language of the user:
#   <localized_answer>Answer translated to the language of the user.</localized_answer>
#   ]
# </faq>
class FinalizerResponse(BaseResponse):
    chain_of_thought: str = Field(
        ...,
        description="Chain of thoughts with reasoning why adjustments to the question and answer are needed."
    )
    
    title: str = Field(
        ...,
        description="A title for the FAQ section of the rules."
    )
    
    user_input: str = Field(
        ...,
        description="The original input from the user."
    )
    
    question: str = Field(
        ...,
        description="Question original or adjusted if the need for adjustments was discovered."
    )
    
    answer: str = Field(
        ...,
        description="Answer original or adjusted if the need for adjustments was discovered. In English."
    )
    
    localized_answer: Optional[str] = Field(
        None,
        description="Answer translated to the language of the user. Only included if the answer is not in the user's language."
    )
