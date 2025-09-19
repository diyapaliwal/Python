import pandas as pd
df = pd.read_csv("pandas\data.csv", index_col = "Name")

pokemon = input("Enter a Pokemon name: ")

try:
    print(df.loc[pokemon])
except:
    print(f"{pokemon} not found! Try again with the first letter capital or check the spelling.")