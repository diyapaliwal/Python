import numpy as np
ages = np.array([[12,45,67,12,22,39,3],
                [3,56,45,98,13,66,77]])

mature = np.where(ages>=18,ages,0)
# mature = np.where(conditions, array, replace)
print(mature)