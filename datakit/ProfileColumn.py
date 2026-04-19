from typing import Any

import pandas as pd

import Top, cli

def isNumeric(i: list[Any]) -> bool:
    for x in i:
        try:
            int(x)
        except:
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
    missing = round(100 - ((len(df[column].dropna().index) / row_count) * 100 ), 2)
    uniqueCount = df[column].nunique()
    uniqueRatio = uniqueCount / row_count

    returnDict["missing"] = missing
    returnDict["uniqueCount"] = uniqueCount

    # classification
    # kind → numeric | categorical | boolean | unknown
    if isNumeric(df[column].to_list()):
        returnDict["kind"] = "numeric"
    elif uniqueRatio < (10 / row_count) * 100 and uniqueCount > 2:
        returnDict["kind"] = "categorical"
    elif uniqueCount == 2:
        returnDict["kind"] = "boolean"
    else:
        returnDict["kind"] = None

    # structural role
    # role → identifier | constant | sparse | feature
    # Uniqueness for being an identifier is AT LEAST 95% of the column is unique
    sparse = missing > 0.5
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
    imbalence = Top.Imbalence(df[column].to_list(), row_count, 0.7)
    if imbalence:
        returnDict["imbalence"] = f"high {imbalence}"

    # numeric only
    # min, max, mean, range
    if returnDict["kind"] == "numeric" and returnDict["role"] != "identifier":
        returnDict["stats"] = {
            "min" : int(df[column].min()),
            "max" : int(df[column].max()),
            "mean" : int(df[column].mean()),
            "range" : (int(df[column].max() - df[column].min())),
        }

    # categorical only
    #top_values
    if returnDict["kind"] == "categorical" and uniqueRatio < 0.5:
        returnDict["TopValues"] = Top.Top(df[column].to_list(), top)

    return returnDict