from itertools import combinations

import pandas as pd

import cli, correlation, Top, ProfileColumn

fileName = cli.flag.file
df = pd.read_csv(fileName)

rows = len(df.index)
columns = df.columns

print(f"Dataset: {fileName}")
print(f"Rows: {rows}")
print(f"Columns: {len(columns)}")

intColumns = []
threshold = cli.flag.get_value("--corr-threshold")

print("━━━ Column Overview ━━━")
for column in columns:
    print(column, df[column].dtype)

    profile = ProfileColumn.ProfileColumn(df, column, rows, cli.flag.top)

    print(profile["kind"], profile["role"])

    if profile["kind"] == "numeric":
        if profile["role"] != "identifier":
            print(profile["stats"])
            intColumns.append(column)

    if profile.get("imbalence", False):
        print("Imbalence:", profile["imbalence"])
    
    if profile.get("TopValues", False):
        print(', '.join(profile["TopValues"]))

    print()

if len(intColumns) > 1:
    combos = combinations(intColumns, 2)
    for eachCombo in combos:
        R = correlation.correlation(df[eachCombo[0]].dropna(), df[eachCombo[1]].dropna())
        if abs(R) > float(threshold) :
            print("Signifcant Correlation: ", eachCombo[0], eachCombo[1], R)