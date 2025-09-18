import pandas as pd
# DataFrame = A tabular data structure with rows and columns. (2 Dimensional) similar to an excel spreadsheet

data = {"Name": ["Spongebob","Patrick","Squidward"],
        "Age":[30,35,50]}

df = pd.DataFrame(data) # DataFrame is a constructor
print(df,"\n")

df2 = pd.DataFrame(data, index= ["Employee 1","Employee 2","Employee 3"])
print(df2)
print(df2.loc["Employee 1"])
# or
print(df2.iloc[0])