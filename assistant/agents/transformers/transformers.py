from responses import EntryResponse, UserRequestInterpretation
import xml.etree.ElementTree as ET
from typing import Dict

def trim_xml_response(xml_string: str, root_tag: str) -> str:
    start_index = xml_string.find(f'<{root_tag}>')
    end_index = xml_string.rfind(f'</{root_tag}>') + len(f'</{root_tag}>')
    if start_index != -1 and end_index != -1:
        return xml_string[start_index:end_index]
    return xml_string

def entry_response_xml_to_json(xml_string: str) -> EntryResponse:
    """Convert XML response to JSON format"""
    try:
        # Parse XML string
        root = ET.fromstring(trim_xml_response(xml_string, "response"))
        
        # Initialize result dictionary
        result = {
            "chainOfThought": "",
            "originalUserQuestion": "",
            "interpretations": None,
            "chosenInterpretation": None,
            "reformulationRequest": None
        }
        
        # Extract data from XML
        chain_of_thought = root.find('chainOfThought')
        if chain_of_thought is not None:
            result["chainOfThought"] = chain_of_thought.text.strip()
            
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
            chain_of_thought=result["chainOfThought"],
            original_user_question=result["originalUserQuestion"],
            interpretations=result["interpretations"],
            chosen_interpretation=result["chosenInterpretation"],
            reformulation_request=result["reformulationRequest"]
        )
    except ET.ParseError:
        raise ValueError("Invalid XML response from model")
