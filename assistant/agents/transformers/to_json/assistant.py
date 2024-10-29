
from data_structures.responses.assistant import BaseAssistantResponse, VerificationAssistantResponse
from . import utils
import xml.etree.ElementTree as ET

def parse_response(xml_string: str) -> BaseAssistantResponse:
    """Convert XML response to BaseAssistantResponse object
    
    Args:
        xml_string (str): XML string containing the assistant response
        
    Returns:
        BaseAssistantResponse: Parsed response object
        
    Raises:
        ValueError: If XML is invalid or required elements are missing
    """
    try:
        # Parse XML string
        root = ET.fromstring(utils.trim_xml_response(xml_string, "brainstorm"))
        
        # Extract required fields
        question = root.find('question')
        chain_of_thoughts = root.find('chain_of_thoughts') 
        answer = root.find('answer')
        
        if question is None:
            print(f"Question: {question}")
            raise ValueError("Missing question XML element")
        if chain_of_thoughts is None:
            print(f"Chain of thoughts: {chain_of_thoughts}")
            raise ValueError("Missing chain of thoughts XML element")
        if answer is None:
            print(f"Answer: {answer}")
            raise ValueError("Missing answer XML element")
            
        return BaseAssistantResponse(
            question=question.text.strip(),
            chain_of_thought=chain_of_thoughts.text.strip(),
            answer=answer.text.strip()
        )
            
    except ET.ParseError as e:
        raise ValueError(f"Invalid XML: {str(e)}")

def parse_verification(xml_string: str) -> VerificationAssistantResponse:
    """Convert XML response to VerificationAssistantResponse object
    
    Args:
        xml_string (str): XML string containing a verification of the assistant response
        
    Returns:
        VerificationAssistantResponse: Parsed response object
        
    Raises:
        ValueError: If XML is invalid or required elements are missing
    """
    try:
        # Parse XML string
        root = ET.fromstring(utils.trim_xml_response(xml_string, "brainstorm"))
        
        # Extract required fields
        chain_of_thoughts = root.find('chain_of_thoughts') 
        answer = root.find('answer')
        
        if chain_of_thoughts is None:
            print(f"Chain of thoughts: {chain_of_thoughts}")
            raise ValueError("Missing chain of thoughts XML element")
        if answer is None:
            print(f"Answer: {answer}")
            raise ValueError("Missing answer XML element")
            
        return VerificationAssistantResponse(
            chain_of_thought=chain_of_thoughts.text.strip(),
            answer=answer.text.strip()
        )
            
    except ET.ParseError as e:
        raise ValueError(f"Invalid XML: {str(e)}")
