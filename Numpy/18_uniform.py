import numpy as np
nr = np.random.default_rng(seed = 1)
print(nr.uniform(low=-1, high=1, size=(3,2)), "\n")
print(np.random.uniform(low=-1, high=1, size=(3,2)))
# uniform is used to get float value and -ve values

#another hack
np.random.seed(seed = 1)

print(np.random.uniform(low=-1, high=1, size=(3,2)))