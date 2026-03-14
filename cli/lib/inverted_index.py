import os
from typing import List, Set
from pathlib import Path
from pickle import dump


from lib.search_utils import tokenize, load_movies_db


PROJECT_ROOT = Path(__file__).resolve().parents[2]

CACHE_PATH = PROJECT_ROOT / "cache"


class InvertedIndex:

    def __init__(
        self,
        index: dict[str, Set[int]] = {},
        docmap: dict[int, str] = {},
    ) -> None:
        self.index = index
        self.docmap = docmap

    def __add_document(self, doc_id: int, text: str) -> None:
        tokens = tokenize(text)
        for token in tokens:
            if token in self.index:
                self.index[token].add(doc_id)
            else:
                self.index[token] = {doc_id}

    def get_documents(self, term: str):
        term = term.lower()
        try:
            result = self.index[term]
        except KeyError:
            print("No index was found for the given term")
            return []
        result = list(sorted(result))

        return result

    def build(self) -> None:
        movies = load_movies_db()

        size = len(movies)
        for i, movie in enumerate(movies, start=1):
            movie_object = f"{movie["title"]} {movie["description"]}"
            id = movie["id"]
            print(f"Adding {id} {movie["title"]} ...")
            self.__add_document(id, movie_object)
            self.docmap[id] = movie_object
            print(f"{i}/{size} movies added to Index")

    def save(self):
        os.makedirs(CACHE_PATH, exist_ok=True)

        print("Pickling indexes ...")
        with open(CACHE_PATH / "index.pkl", "wb") as f:
            dump(self.index, f)

        print("Pickling docmap ...")
        with open(CACHE_PATH / "docmap.pkl", "wb") as f:
            dump(self.docmap, f)
