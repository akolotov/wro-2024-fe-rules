from data_structures.responses.entry import EntryResponse, UserRequestInterpretation
from . import utils
import xml.etree.ElementTree as ET

def parse(xml_string: str) -> EntryResponse:
    """Convert XML response to EntryResponse object
    
    Args:
        xml_string (str): XML string containing the entrypoint response
        
    Returns:
        EntryResponse: Parsed response object
        
    Raises:
        ValueError: If XML is invalid or required elements are missing
    """
    try:
        # Parse XML string
        root = ET.fromstring(utils.trim_xml_response(xml_string, "response"))
        
        interpretations = []
        
        # Extract data from XML
        interpretations_element = root.find('interpretations')
        if interpretations_element is not None:
            interpretations = [
                UserRequestInterpretation(content=interp.text.strip())
                for interp in interpretations_element.findall('interpretation')
            ]
            
        chosen_interpretation = UserRequestInterpretation(
            content=utils.get_element_text(root, 'chosenInterpretation')
        )
                    
        return EntryResponse(
            chain_of_thought=utils.get_element_text(root, 'chain_of_thoughts'),
            original_user_question=utils.get_element_text(root, 'originalUserQuestion'),
            interpretations=interpretations,
            chosen_interpretation=chosen_interpretation,
            reformulation_request=utils.get_element_text(root, 'reformulationRequest', required=False)
        )
    
    except ET.ParseError as e:
        raise ValueError(f"Invalid XML: {str(e)}")
