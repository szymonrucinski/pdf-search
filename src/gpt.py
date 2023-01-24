import openai
import os
from . import qa_pipeline as qa
from . import summarizer as summarizer

openai.api_key = os.environ.get("OPEN_AI_KEY")

# COMPLETIONS_MODEL = "text-davinci-002"

# COMPLETIONS_API_PARAMS = {
#     # We use temperature of 0.0 because it gives the most predictable, factual answer.
#     "temperature": 0.0,
#     "max_tokens": 500,
#     "model": COMPLETIONS_MODEL,
# }


def construct_prompt(haystack_prediction):
    prediction = haystack_prediction["documents"][0]

    return (
        "Question: "
        + haystack_prediction["query"]
        + 'Based on this context: " '
        + prediction.content
    )


def answer_query_with_context(query, pipeline) -> str:
    haystack_prediction = qa.qa_pipeline.query(query, pipeline)
    prompt = construct_prompt(haystack_prediction)
    response = summarizer.get_answer(prompt)
    return response
