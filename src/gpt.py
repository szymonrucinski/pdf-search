import sys
import os
import logging
import coloredlogs

coloredlogs.install()
logger = logging.getLogger(__name__)

sys.path.append(".")
from . import qa_pipeline
from . import summarizer


# def construct_prompt(haystack_prediction):
#     prediction = haystack_prediction["documents"][0]
#     logger.info(haystack_prediction)

#     return (
#         "Question: "
#         + haystack_prediction["query"]
#         + 'Based on this context: " '
#         + prediction.content
#     )


def answer_query_with_context(query, pipeline) -> str:
    haystack_prediction = qa_pipeline.query(query, pipeline)

    # prompt = construct_prompt(haystack_prediction)
    # response = summarizer.get_answer(prompt)

    response = (
        haystack_prediction.get("answers")[0].answer
        + " \n BASED ON THIS CONTEXT: \n"
        + haystack_prediction.get("answers")[0].context
    )
    return response
