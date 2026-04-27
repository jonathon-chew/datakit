from itertools import combinations

import pandas as pd

import cli, correlation, ProfileColumn, Adonis

fileName = cli.flag.file
df = pd.read_csv(fileName)

rows = len(df.index)
columns = df.columns

print(f"Dataset: {fileName}")
print(f"Rows: {rows}")
print(f"Columns: {len(columns)}")

intColumns = []
threshold = cli.flag.corr_threshold

print("━━━ Column Overview ━━━")
for column in columns:
    print(column, df[column].dtype)

    profile = ProfileColumn.ProfileColumn(df, column, rows, cli.flag.top)

    Adonis.PrintTable(profile)
    print()

if len(intColumns) > 1:
    combos = combinations(intColumns, 2)
    for eachCombo in combos:
        try:
            clear_df = df.dropna(subset=[eachCombo[0], eachCombo[1]])
            R = correlation.correlation(clear_df[eachCombo[0]].to_list(), clear_df[eachCombo[1]].to_list())
            if abs(R) > float(threshold) :
                print("Signifcant Correlation: ", eachCombo[0], eachCombo[1], R)
        except Exception as e:
            print(f"There was an error: {e}")