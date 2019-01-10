## Convert 1D array into 2D

import numpy as np

arr = np.arange(10)

newArr = np.reshape(arr, (2, 5))

print(arr)
print(newArr)

## other solution

newArr1 = np.reshape(arr, (2, -1))

print(newArr1)
