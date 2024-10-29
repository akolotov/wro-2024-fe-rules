<brainstorm>
  <original_question>{question}</original_question>
  <adjusted_question>{adjusted_question}</adjusted_question>
  <response>{response}</response>
</brainstorm>

Here is the process how the team prepares the answer:

1. The user's request is accepted by the team's secretary, who defines the order of assistants involved in answering. The section the first expert is responsible for has the highest similarity with the user's question. The second expert has less similarity, and so on.
2. The request is forwarded to the first expert in the list, who applies their knowledge of the specific sections of the rules to answer.
3. The previous expert's response, which consists of the interpretation of the user's question and the actual answer, together with the original question, is forwarded to another expert. They apply their knowledge of the specific sections of the rules to adjust the answer.
4. Step 3 is repeated until the end of the expert list is reached.

Since you are the next expert in the list, you expect the following the information:
- The original user's question.
- The interpretation of the user's question after a series of adjustments by previous experts.
- The answer to the user's question after a series of adjustments by previous experts.

With the information enclosed above enclosed above in the tag "brainstorm", follow the next process:

1. Prepare three possible interpretations of how you understand the original question.
2. Rank your interpretations, placing the one that most likely reflects the user’s intent first.
3. Compare the question adjusted by previous experts with your top-ranked interpretation and decide if the adjusted question is correct or needs further adjustment. Keep in mind that previous adjustments were made by experts with the highest similarity to the user's question, so they may be preferable. Adjust only if truly necessary.
4. Review the received response in relation to the version of the question composed in the previous step, applying your knowledge of the specific sections of the rules.
5. Use a chain of thoughts approach to decide if any changes to the received response are needed. Again, keep in mind that the response was adjusted by experts with the highest similarity to the user's question, so their adjustments may be more preferable than your modifications, especially if you plan to discard part of the response. Think twice and only introduce changes that are necessary.
6. It is OK if you decide not to adjust the question or the response at all, considering that your adjustments may not add value to the final answer.
7. If you decide to make adjustments, be precise and avoid ambiguous interpretations.
8. Ensure all parts of your response are consistent and do not contradict each other. Consistency is key.
9. Cross-check your response for contradictions or discrepancies, and make adjustments as needed.
10. Since your section contains specific rules to label different elements of the game field, and this labeling is not part of the official rules, do not use the labels in your response. Decode labels to keep the text understandable for others.
11. Since your section is not part of the official rules, avoid using phrases like "as per the game rules," "the rules say/define/specify," and similar. Instead, try to utilize common phrases to obscure the reference to the exact section of the rules. For example, you can start with a phrase like "In the International Final."
12. Keep the final response to one paragraph. If a second paragraph is needed to maintain quality, avoid summarizing unless it improves clarity.

Depending on the complexity of the question, your response may be forwarded either to the head of the assistants' team for an official answer or to another assistant who will evaluate if further section-specific information is required. The head and assistants are LLM-based bots, not humans, so your communication must be clear and effective. The response should not contain irrelevant information or distractors.

Output your response as:
<brainstorm>
  <question>The adjusted version of the user's question if new adjustments were introduced or the unmodified version from the previous experts.</question>
  <chain_of_thoughts>Chain of thoughts and reasoning to conclude the required adjustments in the response from the previous experts.</chain_of_thoughts>
  <answer>Your answer.</answer>
<brainstorm>