
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
        
        return BaseAssistantResponse(
            question=utils.get_element_text(root, 'question'),
            chain_of_thought=utils.get_element_text(root, 'chain_of_thoughts'),
            applicable=utils.get_element_bool(root, 'applicable'),
            answer=utils.get_element_text(root, 'answer')
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
        
        return VerificationAssistantResponse(
            chain_of_thought=utils.get_element_text(root, 'chain_of_thoughts'),
            adjustments_required=utils.get_element_bool(root, 'adjustments_required'),
            answer=utils.get_element_text(root, 'answer', empty_ok=True)
        )
            
    except ET.ParseError as e:
        raise ValueError(f"Invalid XML: {str(e)}")
