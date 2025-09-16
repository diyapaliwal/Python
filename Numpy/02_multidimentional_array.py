import numpy as np

# 0 Dimensional Array
array0 = np.array("A")
print(array0)
print(array0.ndim)
print(array0.shape)

# 1D Array
array1 = np.array([1,2,3])
print(array1)
print(array1.ndim)
print(array1.shape)

# 2D array
array2 = np.array([[1,2,3],["a","b","c"],["!","@","#"]])
print(array2)
print(array2.ndim)
print(array2.shape)

# 3D array
array3 = np.array([[[1,2,3],["a","b","c"],["!","@","#"]],
                   [[1,2,3],["a","b","c"],["!","@","#"]],
                   [[1,2,3],["a","b","c"],["!","@","#"]]])
print(array3)
print(array3.ndim)
print(array3.shape)

word = array3[0,0,2]+array3[2,2,2]+array2[1,1]
print(word)