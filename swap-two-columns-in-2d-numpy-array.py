## Swap 2 columns in a 2D numpy array

import numpy as np

arr = np.arange(9).reshape(3, 3)

print(arr)

# arr[rows, indices]
print(arr[:, [1, 0, 2]])
