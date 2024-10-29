import xml.etree.ElementTree as ET
from data_structures.inputs.assistant import AssistantRequest
from .utils import to_string_without_declaration

def format_input(user_request: AssistantRequest) -> str:
    root = ET.Element("brainstorm")
    
    # Add original question
    original_question = ET.SubElement(root, "original_question")
    original_question.text = user_request.original_question
    
    # Add adjusted question if present
    if user_request.adjusted_question and user_request.response:
        adjusted_question = ET.SubElement(root, "adjusted_question")
        adjusted_question.text = user_request.adjusted_question
        
        response = ET.SubElement(root, "response")
        response.text = user_request.response
        
    return to_string_without_declaration(root)
