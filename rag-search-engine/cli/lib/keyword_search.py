import string
from typing import List


from lib.search_utils import tokenize


# Mapping table from punctuation to None to allow the translate function to remove punctuation
punc_trans_table = str.maketrans({punc: None for punc in string.punctuation})


def keyword_search(
    data: dict, search_query: str, limit: int = 5
) -> List[dict[str, str | int]]:
    result = []
    for el in data["movies"]:
        # Text Processing
        search_query_tokens = tokenize(search_query)
        title_tokens = tokenize(el["title"])

        # If any token from the query matches a token in a title add It to our result
        for search_token in search_query_tokens:
            for title_token in title_tokens:
                if search_token in title_token:
                    result.append(el)

    return result[:limit]


if __name__ == "__main__":
    assert "Hello !! ---- ".translate(punc_trans_table) == "Hello   "
