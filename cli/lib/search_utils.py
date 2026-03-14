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

    return movies_db["movies"]


def load_stop_words() -> List[str]:

    with open(STOP_WORDS_FILE_PATH, "r") as f:
        stop_words = f.read().splitlines()
    return stop_words


def clean_text(word: str) -> str:

    punc_trans_table = str.maketrans("", "", string.punctuation)
    result = word.lower().translate(punc_trans_table)
    return result


def has_matching_token(query_tokens: List[str], movie_tokens: List[str]) -> bool:
    for query_token in query_tokens:
        for movie_token in movie_tokens:
            if query_token in movie_token:
                return True
    return False


def remove_stop_words(tokens: List[str]) -> List[str]:
    stop_words = load_stop_words()
    result = []
    for token in tokens:
        if token not in stop_words:
            result.append(token)

    return result


def stem_tokens(tokens: List[str]) -> List[str]:
    from nltk.stem import PorterStemmer

    stemmer = PorterStemmer()

    result = [stemmer.stem(token) for token in tokens]
    return result


def tokenize(word: str) -> List[str]:
    word = clean_text(word)
    result = [token for token in word.split(" ") if token]

    result = remove_stop_words(result)

    result = stem_tokens(result)
    return result


if __name__ == "__main__":
    assert set(remove_stop_words(["hello", "the", "out"])) == set(["hello"])
    assert tokenize("hello by what ( )") == ["hello", "by", "what", "(", ")"]
