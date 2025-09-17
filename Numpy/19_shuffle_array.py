import numpy as np
rng = np.random.default_rng()

fruits = np.array(["apple", "orange", "banana", "coconut", "pineapple"])
rng.shuffle(fruits)
print(fruits)