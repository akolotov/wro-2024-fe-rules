import xml.etree.ElementTree as ET

def to_string_without_declaration(element: ET.Element) -> str:
    xml_str = ET.tostring(element, encoding='unicode', method='xml')
    
    # Add manual indentation
    from xml.dom import minidom
    # Parse without declaration and re-indent
    xml_str = minidom.parseString(xml_str).documentElement.toprettyxml(indent="  ")

    return xml_str