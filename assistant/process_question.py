import json
from llms import initialize as initialize_llm
import argparse
from agents import EntryAgent, RouterAgent, AssistantAgent, FinalizerAgent
from data_structures.inputs.assistant import AssistantRequest
from data_structures.responses.assistant import BaseRule

def process_question(input_file_path: str, output_file_path: str = "out.json"):
    with open(input_file_path, 'r', encoding='utf-8') as file:
        input_data = json.load(file)
        user_request = input_data.get('question')

    print(f"Involving the secretary")
    entry_agent = EntryAgent()
    entry_report = entry_agent.process_question(user_request)
    workflow = {
        "entrypoint": entry_report.model_dump()
    }

    if entry_report.response.reformulation_request is None:
        print(f"Involving the router")
        router_agent = RouterAgent()
        router_report = router_agent.process_question(entry_report.response.chosen_interpretation.content)
        workflow["router"] = router_report.model_dump()

        next_request = AssistantRequest(original_question=entry_report.response.chosen_interpretation.content)

        relevant_rules_accumulator = {}

        for section in router_report.response.sections:
            print(f"Involving assistant for {section}")
            assistant_agent = AssistantAgent(section)

            assistant_report = assistant_agent.brainstorm_contribution(next_request)

            workflow[section] = assistant_report.model_dump()

            if assistant_report.verification.response.relevant_rules:
                for rule in assistant_report.verification.response.relevant_rules:
                    if rule.section not in relevant_rules_accumulator:
                        relevant_rules_accumulator[rule.section] = {}
                    if rule.id not in relevant_rules_accumulator[rule.section]:
                        relevant_rules_accumulator[rule.section][rule.id] = {}
                    relevant_rules_accumulator[rule.section][rule.id]["content"] = rule.content
                    relevant_rules_accumulator[rule.section][rule.id]["explanation"] = rule.explanation
            else:
                if assistant_report.proposal.response.relevant_rules:
                    for rule in assistant_report.proposal.response.relevant_rules:
                        if rule.section not in relevant_rules_accumulator:
                            relevant_rules_accumulator[rule.section] = {}
                        if rule.id not in relevant_rules_accumulator[rule.section]:
                            relevant_rules_accumulator[rule.section][rule.id] = {}
                        relevant_rules_accumulator[rule.section][rule.id]["content"] = rule.content
                        relevant_rules_accumulator[rule.section][rule.id]["explanation"] = rule.explanation

            if len(relevant_rules_accumulator) == 0:
                relevant_rules = None
            else:
                relevant_rules = []
                for section in relevant_rules_accumulator:
                    for rule_id in relevant_rules_accumulator[section]:
                        relevant_rules.append(BaseRule(
                            section=section,
                            id=rule_id,
                            content=relevant_rules_accumulator[section][rule_id]["content"],
                            explanation=relevant_rules_accumulator[section][rule_id]["explanation"]
                        ))

            # Proceed with the same for the next assistant if the question is applicable
            if assistant_report.proposal.response.applicable:
                if assistant_report.verification.response.adjustments_required:
                    # If the answer was adjusted during verification, use the adjusted answer
                    next_request = AssistantRequest(
                        original_question=entry_report.response.chosen_interpretation.content,
                        adjusted_question=assistant_report.proposal.response.question,
                        relevant_rules=relevant_rules,
                        response=assistant_report.verification.response.answer
                    )
                else:
                    # If the answer was not adjusted during verification, use the original answer of the assistant
                    next_request = AssistantRequest(
                        original_question=entry_report.response.chosen_interpretation.content,
                        adjusted_question=assistant_report.proposal.response.question,
                        relevant_rules=relevant_rules,
                        response=assistant_report.proposal.response.answer
                    )

        final_request = AssistantRequest(
            original_question=entry_report.response.original_user_question,
            adjusted_question=next_request.adjusted_question,
            response=next_request.response
        )
        
        print(f"Involving the finalizer")
        finalizer_agent = FinalizerAgent()
        finalizer_report = finalizer_agent.process_question(final_request)
        workflow["finalizer"] = finalizer_report.model_dump()

    # Save to JSON file
    with open(output_file_path, 'w', encoding='utf-8') as f:
        json.dump(workflow, f, ensure_ascii=False, indent=2)

    return workflow

def main():
    parser = argparse.ArgumentParser(description='Process user question and generate response')
    parser.add_argument('input', help='Input JSON file containing the question')
    parser.add_argument('--output', default='out.json', help='Output JSON file path (default: out.json)')
    
    args = parser.parse_args()
    
    try:
        initialize_llm()
        result = process_question(args.input, args.output)
        print(f"Response saved to {args.output}")
    except Exception as e:
        print(f"Error: {str(e)}")
        exit(1)

if __name__ == "__main__":
    main()
