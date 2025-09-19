import pandas as pd

# Data cleaning = the process of fixing/removing:
# incomplete, incorrect, or irrelevant data. ~75% of work done with Pandas is data cleaning

df = pd.read_csv("pandas\data.csv")

# 1. Drop irrelevant columns
df = df.drop(columns=["Legendary","No","Height"]) 
print(df)

df2 = pd.read_csv("pandas\data.csv")
# 2. Handle missing data
# dropna means Drop Not Available
df2 = df2.dropna(subset=["Type2"])
df2 = df2.fillna({"Type2":"None"})

# 3. Fix Inconsistent Values

df2["Type1"] = df2["Type1"].replace({"Grass":"GRASS", "Fire":"FIRE", "Water":"WATER"})

# 4. Standardize text
df2["Name"] = df2["Name"].str.lower()

# 5. Fix data types
df2["Legendary"] = df2["Legendary"].astype(bool)

# 6. Remove duplicate values
df2 = df2.drop_duplicates()
print(df2.to_string())