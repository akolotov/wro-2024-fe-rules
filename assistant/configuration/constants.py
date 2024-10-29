from pathlib import Path
from pydantic import BaseModel

class Constants(BaseModel):
    prompts_path: Path = Path('./prompts/gemini/team')
    rules_path: Path = Path('./rules')

    # Prompts files
    entry_prompt_file: str = 'entry.md'
    router_prompt_file: str = 'router-system.md'

    assistant_system_prompt_file: str = 'assistant-system.md'
    assistant_first_general_prompt_file: str = 'assistant-first-general.md'
    assistant_next_general_prompt_file: str = 'assistant-next-general.md'
    special_assistant_prompts_files: dict[str, list[str]] = {
        '19-appendix-y-randomization.md': ['assistant-first-specific-19.md', 'assistant-next-specific-19.md'],
        '20-appendix-z-one-lap.md': ['assistant-first-specific-20.md', 'assistant-next-specific-20.md'],
    }
    assistant_first_verification_prompt_file: str = 'assistant-first-verification.md'
    assistant_next_verification_prompt_file: str = 'assistant-next-verification.md'

    # Rules files 
    summary_file: str = '00-summary.md'
    annotations_file: str = 'ANNOTATIONS.md'

    # Generation parameters
    generation_temperature: float = 0.0

constants = Constants()