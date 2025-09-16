import numpy as np

# vectorized math funcs
array = np.array([4,9,16])
print(np.sqrt(array).astype(int))
print(np.sqrt(array),"\n")

array2 = np.array([1.01,2.50,2.51,3.99])
print(np.sqrt(array2))
print(np.round(array2))
print(np.ceil(array2))
print(np.floor(array2))
print(np.pi*array2)
