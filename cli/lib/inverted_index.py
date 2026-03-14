import os
import sys
from typing import List, Set
from pathlib import Path
from collections import defaultdict
from pickle import dump, load


from lib.search_utils import tokenize, load_movies_db


PROJECT_ROOT = Path(__file__).resolve().parents[2]

CACHE_PATH = PROJECT_ROOT / "cache"


class InvertedIndex:

    def __init__(
        self,
    ) -> None:
        self.index: dict[str, Set[int]] = defaultdict(set)
        self.docmap: dict[int, dict] = {}
        self.index_path = CACHE_PATH / "index.pkl"
        self.docmap_path = CACHE_PATH / "docmap.pkl"

    def __add_document(self, doc_id: int, text: str) -> None:
        tokens = tokenize(text)
        for token in tokens:
            self.index[token].add(doc_id)

    def get_documents(self, term: str):
        term = term.lower()

        result = list(sorted(self.index[term]))

        return result

    def build(self) -> None:
        movies = load_movies_db()

        size = len(movies)
        for i, movie in enumerate(movies, start=1):
            movie_text = f"{movie["title"]} {movie["description"]}"
            id = movie["id"]

            print(f"Adding {id} {movie["title"]} ...")
            self.__add_document(id, movie_text)
            self.docmap[id] = movie  # id to document

            print(f"{i}/{size} movies added to Index")

    def save(self):
        os.makedirs(CACHE_PATH, exist_ok=True)

        print("Pickling indexes ...")
        with open(self.index_path, "wb") as f:
            dump(self.index, f)

        print("Pickling docmap ...")
        with open(self.docmap_path, "wb") as f:
            dump(self.docmap, f)

    def load(self):

        print("Loading indexes ...")
        try:
            with open(self.index_path, "rb") as f:
                self.index = load(f)
        except FileNotFoundError:
            print(
                f"Couldn't find file: {self.index_path} make sure to create it using the build command"
            )
            sys.exit(1)

        print("Loading docmap ...")
        try:
            with open(self.docmap_path, "rb") as f:
                self.docmap = load(f)
        except FileNotFoundError:
            print(
                f"Couldn't find file: {self.docmap_path}make sure to create it using the build command"
            )
            sys.exit(1)
