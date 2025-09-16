import numpy as np

array = np.array([[1,2,3,4],
                  [5,6,7,8],
                  [9,10,11,12],
                  [13,14,15,16]])

# column slicing 

print(array[:, 0], "\n")
print(array[:, -2], "\n")
print(array[2:, 0], "\n")
print(array[1:3, :3], "\n")
print(array[1:3:2, ::2], "\n")
print(array[1:3:2, 1::2], "\n")