## Remove from one array items that exist in another

import numpy as np

arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([5, 6, 7, 8, 9])

commonElems = np.setdiff1d(arr1, arr2)

print(commonElems)
