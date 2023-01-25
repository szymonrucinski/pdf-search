import sys
import logging
import os
import re

sys.path.append(".")
from dotenv import load_dotenv
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

import src.qa_pipeline as qa_pipeline
import src.gpt as gpt
from src.data_cleaning import clean_data_get_handbook_dict

load_dotenv()

SLACK_APP_TOKEN = os.environ["SLACK_APP_TOKEN"]
SLACK_BOT_TOKEN = os.environ["SLACK_BOT_TOKEN"]

app = App(token=SLACK_BOT_TOKEN, name="hr-bot")
logger = logging.getLogger(__name__)


@app.event("message")  # type: ignore
def answer_hr_question(message, say):
    """Send a random pyjoke back"""
    channel_type = message["channel_type"]
    if channel_type != "im":
        return

    dm_channel = message["channel"]
    user_id = message["user"]

    # joke = pyjokes.get_joke()
    answer = gpt.answer_query_with_context(message["text"], pipeline)[0]["summary_text"]

    logger.info(f"Sent answer < {answer} > to user {user_id}")

    say(text=answer, channel=dm_channel)


@app.command("/topics")
def repeat_text(ack, say, command):
    # Acknowledge command request
    ack()
    files = os.listdir("./mocks")
    files = [f.split(" ") for f in files]
    new_str = [" ".join(f[0:-1]) + "\n" for f in files]
    new_str = "".join(new_str)

    say(f"Here are the topics that you can ask me about: \n {new_str}")


def init_pipeline():
    hanbook = clean_data_get_handbook_dict()
    global pipeline
    pipeline = qa_pipeline.build_pipeline(hanbook)
    print("Pipeline built")


def main():
    # load db
    init_pipeline()
    handler = SocketModeHandler(app, SLACK_APP_TOKEN)
    handler.start()


if __name__ == "__main__":
    main()
