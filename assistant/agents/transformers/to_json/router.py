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
        
        # Initialize result dictionary
        result = {
            "chain_of_thought": "",
            "sections": []
        }
        
        # Extract chain of thoughts
        chain_of_thoughts = root.find('chain_of_thoughts')
        if chain_of_thoughts is not None:
            result["chain_of_thought"] = chain_of_thoughts.text.strip()
        
        # Extract sections
        sections = root.find('sections')
        if sections is not None:
            # Get all filename elements and extract their text
            result["sections"] = [
                filename.text.strip()
                for filename in sections.findall('filename')
                if filename.text is not None and filename.text.strip()  # Skip empty filenames
            ]
        
        # Create and return RouterResponse object
        return RouterResponse(
            chain_of_thought=result["chain_of_thought"],
            sections=result["sections"]
        )
        
    except ET.ParseError:
        raise ValueError("Invalid XML response from model")

