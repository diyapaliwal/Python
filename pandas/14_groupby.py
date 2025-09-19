import pandas as pd
df = pd.read_csv("pandas\data.csv")

poison_poki = df[df["Type1"] == "Poison"]
print(poison_poki)
group = df.groupby("Type1")
print(group["Weight"].max())