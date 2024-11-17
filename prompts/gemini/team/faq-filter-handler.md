{user_request}

The question/clarification request is a JSON object above where the field `request` is the question text.

Here is the process:

1. Try to understand the essence of the question by applying your knowledge of the game base on the summary.
2. Go through the "Questions and answers" part of the rules and find a pair of the questions and answers which are most relevant to the user's question.
3. If there is no relevant pair, respond that the question is not applicable to the "Questions and answers" part.
4. If there is a relevant pair, provide exact answer found in the "Questions and answers" part.

Your goal is to provide the output following the schema provided. Ensure that all fields are present and correctly formatted.
Schema Description:

- 'chain_of_thought': The chain of thoughts and reasoning why the corresponding pair of the questions and answers is going to be chosen. Or why the question is not applicable to the "Questions and answers" part.
- 'applicable': False, if the question is not applicable to the "Questions and answers" part otherwise True.
- 'question': The question found in the "Questions and answers" part.
- 'answer': The answer found in the "Questions and answers" part.
