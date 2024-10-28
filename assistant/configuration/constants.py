from pathlib import Path
from pydantic import BaseModel

class Constants(BaseModel):
    prompts_path: Path = Path('./prompts/gemini/team')
    rules_path: Path = Path('./rules')

    # Prompts files
    entry_prompt_file: str = 'entry.md'
    router_prompt_file: str = 'router-system.md'
    # Rules files 
    summary_file: str = '00-summary.md'
    annotations_file: str = 'ANNOTATIONS.md'

    # Generation parameters
    generation_temperature: float = 0.0

constants = Constants()