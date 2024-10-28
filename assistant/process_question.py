import json
from llms import gemini
import argparse
from agents.entry import EntryAgent
from agents.router import RouterAgent

def process_question(input_file_path: str, output_file_path: str = "out.json"):
    with open(input_file_path, 'r', encoding='utf-8') as file:
        input_data = json.load(file)
        user_request = input_data.get('question')

    entry_agent = EntryAgent()
    router_agent = RouterAgent()

    entry_report = entry_agent.process_question(user_request)
    workflow = {
        "entrypoint": entry_report.model_dump()
    }

    if entry_report.response.reformulation_request is None:
        router_report = router_agent.process_question(entry_report.response.chosen_interpretation.content)
        workflow["router"] = router_report.model_dump()

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
        gemini.initialize()
        result = process_question(args.input, args.output)
        print(f"Response saved to {args.output}")
    except Exception as e:
        print(f"Error: {str(e)}")
        exit(1)

if __name__ == "__main__":
    main()
