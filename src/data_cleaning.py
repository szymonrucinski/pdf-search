import os
import glob
from bs4 import BeautifulSoup
import nltk
import emoji
from dataclasses import dataclass


@dataclass
class book:
    id: str
    text: str


def remove_non_html_files(data_dir) -> None:
    print("Removing non .html files")
    for clean_up in glob.glob(data_dir):
        if not clean_up.endswith(".html"):
            os.remove(clean_up)


def load_data_html_files_to_dict(data_dir) -> dict:
    handbook = dict()
    for chapter_name in glob.glob(data_dir):
        with open(chapter_name, "r") as f:
            content = f.read()
            handbook[chapter_name] = content
    return handbook


def concat_all_text_files_to_file(data_dir) -> str:
    print("Concatenating all text files to one file")
    array = []
    for filename in glob.glob(data_dir):
        array.append("".join(open(filename).readlines()))
    return array


def get_plain_text_from_html(text) -> str:
    soup = BeautifulSoup(text, "html.parser")
    plain_text = soup.get_text()
    return plain_text


def remove_emoji(plain_text) -> str:
    demojified_text = emoji.replace_emoji(plain_text, replace="")
    return demojified_text


def clean_data_get_handbook_dict(data_dir="./mocks/*") -> list:
    remove_non_html_files(data_dir)
    handbook = load_data_html_files_to_dict(data_dir)
    handbook_arr = []
    for i, text in enumerate(handbook.values()):
        plain_text = get_plain_text_from_html(text)

        plain_text_no_emoji = remove_emoji(plain_text)
        obj = {"id": str(i), "chapter": str(i), "content": plain_text_no_emoji}
        handbook_arr.append(obj)
    return handbook_arr
