import pandas as pd

data = [100,300,234]

series = pd.Series(data)
print(series.loc[2])

series = pd.Series(data,index= ("a","b","c"))
print(series.loc["b"])

s = pd.Series(data,index= ("a","b","c"))
print(series.iloc[0])
# we use loc to print the value at that location
# and iloc is used for integer location like iloc[0] useful when indexing is done manally and its not default
data2 = [100,256,556,765,875]
s = pd.Series(data2)
print(s[s > 500])