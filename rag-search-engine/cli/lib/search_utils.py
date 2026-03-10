import sys
import json
from pathlib import Path

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
