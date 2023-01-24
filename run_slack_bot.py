import logging
import os
import re
from src.summarizer import get_answer
from dotenv import load_dotenv
import pyjokes
import src.qa_pipeline as qa_pipeline
import src.gpt as gpt
from src.data_cleaning import clean_data_get_handbook_dict
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

load_dotenv()

SLACK_APP_TOKEN = os.environ["SLACK_APP_TOKEN"]
SLACK_BOT_TOKEN = os.environ["SLACK_BOT_TOKEN"]

app = App(token=SLACK_BOT_TOKEN, name="hr-bot")
logger = logging.getLogger(__name__)


@app.event("message")  # type: ignore
def show_random_joke(message, say):
    """Send a random pyjoke back"""
    channel_type = message["channel_type"]
    if channel_type != "im":
        return

    dm_channel = message["channel"]
    user_id = message["user"]

    # joke = pyjokes.get_joke()
    answer = gpt.answer_query_with_context(message["text"], pipeline)[0]["summary_text"]

    logger.info(f"Sent joke < {answer} > to user {user_id}")

    say(text=answer, channel=dm_channel)


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
