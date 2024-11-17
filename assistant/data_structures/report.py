from typing import TypeVar, Generic, Optional
from pydantic import BaseModel, Field
from .responses.base import BaseResponse
from .responses.assistant import VerificationAssistantResponse, BaseAssistantResponse
from .responses.faq_filter import FAQFilterResponse

T = TypeVar('T', bound=BaseResponse)
A = TypeVar('A', bound=BaseAssistantResponse)

class Metadata(BaseModel):
    prompt_token_count: int = Field(..., description="Number of tokens in the prompt")
    candidates_token_count: int = Field(..., description="Number of tokens in the model's response")
    total_token_count: int = Field(..., description="Sum of prompt and candidates token counts")
    duration: float = Field(..., description="Duration of the LLM call in seconds")

class Report(BaseModel, Generic[T]):
    metadata: Metadata = Field(..., description="Metadata about the LLM call")
    response: T = Field(..., description="The response from the LLM")

class CombinedAssistantReport(BaseModel, Generic[A]):
    proposal: Report[A]
    verification: Optional[Report[VerificationAssistantResponse]] = None

class FAQFilterReport(BaseModel):
    handler: Report[FAQFilterResponse]
    verification: Report[FAQFilterResponse]
