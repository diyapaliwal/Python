import numpy as np
rng = np.random.default_rng()

fruits = np.array(["apple", "orange", "banana", "coconut", "pineapple"])
emoji = np.array(["🍎","🍌","🍍","🥥","🍊"])
fruits= rng.choice(fruits, size=(3))
print(fruits)
emoji= rng.choice(emoji, size=(3,3))
print(emoji)