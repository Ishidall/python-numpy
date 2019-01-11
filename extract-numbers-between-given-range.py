## Extract all numbers between a given range from a numpy array

import numpy as np

arr1 = np.array([2, 6, 1, 9, 10, 3, 27])

extractedIndices = np.where((arr1 <= 10) & (arr1 >= 5))

extracted = arr1[extractedIndices]

print(extracted)

## other solution1

indices1 = np.where(np.logical_and(arr1 >= 5, arr1 <= 10))

print(arr1[indices1])

## other solution2

print(arr1[(arr1 >= 5) & (arr1 <= 10)])

## other solution3

print(arr1[np.logical_and(arr1 >= 5, arr1 <= 10)])
