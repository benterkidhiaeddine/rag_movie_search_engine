from typing import List



def keyword_search(data: dict, search_query: str, limit: int = 5) -> List[dict[str, str | int]]: 
    result = []
    for el in data["movies"]:
        if search_query in el["title"]:
            result.append(el)
    return result[:limit]
            
    
    