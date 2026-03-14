#!/usr/bin/env python3

import argparse

from lib.keyword_search import keyword_search
from lib.search_utils import load_movies_db

from lib.inverted_index import InvertedIndex


def main() -> None:
    parser = argparse.ArgumentParser(description="Keyword Search CLI")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    search_parser = subparsers.add_parser("search", help="Search movies using BM25")
    build_parser = subparsers.add_parser("build", help="Build movies inverted Index")
    search_parser.add_argument("query", type=str, help="Search query")

    args = parser.parse_args()

    match args.command:
        case "search":
            search_query = args.query
            # print the search query here
            print(f"Searching for: {search_query}")

            movies_db_data = load_movies_db()

            search_result = keyword_search(
                data=movies_db_data, search_query=search_query
            )
            for i, movie in enumerate(search_result, start=1):
                print(f"{i}. {movie['title']}")

        case "build":
            inverted_index = InvertedIndex()

            inverted_index.build()

            inverted_index.save()

            print(
                f"First document for token 'merida' = {inverted_index.get_documents("merida")[0]}"
            )

        case _:
            parser.print_help()


if __name__ == "__main__":
    main()
