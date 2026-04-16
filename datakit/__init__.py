import pandas as pd

import cli

df = pd.read_csv(str(cli.flag.get_value("--file")))

rows = df.index
columns = df.columns

print(f"Dataset: {str(cli.flag.get_value("--file"))}")
print(f"Rows: {len(rows)}")
print(f"Columns: {len(columns)}")

print("━━━ Column Overview ━━━")
for column in columns:
    print(column, df[column].dtype)
    print("  - Unique:", df[column].nunique())
    print("  - Missing:", round(100 - ((len(df[column].dropna().index) / len(rows)) * 100 ), 2), "%")
    if df[column].dtype == int:
        print("  - Top:", df[column].nlargest(1))