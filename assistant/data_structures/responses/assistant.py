from pydantic import Field, BaseModel
from .base import BaseResponse

class BaseRule(BaseModel):
    """
    Pydantic model representing a single rule with its metadata and explanation.
    """
    section: str = Field(
        ..., 
        description="Section filename containing the rule",
        min_length=1
    )
    
    id: str = Field(
        ...,
        description="Rule identifier",
    )
    
    content: str = Field(
        ...,
        description="Full text content of the rule",
        min_length=1
    )
    
    explanation: str = Field(
        ...,
        description="1-3 sentences of explanation how the rule is helpful.",
        min_length=1
    )

class FirstResponseRule(BaseRule):
    # override the base class field to redefine the description
    explanation: str = Field(
        ...,
        description="1-3 sentences of explanation how the rule is helpful in answering on the question. The explanation must be self-sufficient to be used without knowing the previous context of the section.",
        min_length=1
    )

class SubsequentResponseRule(BaseRule):
    # override the base class field to redefine the description
    explanation: str = Field(
        ...,
        description="1-3 sentences of explanation how the rule is helpful to the adjustments action. The explanation must be self-sufficient to be used without knowing the previous context of the section.",
        min_length=1
    )

class BaseAssistantResponse(BaseResponse):
    """
    Pydantic model for the assistant agent's response structure.
    Includes validation, documentation, and examples.
    """
    relevant_rules: list[BaseRule] | None = Field(
        None,
        description="The list of all the rules items that are relevant to answer the question",
    )

    question: str = Field(
        ...,
        description="The user's question",
        min_length=1
    )

    applicable: bool = Field(
        ...,
        description="True if the question is applicable, False otherwise",
    )
    
    answer: str = Field(
        ...,
        description="Your answer.",
    )

# Class below describes the response structure of the assistant agent:
# <brainstorm>
#   <question>The interpretation of the user's question with the highest rank</question>
#   <relevant_rules>
#     <!-- The list of all the rules items that are relevant to answer the question -->
#     <rule section="section filename" id="A1.2">
#         <content>Text of rule A1.2</content>
#         <explanation>1-3 sentences of explanation how the rule is helpful in answering on the question. The explanation must be self-sufficient to be used without knowing the previous context of the section.</explanation>
#     </rule>
#   </relevant_rules>
#   <chain_of_thoughts>Chain of thoughts and reasoning to conclude the answer.</chain_of_thoughts>
#   <applicable>True if the question is applicable, False otherwise</applicable>
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
    relevant_rules: list[FirstResponseRule] | None = Field(
        None,
        description="The list of all the rules items that are relevant to answer the question.",
    )

    # override the base class field to redefine the description
    chain_of_thought: str = Field(
        ...,
        description="Chain of thoughts and reasoning to conclude the answer.",
        min_length=1
    )

    applicable: bool = Field(
        ...,
        description="True if the question is applicable, False otherwise",
    )
    
    class Config:
        json_schema_extra = {
            "example": {
                "question": "How many laps are required in the Open Challenge?",
                "relevant_rules": [
                    {
                        "section": "Appendix-A.md",
                        "id": "A1.2",
                        "content": "Text of rule A1.2",
                        "explanation": "1-3 sentences of explanation how the rule is helpful in answering on the question."
                    }
                ],
                "chain_of_thought": "1. Analyzed question context\n2. Reviewed relevant rules\n3. Formulated response",
                "applicable": True,
                "answer": "According to section 3.1 of the rules, teams must complete 3 laps in the Open Challenge."
            }
        }

# Class below describes the response structure of the assistant agent:
# <brainstorm>
#   <question>The adjusted version of the user's question if new adjustments were introduced or the unmodified version from the previous experts.</question>
#   <relevant_rules>
#     <!-- The list of the rules items that are relevant to the adjustments action. It must be combined with the list from the previous experts. -->
#     <rule section="section filename" id="A1.2">
#         <content>Text of rule A1.2</content>
#         <explanation>1-3 sentences of explanation how the rule is helpful to the adjustments action. The explanation must be self-sufficient to be used without knowing the previous context of the section.</explanation>
#     </rule>
#   </relevant_rules>
#   <chain_of_thoughts>Chain of thoughts and reasoning to conclude the required adjustments in the response from the previous experts.</chain_of_thoughts>
#   <applicable>True if the question is applicable, False otherwise</applicable>
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
    relevant_rules: list[SubsequentResponseRule] | None = Field(
        None,
        description="The list of the rules items that are relevant to the adjustments action. It must be combined with the list from the previous experts.",
    )

    # override the base class field to redefine the description
    chain_of_thought: str = Field(
        ...,
        description="Chain of thoughts and reasoning to conclude the required adjustments in the response from the previous experts",
        min_length=1
    )

    applicable: bool = Field(
        ...,
        description="True if the question is applicable, False otherwise",
    )
    
    class Config:
        json_schema_extra = {
            "example": {
                "question": "How many laps are required in the Open Challenge?",
                "relevant_rules": [
                    {
                        "section": "Appendix-A.md",
                        "id": "A1.2",
                        "content": "Text of rule A1.2",
                        "explanation": "1-3 sentences of explanation how the rule is helpful in answering on the question."
                    }
                ],
                "chain_of_thought": "1. Reviewed previous expert interpretation\n2. Analyzed response accuracy\n3. Determined no adjustments needed",
                "applicable": True,
                "answer": "According to section 3.1 of the rules, teams must complete 3 laps in the Open Challenge."
            }
        }

# Class below describes the response structure of the assistant agent verification:
# <brainstorm>
#   <relevant_rules>
#     <!-- The list of the rules items that are relevant to the adjustments action. It must be combined with the list from the previous step. -->
#     <rule section="section filename" id="A1.2">
#         <content>Text of rule A1.2</content>
#         <explanation>1-3 sentences of explanation how the rule is helpful to the adjustments action. The explanation must be self-sufficient to be used without knowing the previous context of the section.</explanation>
#     </rule>
#   </relevant_rules>
#   <chain_of_thoughts>Chain of thoughts and reasoning to conclude the about required adjustments</chain_of_thoughts>
#   <adjustments_required>True if answer needs to be adjusted, False otherwise</adjustments_required>
#   <answer>Adjusted answer if the need for adjustments was discovered.</answer>
# </brainstorm>
class VerificationAssistantResponse(BaseResponse):
    # override the base class field to redefine the description
    relevant_rules: list[SubsequentResponseRule] | None = Field(
        None,
        description="The list of the rules items that are relevant to the adjustments action. It must be combined with the list from the previous step.",
    )

    # override the base class field to redefine the description
    chain_of_thought: str = Field(
        ...,
        description="Chain of thoughts and reasoning to conclude the about required adjustments.",
        min_length=1
    )

    adjustments_required: bool = Field(
        ...,
        description="True if answer needs to be adjusted, False otherwise",
    )

    answer: str = Field(
        ...,
        description="Adjusted answer if the need for adjustments was discovered.",
    )

    class Config:
        json_schema_extra = {
            "example": {
                "relevant_rules": [
                    {
                        "section": "Appendix-A.md",
                        "id": "A1.2",
                        "content": "Text of rule A1.2",
                        "explanation": "1-3 sentences of explanation how the rule is helpful in answering on the question."
                    }
                ],
                "chain_of_thought": "1. Reviewed previous expert interpretation\n2. Analyzed response accuracy\n3. Determined no adjustments needed",
                "adjustments_required": True,
                "answer": "According to section 3.1 of the rules, teams must complete 3 laps in the Open Challenge."
            }
        }
