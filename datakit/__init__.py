from itertools import combinations

import pandas as pd

import cli, correlation

df = pd.read_csv(str(cli.flag.get_value("--file")))

rows = len(df.index)
columns = df.columns

print(f"Dataset: {str(cli.flag.get_value("--file"))}")
print(f"Rows: {rows}")
print(f"Columns: {len(columns)}")

intColumns = []

threshold = cli.flag.get_value("--corr-threshold")

print("━━━ Column Overview ━━━")
for column in columns:
    print(column, df[column].dtype)
    print("  - Unique:", df[column].nunique())
    missing = round(100 - ((len(df[column].dropna().index) / rows) * 100 ), 2)
    if missing > 0.0:
        print("  - Missing:", missing, "%")
    if df[column].dtype == int or df[column].dtype == float:
        print("  - Top:", df[column].nlargest(int(cli.flag.get_value("--top"))).values)
        if df[column].nunique() != rows:
            minValue = min(df[column])
            maxValue = min(df[column])
            print("  - Min: ", minValue)
            print("  - Max: ", maxValue)
            print("  - Range: ", maxValue - minValue)
        
        intColumns.append(column)
    
    print()

if len(intColumns) > 1:
    combos = combinations(intColumns, 2)
    for eachCombo in combos:
        R = correlation.correlation(df[eachCombo[0]], df[eachCombo[1]])
        if R > float(threshold):
            print("Signifcant Correlation: ", eachCombo[0], eachCombo[1], R)