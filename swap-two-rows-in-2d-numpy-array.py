## Swap 2 rows in a 2D numpy array

import numpy as np

arr = np.arange(9).reshape(3,3)

print(arr[[1, 0, 2], :])
