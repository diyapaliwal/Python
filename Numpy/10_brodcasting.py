import numpy as np

# Broadcasting in NumPy = when you do math on arrays of different shapes, NumPy automatically stretches (broadcasts) the smaller one so shapes match.

import numpy as np

a = np.array([1,2,3])
b = 5
print(a + b)   
# [6,7,8]
# Here 5 is “broadcast” to [5,5,5].

a = np.array([1,2,3,4]) 
b = np.array([[5],[6],[7],[8]])
print()   
print(a.shape)
print(b.shape)
print(a+b)
print(a*b)
# From the right, every dimension pair must be either equal or 1. If not → error.

'''Broadcasting works if:

Compare shapes from right → left.

At each dimension:

Sizes are equal, OR

One of them is 1.

If array has fewer dimensions → NumPy pads with 1s on the left.

Result shape = take the maximum size along each dimension.'''
