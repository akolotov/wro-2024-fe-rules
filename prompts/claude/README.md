# Setting Up Claude Assistant for WRO Future Engineers Judges

## Overview
This guide explains how to set up Claude as an assistant for judging the WRO Future Engineers competition. The setup involves configuring Claude with specific rules documents and custom instructions that enable it to provide consistent and accurate assistance with rule interpretations.

## Repository Structure
```
prompts/
└── claude/
    ├── instructions-writing.md   # Custom instructions for Claude
rules/                            # WRO Future Engineers rules files
```

## Interaction Modes

Claude supports two distinct modes of operation:

1. **Question Answering Mode**
   - Activated by starting your message with "Question:"
   - Used specifically for rule interpretations and competition-related questions
   - Provides responses in structured XML format
   - Example: "Question: Can traffic signs be placed directly in front of a vehicle's starting position?"

2. **Assistant Mode**
   - Activated by any message that doesn't start with "Question:"
   - Used for general assistance, discussions, and non-rule-related tasks
   - Provides responses in plain text format
   - Example: "Could you help me organize the judging schedule for tomorrow?"

The mode is determined message by message - you can switch between modes freely during your conversation with Claude.

## Setup Steps

1. **Create a New Claude Project**
   - Log in to your Claude interface
   - Create a new project
   - Name it appropriately (e.g., "WRO FE 2024 Judge Assistant")

2. **Add Rule Documents**
   The following files from [the `rules` directory](../../rules) need to be added to the project content:
   - ANNOTATIONS.md
   - 00-summary.md
   - 01-general-information.md
   - 02-team-and-age-groups.md
   - 03-responsibilities.md
   - 04-game-documents.md
   - 05-game-description.md
   - 06-surprise-rule.md
   - 07-documentation.md
   - 08-challenge-rounds.md
   - 09-specific-rules.md
   - 10-scoring.md
   - 11-vehicle.md
   - 12-competition-format.md
   - 13-game-table.md
   - 14-glossary.md
   - 15-appendix-a-explanatories.md
   - 16-appendix-b-gf.md
   - 17-appendix-c-ejv.md
   - 18-appendix-d-msec.md
   - 19-appendix-y-randomization.md
   - 20-appendix-z-one-lap.md
   - 21-appendix-w-scoring.md
   - 99-questions-and-answers.md

3. **Configure Custom Instructions**
   - Locate the `instructions-writing.md` file
   - Copy its contents into Claude's custom instructions section
   - Ensure all sections (preferences, artifacts info, etc.) are properly transferred

4. **Verify Setup**
   Test both modes:
   ```
   Question: Can traffic signs be placed directly in front of a vehicle's starting position?
   ```
   Should return XML format response.
   ```
   Could you help me summarize the key differences between Open and Obstacle challenges?
   ```
   Should return plain text response.

## Usage Guidelines

1. **Question Answering Mode**
   - Start messages with "Question:" for rule interpretations
   - Responses will be in XML format:
   ```xml
   <response>
     <source>Rule reference</source>
     <chain_of_thought>Reasoning</chain_of_thought>
     <answer>Final answer</answer>
   </response>
   ```
   - Best for specific rule clarifications and judging decisions

2. **Assistant Mode**
   - Use regular messages without "Question:" prefix
   - Get help with general tasks, scheduling, documentation
   - Responses will be in plain text
   - Best for general assistance and discussions

3. **Best Practices**
   - Be specific in your questions
   - Reference specific situations or rules when possible
   - Use clear language to avoid ambiguity
   - Choose the appropriate mode for your needs
   - Always verify Claude's responses:
     * Rephrase your question and ask again to check if responses correlate
     * Inspect the game rules sections that Claude refers to in its answers
     * Never rely solely on Claude's interpretation without verification
     * Remember that Claude is an assistant tool to help with rule interpretation, not a replacement for human judgment

## Troubleshooting

If Claude's responses don't follow the expected format or seem incorrect:
1. Verify all rules files are properly loaded
2. Check that custom instructions are correctly copied
3. Ensure you're using the correct prefix for the desired mode
4. Check that questions about rules start with "Question:"

## Maintenance

- Update rules files when new versions are released
- Keep track of any Q&As or rule clarifications
- Report any inconsistencies or issues in responses
