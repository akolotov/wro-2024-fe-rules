from data_structures.inputs.common import UserRequest
import xml.etree.ElementTree as ET
from .utils import to_string_without_declaration

def format_input(user_request: UserRequest) -> str:
    root = ET.Element("user_question")
    root.text = user_request.request

    return to_string_without_declaration(root)