import numpy as np

# Aggregate functions = summarize data and typically return a single value
array = np.array([[1,2,3,4,5],[6,7,8,9,10]])

print(np.sum(array))
print(np.mean(array))
print(np.std(array))
print(np.var(array))
print(np.min(array))
print(np.max(array))
print(np.argmin(array)) # arg means argument and argmin shows the position of min argument
print(np.argmax(array))