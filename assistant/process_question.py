import json
import os
import google.generativeai as genai
from dotenv import load_dotenv
from config import PROMPT_PATH, SUMMARY_PATH, ANNOTATIONS_PATH, GENERATION_TEMPERATURE
from helper import read_file_content, get_filename_from_path
from transformers import entry_response_xml_to_json
import xml.etree.ElementTree as ET
import argparse

load_dotenv()

def process_question(input_file_path: str, output_file_path: str = "out.json"):
    api_key = os.getenv('GEMINI_API_KEY')
    if not api_key:
        raise ValueError("GEMINI_API_KEY environment variable is not set")
    model_name = os.getenv('GEMINI_MODEL_NAME', 'gemini-1.5-flash-002')

    # Read input JSON
    with open(input_file_path, 'r', encoding='utf-8') as file:
        input_data = json.load(file)
        user_question = input_data.get('question')

    # Read necessary files
    prompt_template = read_file_content(PROMPT_PATH)
    summary_content = read_file_content(SUMMARY_PATH)
    annotations_content = read_file_content(ANNOTATIONS_PATH)

    # Replace placeholders in the prompt
    system_prompt = prompt_template.format(
        summary_filename=get_filename_from_path(SUMMARY_PATH),
        summary_file_content=summary_content,
        annotations_filename=get_filename_from_path(ANNOTATIONS_PATH),
        annotations_file_content=annotations_content
    )

    # Configure Google AI
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel(
        model_name,
        system_instruction=system_prompt,
        generation_config=genai.types.GenerationConfig(
            temperature=GENERATION_TEMPERATURE
        )        
    )

    # Format the user question as specified in the prompt
    formatted_question = f"<userQuestion>\n{user_question}\n</userQuestion>"

    # Generate response
    response = model.generate_content(formatted_question)

    print(response.usage_metadata)

    raw_text_response = response.candidates[0].content.parts[0].text
    formatted_response = entry_response_xml_to_json(raw_text_response)
    
    # Save to JSON file
    with open(output_file_path, 'w', encoding='utf-8') as f:
        json.dump(formatted_response.model_dump(), f, ensure_ascii=False, indent=2)
    # with open(output_file_path, 'w', encoding='utf-8') as f:
    #     f.write(text_response)

    return formatted_response

def main():
    parser = argparse.ArgumentParser(description='Process user question and generate response')
    parser.add_argument('input', help='Input JSON file containing the question')
    parser.add_argument('--output', default='out.json', help='Output JSON file path (default: out.json)')
    
    args = parser.parse_args()
    
    try:
        result = process_question(args.input, args.output)
        print(f"Response saved to {args.output}")
    except Exception as e:
        print(f"Error: {str(e)}")
        exit(1)

if __name__ == "__main__":
    main()
