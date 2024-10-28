def trim_xml_response(xml_string: str, root_tag: str) -> str:
    start_index = xml_string.find(f'<{root_tag}>')
    end_index = xml_string.rfind(f'</{root_tag}>') + len(f'</{root_tag}>')
    if start_index != -1 and end_index != -1:
        return xml_string[start_index:end_index]
    return xml_string
