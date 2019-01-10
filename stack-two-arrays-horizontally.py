## Stack two arrays horizontally

import numpy as np

arr1 = np.arange(10).reshape(2, -1)
arr2 = np.repeat(11, 10).reshape(2, -1)

newArr = np.concatenate([arr1, arr2], axis=1)

print(newArr)

## other solution1

newArr = np.hstack([arr1, arr2])

print(newArr)

## other solution2

newArr = np.append(arr1, arr2, axis=1)

print(newArr)

## other solution3

newArr = np.c_[arr1, arr2]

print(newArr)
