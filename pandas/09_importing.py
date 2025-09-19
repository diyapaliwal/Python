import pandas as pd
df = pd.read_csv("pandas\data.csv")
''' for json file:
df = pd.read_json("pandas\data.json")'''
print(df) # It shows 5 upper 5 lower rows only not whole data
print(df.to_string()) # it shows whole data