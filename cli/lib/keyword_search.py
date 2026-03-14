import string
from typing import List


from lib.search_utils import (
    tokenize,
    has_matching_token,
)


def keyword_search(
    data: dict, search_query: str, limit: int = 5
) -> List[dict[str, str | int]]:
    result = []

    search_query_tokens = tokenize(search_query)
    for el in data["movies"]:

        # Text Processing
        title_tokens = tokenize(el["title"])
        if has_matching_token(search_query_tokens, title_tokens):
            result.append(el)

    return result[:limit]
