import sys
import json
import string
from io import TextIOBase
from pathlib import Path
from typing import List

PROJECT_ROOT = Path(__file__).resolve().parents[2]

MOVIES_DB_FILE_PATH = PROJECT_ROOT / "data" / "movies.json"

STOP_WORDS_FILE_PATH = PROJECT_ROOT / "data" / "stopwords.txt"


def load_movies_db() -> dict:
    result = {}
    # Load the movies db
    try:
        jsonfile = open(MOVIES_DB_FILE_PATH, mode="r", encoding="utf-8")
        movies_db = json.load(jsonfile)
        jsonfile.close()
    except FileNotFoundError:
        print(f"The file {MOVIES_DB_FILE_PATH} does not exist")
        sys.exit(1)

    return movies_db


def load_stop_words() -> List[str]:

    with open(STOP_WORDS_FILE_PATH, "r") as f:
        stop_words = f.read().splitlines()
    return stop_words


def tokenize(word: str) -> List[str]:
    # Mapping table from punctuation to None to allow the translate function to remove punctuation
    punc_trans_table = str.maketrans({punc: None for punc in string.punctuation})

    result = word.lower().translate(punc_trans_table).split(" ")

    return result


def remove_stop_words(tokens: List[str]) -> List[str]:
    stop_words = load_stop_words()
    result = []
    for token in tokens:
        if token not in stop_words:
            result.append(token)

    return result


if __name__ == "__main__":
    print(remove_stop_words(["hello", "the", "out"]))
    assert set(remove_stop_words(["hello", "the", "out"])) == set(["hello"])
