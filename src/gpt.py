import sys
import os

sys.path.append(".")
from . import qa_pipeline
from . import summarizer


def construct_prompt(haystack_prediction):
    prediction = haystack_prediction["documents"][0]

    return (
        "Question: "
        + haystack_prediction["query"]
        + 'Based on this context: " '
        + prediction.content
    )


def answer_query_with_context(query, pipeline) -> str:
    haystack_prediction = qa_pipeline.query(query, pipeline)
    prompt = construct_prompt(haystack_prediction)
    response = summarizer.get_answer(prompt)
    return response
