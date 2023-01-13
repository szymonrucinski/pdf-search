import slack
import os
import json
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables
env_path = Path(".") / ".env"
load_dotenv(dotenv_path=env_path)

client = slack.WebClient(token=os.environ.get("SLACK_TOKEN"))

client.chat_postMessage(channel="#ask-hr-bot", text="Hello world!")
