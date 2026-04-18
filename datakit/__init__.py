from itertools import combinations

import pandas as pd

import cli, correlation, Top

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
    
    ### Numeric:
    if df[column].dtype == int or df[column].dtype == float:
        missing = round(100 - ((len(df[column].dropna().index) / rows) * 100 ), 2)
        if missing > 0.0:
            print("  - Missing:", missing, "%")
        minValue = df[column].min()
        maxValue = df[column].nlargest(1).values
        print("  - Min: ", minValue)
        print("  - Max: ", maxValue[0])
        print("  - Range: ", maxValue[0] - minValue)
        print("  - Mean", sum(df[column]) / len(df[column]))
        
        intColumns.append(column)
        print()
        continue
    
    ### Categorical:
    # unique count
    print("  - Unique:", df[column].nunique())
    
    if df[column].nunique() != rows:
        # top values
        print("  - Top:", ', '.join(list(Top.Top(df[column].to_list(), int(cli.flag.get_value("--top"))))))

        # imbalance detection
        imbalence = Top.Imbalence(df[column].to_list(), rows)
        print("  - Imbalence:", imbalence ) if imbalence else ""


    ### Structural flags:

    # is identifier?

    # is constant?

    # is sparse?

    
    print()

if len(intColumns) > 1:
    combos = combinations(intColumns, 2)
    for eachCombo in combos:
        R = correlation.correlation(df[eachCombo[0]], df[eachCombo[1]])
        if R > float(threshold):
            print("Signifcant Correlation: ", eachCombo[0], eachCombo[1], R)