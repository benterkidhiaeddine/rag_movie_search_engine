import string
from typing import List


# Mapping table from punctuation to None to allow the translate function to remove punctuation
punc_trans_table = str.maketrans({punc: None for punc in string.punctuation})


def keyword_search(
    data: dict, search_query: str, limit: int = 5
) -> List[dict[str, str | int]]:
    result = []
    for el in data["movies"]:
        # Text Processing
        search_query = search_query.lower().translate(punc_trans_table)
        title = el["title"].lower().translate(punc_trans_table)

        if search_query in title:
            result.append(el)
    return result[:limit]


if __name__ == "__main__":
    assert "Hello !! ---- ".translate(punc_trans_table) == "Hello   "
