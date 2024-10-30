import xml.etree.ElementTree as ET

def trim_xml_response(xml_string: str, root_tag: str) -> str:
    start_index = xml_string.find(f'<{root_tag}>')
    end_index = xml_string.rfind(f'</{root_tag}>') + len(f'</{root_tag}>')
    if start_index != -1 and end_index != -1:
        return xml_string[start_index:end_index]
    return xml_string


def get_element_text(root: ET.Element, element: str, required: bool = True, empty_ok: bool = False) -> str:
    element = root.find(element)
    if element is None:
        if required:
            raise ValueError(f"Missing {element} XML element")
        return None
    text = element.text
    if text is None:
        if not empty_ok:
            raise ValueError(f"Empty {element} XML element")
        return ""
    return text.strip()

def get_element_bool(root: ET.Element, element: str, required: bool = True) -> bool:
    element = root.find(element)
    if element is None:
        if required:
            raise ValueError(f"Missing {element} XML element")
        return None
    text = element.text
    if text is None:
        raise ValueError(f"Empty {element} XML element")
    return text.strip().lower() == 'true'