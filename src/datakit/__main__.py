from itertools import combinations

import pandas as pd

from .cli import cli
from .correlation import correlation
from .ProfileColumn import ProfileColumn

from .Adonis import PrintTable

flag = cli()

fileName = flag.file
df = pd.read_csv(fileName)

rows = len(df.index)
columns = df.columns

print(f"Dataset: {fileName}")
print(f"Rows: {rows}")
print(f"Columns: {len(columns)}")

intColumns = []
threshold = flag.corr_threshold

print("━━━ Column Overview ━━━")
for column in columns:
    print(column, df[column].dtype)

    profile = ProfileColumn(df, column, rows, flag.top)

    PrintTable(profile)
    print()

if len(intColumns) > 1:
    combos = combinations(intColumns, 2)
    for eachCombo in combos:
        try:
            clear_df = df.dropna(subset=[eachCombo[0], eachCombo[1]])
            R = correlation(clear_df[eachCombo[0]].to_list(), clear_df[eachCombo[1]].to_list())
            if abs(R) > float(threshold) :
                print("Signifcant Correlation: ", eachCombo[0], eachCombo[1], R)
        except Exception as e:
            print(f"There was an error: {e}")