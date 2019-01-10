## Stack two arrays vertically

import numpy as np

arr1 = np.arange(10).reshape(2, -1)
arr2 = np.repeat(11, 10).reshape(2, -1)

print(arr1)
print(arr2)

appendedArr = np.append(arr1, arr2, axis=0)

print(appendedArr)

## other solution1

appendedArr1 = np.concatenate([arr1, arr2], axis=0)

print(appendedArr1)

## other solution2

appendedArr2 = np.vstack([arr1, arr2])

print(appendedArr2)

## other solution3

appendedArr3 = np.r_[arr1, arr2]

print(appendedArr3)
