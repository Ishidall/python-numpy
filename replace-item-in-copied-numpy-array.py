## Replace all odd numbers into -1 without affecting original array

import numpy as np

arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

copiedArr = arr.copy()

copiedArr[copiedArr % 2 == 1] = -1

print(arr)
print(copiedArr)

## other solution

arr1 = np.arange(10)

# if condition is True, element will be -1, otherwise, yield arr1
newArr = np.where(arr1 % 2 == 1, -1, arr1)

print(arr1)
print(newArr)
