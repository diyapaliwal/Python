import numpy as np
rng = np.random.default_rng()
print(rng.integers(1,7))
print(rng.integers(low =1,high =7)) # can akso use keywords
print(rng.integers(low = 1, high = 101, size = 3))
print(rng.integers(low = 1, high = 101, size = (3,2)))