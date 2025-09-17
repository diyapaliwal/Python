import numpy as np
rn = np.random.default_rng(seed = 1)

print(rn.integers(low = 1, high = 101, size = (3,2)))

# seed makes output permanent for every interpritation following the 1st one