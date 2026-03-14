import string
from typing import List


from lib.inverted_index import InvertedIndex
from lib.search_utils import (
    tokenize,
    has_matching_token,
)


# Deprecated we will be using inverted Indexes insted
def keyword_search(
    data: dict, search_query: str, limit: int = 5
) -> List[dict[str, str | int]]:
    result = []

    search_query_tokens = tokenize(search_query)
    for el in data:

        # Text Processing
        title_tokens = tokenize(el["title"])
        if has_matching_token(search_query_tokens, title_tokens):
            result.append(el)

    return result[:limit]


def keyword_search_using_index(search_query: str, limit: int = 5):

    inverted_index = InvertedIndex()
    inverted_index.load()

    seen, res = set(), []
    search_query_tokens = tokenize(search_query)
    for search_query_token in search_query_tokens:
        # get matching document ids for the token
        matching_movie_ids = inverted_index.get_documents(search_query_token)
        for matching_movie_id in matching_movie_ids:
            # avoids duplicates using a hash set
            if matching_movie_id in seen:
                continue

            seen.add(matching_movie_id)
            res.append(inverted_index.docmap[matching_movie_id])

            if len(res) >= limit:
                return res
    return res
