from data_structures.responses.finalizer import FinalizerResponse
from . import utils
import xml.etree.ElementTree as ET

def parse(xml_string: str) -> FinalizerResponse:
    """Convert XML response to FinalizerResponse object
    
    Args:
        xml_string (str): XML string containing the finalizer response
        
    Returns:
        FinalizerResponse: Parsed response object
        
    Raises:
        ValueError: If XML is invalid or required elements are missing
    """
    try:
        # Parse XML string
        root = ET.fromstring(utils.trim_xml_response(xml_string, "faq"))
        
        # Extract required fields
        chain_of_thoughts = utils.get_element_text(root, 'chain_of_thoughts') 
        title = utils.get_element_text(root, 'title')
        user_input = utils.get_element_text(root, 'user_input')
        question = utils.get_element_text(root, 'question')
        answer = utils.get_element_text(root, 'answer')
        localized_answer = utils.get_element_text(root, 'localized_answer', required=False)
        
        return FinalizerResponse(
            chain_of_thought=chain_of_thoughts,
            title=title,
            user_input=user_input,
            question=question,
            answer=answer,
            localized_answer=localized_answer
        )
            
    except ET.ParseError as e:
        raise ValueError(f"Invalid XML: {str(e)}")
