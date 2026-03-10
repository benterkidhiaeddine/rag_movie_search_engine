import sys
import json
import string
from pathlib import Path
from typing import List

PROJECT_ROOT = Path(__file__).resolve().parents[2]

MOVIES_DB_FILE_PATH = PROJECT_ROOT / "data" / "movies.json"


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


def tokenize(word: str) -> List[str]:
    # Mapping table from punctuation to None to allow the translate function to remove punctuation
    punc_trans_table = str.maketrans({punc: None for punc in string.punctuation})

    result = word.lower().translate(punc_trans_table).split(" ")

    return result
