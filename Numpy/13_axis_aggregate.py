import numpy as np

# Aggregate functions = summarize data and typically return a single value
array = np.array([[1,2,3,4,5],[6,7,8,9,10]])

print(np.sum(array,axis=0))
print(np.sum(array,axis=1))