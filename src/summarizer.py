from transformers import pipeline

global generator
summarizer = pipeline("summarization", model="philschmid/bart-large-cnn-samsum")
from transformers import AutoTokenizer, AutoModelForCausalLM


def get_answer(question):
    answer = summarizer(question)
    print(answer)
    return answer