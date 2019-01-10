## generate custom sequences wout hardcoding

import numpy as np

arr = np.array([1, 2, 3])

print(arr)

newArr = np.r_[[arr[0]] * 3, [arr[1]] * 3, [arr[2]] * 3, arr, arr, arr]

print(newArr)

## better solution

newArr = np.r_[np.repeat(arr, 3), np.tile(arr, 3)]

print(newArr)
