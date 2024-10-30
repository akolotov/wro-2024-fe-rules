from data_structures.responses.router import RouterResponse
from . import utils
import xml.etree.ElementTree as ET

def parse(xml_string: str) -> RouterResponse:
    
    """Convert XML response to RouterResponse object
    
    Args:
        xml_string (str): XML string containing the router response
        
    Returns:
        RouterResponse: Parsed response object
        
    Raises:
        ValueError: If XML is invalid or required elements are missing
    """
    try:
        # Parse XML string - the root tag is 'brainstorm' for router responses
        root = ET.fromstring(utils.trim_xml_response(xml_string, "brainstorm"))

        sections = []
                
        # Extract sections
        sections_element = root.find('sections')
        if sections_element is not None:
            # Get all filename elements and extract their text
            sections = [
                filename.text.strip()
                for filename in sections_element.findall('filename')
                if filename.text is not None and filename.text.strip()  # Skip empty filenames
            ]
        
        # Create and return RouterResponse object
        return RouterResponse(
            chain_of_thought=utils.get_element_text(root, 'chain_of_thoughts'),
            sections=sections
        )
        
    except ET.ParseError as e:
        raise ValueError(f"Invalid XML: {str(e)}")
