import string
from typing import List


from lib.search_utils import tokenize, remove_stop_words, stem_tokens


# Mapping table from punctuation to None to allow the translate function to remove punctuation
punc_trans_table = str.maketrans({punc: None for punc in string.punctuation})


def keyword_search(
    data: dict, search_query: str, limit: int = 5
) -> List[dict[str, str | int]]:
    result = []
    for el in data["movies"]:

        # Text Processing
        search_query_tokens = stem_tokens(
            remove_stop_words(
                tokenize(search_query),
            )
        )
        title_tokens = stem_tokens(
            remove_stop_words(
                tokenize(el["title"]),
            )
        )

        found = False
        # If any token from the query matches a token in a title add It to our result
        for title_token in title_tokens:
            if found:
                break
            for search_query_token in search_query_tokens:
                if search_query_token in title_token:
                    # Flag denoting that we have a match
                    found = True
                    result.append(el)

    return result[:limit]


if __name__ == "__main__":
    assert "Hello !! ---- ".translate(punc_trans_table) == "Hello   "
