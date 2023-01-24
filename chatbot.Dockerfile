FROM python:3.10
# Create api directory
WORKDIR /usr/src/chatbot
# Install app dependencies
ADD ./ /usr/src/chatbot
RUN ls /usr/src/chatbot
RUN  pip install --upgrade pip \
     && pip install pipenv \
     && pipenv install
    #  && pipenv run pip install .
RUN ls /usr/src/chatbot

CMD [ "pipenv", "run", "python", "run_slack_bot.py"]