from typing import Any
from collections import defaultdict

def Top(a: list[Any], k: int = 1) -> list[str]:

    if k <= 0:
        raise ValueError("Top needs to be a positive integer!")

    unique: set[str] = set(a)
    hash = {k: 0 for k in unique}
    for x in a:
        if x in hash.keys():
            hash[x] += 1
    
    _list = sorted(hash.items(), key=lambda item: item[1])

    return [ans[0] for ans in _list[0:k]]

def Imbalence(a: list[Any], number_of_rows: int=0, threshold: float=0.7) -> dict[str, float]:
    # top_ratio = count(top_value) / total_rows
    
    unique: set[str] = set(a)
    hash = {k: 0.0 for k in unique}
    Imbalence = hash.copy()
    for x in a:
        if x in hash.keys():
            hash[x] += 1
    
    for k, v in hash.items():
        value = Imbalence[k] = v / number_of_rows
        if value > threshold:
            Imbalence[k] = value
        else:
            Imbalence.pop(k)

    return Imbalence