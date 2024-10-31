from data_structures.responses.assistant import (
    BaseAssistantResponse, 
    VerificationAssistantResponse,
    BaseRule,
    SubsequentResponseRule
)

from . import utils
import xml.etree.ElementTree as ET
from typing import Optional, List

def _parse_relevant_rule(rule_element: ET.Element) -> BaseRule:
    """Parse a single rule XML element into a BaseRule object
    
    Args:
        rule_element (ET.Element): XML element containing rule data
        
    Returns:
        BaseRule: Parsed rule object
        
    Raises:
        ValueError: If required attributes or elements are missing
    """
    return BaseRule(
        section=utils.get_attribute(rule_element, 'section'),
        id=utils.get_attribute(rule_element, 'id'),
        content=utils.get_element_text(rule_element, 'content'),
        explanation=utils.get_element_text(rule_element, 'explanation')
    )

def _parse_relevant_rules(rules_element: Optional[ET.Element]) -> Optional[List[BaseRule]]:
    """Parse the relevant_rules XML element into a list of BaseRule objects
    
    Args:
        rules_element (Optional[ET.Element]): XML element containing rules
        
    Returns:
        Optional[List[BaseRule]]: List of parsed rules or None if no rules element
    """
    if rules_element is None:
        return None
        
    rules = []
    for rule in rules_element.findall('rule'):
        rules.append(_parse_relevant_rule(rule))
    
    return rules if rules else None

def parse_response(xml_string: str) -> BaseAssistantResponse:
    """Convert XML response to BaseAssistantResponse object
    
    Args:
        xml_string (str): XML string containing the assistant response
        
    Returns:
        BaseAssistantResponse: Parsed response object
        
    Raises:
        ValueError: If XML is invalid or required elements are missing
    """
    try:
        # Parse XML string
        root = ET.fromstring(utils.trim_xml_response(xml_string, "brainstorm"))

        return BaseAssistantResponse(
            question=utils.get_element_text(root, 'question'),
            relevant_rules=_parse_relevant_rules(root.find('relevant_rules')),
            chain_of_thought=utils.get_element_text(root, 'chain_of_thoughts'),
            applicable=utils.get_element_bool(root, 'applicable'),
            answer=utils.get_element_text(root, 'answer'),
        )
            
    except ET.ParseError as e:
        raise ValueError(f"Invalid XML: {str(e)}")

def parse_verification(xml_string: str) -> VerificationAssistantResponse:
    """Convert XML response to VerificationAssistantResponse object
    
    Args:
        xml_string (str): XML string containing a verification of the assistant response
        
    Returns:
        VerificationAssistantResponse: Parsed response object
        
    Raises:
        ValueError: If XML is invalid or required elements are missing
    """
    try:
        # Parse XML string
        root = ET.fromstring(utils.trim_xml_response(xml_string, "brainstorm"))

        relevant_rules = _parse_relevant_rules(root.find('relevant_rules'))
        if relevant_rules is not None:
            relevant_rules = [SubsequentResponseRule(
                section=rule.section,
                id=rule.id,
                content=rule.content,
                explanation=rule.explanation
            ) for rule in relevant_rules]
        
        return VerificationAssistantResponse(
            relevant_rules=relevant_rules,
            chain_of_thought=utils.get_element_text(root, 'chain_of_thoughts'),
            adjustments_required=utils.get_element_bool(root, 'adjustments_required'),
            answer=utils.get_element_text(root, 'answer', empty_ok=True)
        )
            
    except ET.ParseError as e:
        raise ValueError(f"Invalid XML: {str(e)}")
