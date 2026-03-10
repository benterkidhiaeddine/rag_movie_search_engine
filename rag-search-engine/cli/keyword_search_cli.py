#!/usr/bin/env python3
import json

import argparse
from pathlib import Path
from typing import List

# More reliable way for handling paths in python
parent_directory = Path(__file__).parent.parent
MOVIES_DB_FILE_PATH =  parent_directory / "data" / "movies.json"


def search_in_movies_db(query: str, limit=5) -> List[dict[str, str | int]]:
    # Initiate the result
    search_result  = []

    # Load the movies db
    try:
        jsonfile = open(MOVIES_DB_FILE_PATH, mode="r", encoding="utf-8")
        movies_db = json.load(jsonfile)
        jsonfile.close()
    except FileNotFoundError:
        print(f"The file {MOVIES_DB_FILE_PATH} does not exist")
        return search_result
    
    # Itterate over the list of movies
    for movie in movies_db["movies"]:
        if query in movie["title"]:
            search_result.append(movie)
        

    return search_result[:limit]




def main() -> None:
    parser = argparse.ArgumentParser(description="Keyword Search CLI")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    search_parser = subparsers.add_parser("search", help="Search movies using BM25")
    search_parser.add_argument("query", type=str, help="Search query")

    args = parser.parse_args()

    match args.command:
        case "search":
            search_query = args.query
            # print the search query here
            print(f"Searching for: {search_query}")

            search_result = search_in_movies_db(search_query)
            for i , movie in enumerate(search_result, start=1):
                print(f"{i}. {movie['title']}")
        case _:
            parser.print_help()


if __name__ == "__main__":
    main()