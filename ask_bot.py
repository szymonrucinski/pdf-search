from transformers import pipeline

global generator
summarizer = pipeline("summarization", model="philschmid/bart-large-cnn-samsum")
from transformers import AutoTokenizer, AutoModelForCausalLM


def get_answer(question):
    # tokenizer = AutoTokenizer.from_pretrained("facebook/opt-350m")
    # model = AutoModelForCausalLM.from_pretrained("facebook/opt-350m")
    # input_ids = tokenizer(question, return_tensors="pt").input_ids
    # outputs = model.generate(input_ids, do_sample=False, max_new_tokens=200)
    answer = summarizer(question)

    print(answer)
    return answer
