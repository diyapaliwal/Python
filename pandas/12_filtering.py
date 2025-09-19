import pandas as pd

df = pd.read_csv("pandas\data.csv")
# Filtering = Keeping the rows that match a condition

poisonous_poki = df[df["Type1"] == "Poison"]
print(poisonous_poki,"\n")

tall_poki = df[df["Height"] >= 2]
print(tall_poki,"\n")

legen_poki = df[df["Legendary"]==True]
print(legen_poki,"\n")

poison_poki = df[(df["Type1"]=="Poison") | (df["Type2"]=="Poison")] 
print(poison_poki,"\n")

fire_flying_poki = df[(df["Type1"]=="Fire") & (df["Type2"]=="Flying")]
print(fire_flying_poki) 