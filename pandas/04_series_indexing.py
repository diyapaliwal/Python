import pandas as pd

data = [100,200,300]
print(pd.Series(data,index=("a","b","c")))
# default indexing starts with 0