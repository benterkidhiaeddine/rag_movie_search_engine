import string
from typing import List


from lib.search_utils import (
    tokenize,
    remove_stop_words,
    stem_tokens,
    has_matching_token,
)


def keyword_search(
    data: dict, search_query: str, limit: int = 5
) -> List[dict[str, str | int]]:
    result = []

    search_query_tokens = stem_tokens(
        remove_stop_words(
            tokenize(search_query),
        )
    )
    for el in data["movies"]:

        # Text Processing
        title_tokens = stem_tokens(
            remove_stop_words(
                tokenize(el["title"]),
            )
        )
        if has_matching_token(search_query_tokens, title_tokens):
            result.append(el)

    return result[:limit]
