import pandas as pd

data = [100,200,300]
data2 = ["A","B","C"]
data3 = [True,False,True]
print(pd.Series(data))
print(pd.Series(data2))
print(pd.Series(data3))

'''data is a Python list ([100,200,300]).
When you do pd.Series(data), it becomes a Pandas Series.
A Series = 1D array + labels (index).
By default, index = 0,1,2.
So after conversion:
100 is at index 0
200 is at index 1
300 is at index 2'''