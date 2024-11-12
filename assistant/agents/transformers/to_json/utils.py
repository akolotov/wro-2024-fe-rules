import xml.etree.ElementTree as ET

def trim_xml_response(xml_string: str, root_tag: str) -> str:
    start_index = xml_string.find(f'<{root_tag}>')
    end_index = xml_string.rfind(f'</{root_tag}>') + len(f'</{root_tag}>')
    if start_index != -1 and end_index != -1:
        return xml_string[start_index:end_index]
    return xml_string

def escape_xml_characters(text: str) -> str:
    result = text.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot;').replace("'", '&apos;')
    print(f"Escaped XML string: {result}")
    return result

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

def get_attribute(element: ET.Element, attribute: str, required: bool = True, empty_ok: bool = False) -> str:
    value = element.get(attribute)
    if value is None:
        if required:
            raise ValueError(f"Missing {attribute} XML attribute")
        return ""
    if value == "":
        if not empty_ok:
            raise ValueError(f"Empty {attribute} XML attribute")
        return ""
    return value
