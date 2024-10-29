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
        
        # Initialize result dictionary
        result = {
            "chain_of_thoughts": "",
            "originalUserQuestion": "",
            "interpretations": None,
            "chosenInterpretation": None,
            "reformulationRequest": None
        }
        
        # Extract data from XML
        chain_of_thought = root.find('chain_of_thoughts')
        if chain_of_thought is not None:
            result["chain_of_thoughts"] = chain_of_thought.text.strip()
            
        original_question = root.find('originalUserQuestion')
        if original_question is not None:
            result["originalUserQuestion"] = original_question.text.strip()
            
        interpretations = root.find('interpretations')
        if interpretations is not None:
            result["interpretations"] = [
                UserRequestInterpretation(content=interp.text.strip())
                for interp in interpretations.findall('interpretation')
            ]
            
        chosen_interpretation = root.find('chosenInterpretation')
        if chosen_interpretation is not None:
            result["chosenInterpretation"] = UserRequestInterpretation(content=chosen_interpretation.text.strip())
            
        # If it's a reformulation request
        reformulation_request = root.find('reformulationRequest')
        if reformulation_request is not None:
            result["reformulationRequest"] = reformulation_request.text.strip()
        
        return EntryResponse(
            chain_of_thought=result["chain_of_thoughts"],
            original_user_question=result["originalUserQuestion"],
            interpretations=result["interpretations"],
            chosen_interpretation=result["chosenInterpretation"],
            reformulation_request=result["reformulationRequest"]
        )
    
    except ET.ParseError as e:
        raise ValueError(f"Invalid XML: {str(e)}")
