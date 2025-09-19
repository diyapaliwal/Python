import pandas as pd

df = pd.read_csv("pandas\data.csv")
print(df.mean(numeric_only = True))
print(df.sum(numeric_only = True))
print(df.min(numeric_only = True))
print(df.max(numeric_only = True))
print(df.count(),"\n")

#Single column
print(df["Height"].mean(),"\n")
print(df["Height"].sum(),"\n")
print(df["Weight"].max(),"\n")