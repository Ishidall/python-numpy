## Get the positions where elements of two arrays match

import numpy as np

arr1 = np.array([1,2,3,2,3,4,3,4,5,6])
arr2 = np.array([7,2,10,2,7,4,9,4,9,8])

commonIndices = np.in1d(arr1, arr2).nonzero()

print(commonIndices)

## other solution

commonIndices2 = np.where(arr1 == arr2)

print(commonIndices2)
