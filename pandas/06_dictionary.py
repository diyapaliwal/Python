import pandas as pd

calories = {"Day 1": 1750,
            "Day 2": 2100,
            "Day 3": 5432}

series = pd.Series(calories)
print(series.loc["Day 3"],"\n") # indexing done by keys. no numeric indexing is done we can locate them only by keys

series2 = pd.Series(calories)
series2.loc["Day 3"] += 500
print(series2,"\n")

print(series2[series2 >= 2000])