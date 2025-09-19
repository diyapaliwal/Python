import pandas as pd

df = pd.read_csv("pandas\data.csv")

#Selection by column
# print(df["Name"].to_string())
# print(df["Height"].to_string())
# print(df["Weight"].to_string())
# print(df["Type1"].to_string())
# print(df[["Name","Height","Weight"]].to_string()) # we pass list of items we want to display, and it must be within a subscript operator

#SELECTION BY ROW/s
print(df.loc[0])
print(df.loc[1])

# we can select and print row by writing name also
df2 = pd.read_csv("pandas\data.csv",index_col="Name")
print(df2.loc["Pikachu"])
# if we dont want all the output of the row then we can select perticulur column of that row
print(df2.loc["Charizard",["Height","Weight"]])

# integer based indexing
print(df2.iloc[0:11:2, 0:3])
# 0:11:2 is for row selection and 0:3 is for column selection 