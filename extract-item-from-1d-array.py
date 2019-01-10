## Extract all odd numbers from array

import numpy as np

arr = np.arange(10)

extractedArr = arr[arr % 2 != 0]

print(extractedArr)