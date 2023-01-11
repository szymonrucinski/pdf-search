from transformers import pipeline

global generator
generator = pipeline("text-generation", model="facebook/opt-350m")


def ask_opt(question):
    len(question)
    return generator(question, max_lenght=question + 500)
