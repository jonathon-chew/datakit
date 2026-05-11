from typing import Any

import pandas as pd

from .Top import Top, Imbalence

def isNumeric(i: list[Any]) -> bool:
    
    cleaned = [x for x in i if pd.notna(x) and str(x).strip() != ""]

    if not cleaned:
        return False

    try:
        pd.to_numeric(pd.Series(cleaned), errors="raise")
    except Exception:
        return False

    return True

def ProfileColumn(df: pd.DataFrame, column: str, row_count: int=0, top: int=0) -> dict[str, Any]:

    if column == "":
        raise ValueError("There was no column title")
    
    if row_count == 0:
        raise ValueError("There were no rows?!")
    
    returnDict = {}
    
    # base stats
    """ unique_count
    missing_ratio """
    series = df[column]
    populated = series.dropna()

    missing = round(100 - ((len(populated.index) / row_count) * 100 ), 2)
    uniqueCount = series.nunique()
    uniqueRatio = uniqueCount / row_count

    returnDict["missing"] = missing
    returnDict["uniqueCount"] = uniqueCount

    # classification
    # kind → numeric | categorical | boolean | unknown
    if isNumeric(series.to_list()):
        returnDict["kind"] = "numeric"
    elif uniqueCount == 2:
        returnDict["kind"] = "boolean"
    elif uniqueCount > 2 and uniqueRatio <= 0.2:
        returnDict["kind"] = "categorical"
    else:
        returnDict["kind"] = None

    # structural role
    # role → identifier | constant | sparse | feature
    # Uniqueness for being an identifier is AT LEAST 95% of the column is unique
    sparse = missing > 50
    if uniqueCount == 1:
        returnDict["role"] = "constant"
    elif uniqueCount > ((row_count / 100) * 95):
        returnDict["role"] = "identifier"
    elif sparse:
        returnDict["role"] = "sparse"
    else:
        returnDict["role"] = "feature"
    
    # optional signals
    # imbalance → None | moderate | high
    imbalence = Imbalence(populated.to_list(), len(populated.index), 0.7)
    if imbalence:
        returnDict["imbalence"] = f"high {imbalence}"

    # numeric only
    # min, max, mean, range
    if returnDict["kind"] == "numeric" and returnDict["role"] != "identifier":
        numericSeries = pd.to_numeric(populated, errors="coerce").dropna()
        returnDict["stats"] = {
            "min" : float(numericSeries.min()),
            "max" : float(numericSeries.max()),
            "mean" : round(float(numericSeries.mean()), 2),
            "range" : round(float(numericSeries.max() - numericSeries.min()), 2),
        }

    # categorical only
    #top_values
    if returnDict["kind"] == "categorical" and uniqueRatio < 0.5 and top > 0:
        returnDict["TopValues"] = Top(populated.to_list(), top)

    return returnDict
