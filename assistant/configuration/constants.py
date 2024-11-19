from pathlib import Path
from pydantic import BaseModel

class Constants(BaseModel):
    prompts_path: Path = Path('./prompts/gemini/team')
    rules_path: Path = Path('./rules')

    # Prompts files
    entry_prompt_file: str = 'entry.md'
    router_prompt_file: str = 'router-system.md'
    
    faq_filter_system_prompt_file: str = 'faq-filter-system.md'
    faq_filter_handler_prompt_file: str = 'faq-filter-handler.md'
    faq_filter_verification_prompt_file: str = 'faq-filter-verification.md'

    assistant_system_prompt_file: str = 'assistant-system.md'
    assistant_system_multi_section_prompt_file: str = 'assistant-system-multi-section.md'
    assistant_first_general_prompt_file: str = 'assistant-first-general.md'
    assistant_next_general_prompt_file: str = 'assistant-next-general.md'
    special_assistant_prompts_files: dict[str, list[str]] = {
        '19-appendix-y-randomization.md': ['assistant-first-specific-19.md', 'assistant-next-specific-19.md'],
        '20-appendix-z-one-lap.md': ['assistant-first-specific-20.md', 'assistant-next-specific-20.md'],
    }
    assistant_first_verification_prompt_file: str = 'assistant-first-verification.md'
    assistant_next_verification_prompt_file: str = 'assistant-next-verification.md'

    finalizer_prompt_file: str = 'finalizer-system.md'

    # Rules files common for all sections
    summary_file: str = '00-summary.md'
    annotations_file: str = 'ANNOTATIONS.md'
    faq_file: str = '99-questions-and-answers.md'
    dependant_sections: dict[str, list[str]] = {
        '09-specific-rules.md': ['15-appendix-a-explanatories.md'],
        '15-appendix-a-explanatories.md': ['09-specific-rules.md'],
        '07-documentation.md': ['17-appendix-c-ejv.md'],
        '17-appendix-c-ejv.md': ['07-documentation.md'],
        '10-scoring.md': ['21-appendix-w-scoring.md', '17-appendix-c-ejv.md'],
        '08-challenge-rounds.md': ['19-appendix-y-randomization.md'],
        '21-appendix-w-scoring.md': ['10-scoring.md']
    }

    # Generation parameters
    generation_temperature: float = 0.1

constants = Constants()