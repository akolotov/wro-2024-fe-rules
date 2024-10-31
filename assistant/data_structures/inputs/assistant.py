from pydantic import BaseModel, Field
from typing import Optional, List
from data_structures.responses.assistant import BaseRule

# Class below describes the response structure of the router agent:
# <brainstorm>
#   <original_question>...</original_question>
#   <adjusted_question>...</adjusted_question>
#   <relevant_rules>
#     <rule section="..." id="...">
#         <content>...</content>
#         <explanation>...</explanation>
#     </rule>
#   </relevant_rules>
#   <response>...</response>
# </brainstorm>
class AssistantRequest(BaseModel):
    original_question: str = Field(
        ..., 
        description="The original user's question.",
        example="How many laps are in the Open Challenge?"
    )

    adjusted_question: Optional[str] = Field(
        None, 
        description="The adjusted version of the user's question if new adjustments were introduced or the unmodified version from the previous experts.",
        example="Could you clarify how many laps competitors must complete in the Open Challenge event?"
    )

    relevant_rules: Optional[List[BaseRule]] = Field(
        None,
        description="The rules that were relevant to the user's question."
    )
    
    response: Optional[str] = Field(
        None, 
        description="The answer to the user's question after a series of adjustments by previous experts.",
        example="According to the rules, competitors must complete 3 laps in the Open Challenge."
    )