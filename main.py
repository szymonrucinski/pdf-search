import src.qa_pipeline as qa_pipeline
import src.gpt as gpt
from src.data_cleaning import clean_data_get_handbook_dict


def welcome():
    print("Welcome to your source of infinite knowledge")


def query(query):
    answer = gpt.answer_query_with_context(query, pipeline)
    return answer


hanbook = clean_data_get_handbook_dict()


if __name__ == "__main__":
    welcome()
    hanbook = clean_data_get_handbook_dict()
    pipeline = qa_pipeline.build_pipeline(hanbook)
    print("Pipeline built")
    question = "What should I do when I have no work to do at Visium?"
    answer = gpt.answer_query_with_context(question, pipeline)

    print(answer)
