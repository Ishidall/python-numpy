## Create a 2D array containing random floats between 5 and 10

import numpy as np

print(np.random.rand(5, 3) * 5 + 5)

## other solution1

rand_arr1 = np.random.randint(low=5, high=10, size=(5, 3)) + np.random.random((5, 3))

print(rand_arr1)

## other solution2

rand_arr2 = np.random.uniform(5, 10, size=(5, 3))

print(rand_arr2)
