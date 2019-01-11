## Make a python function that handles scalars to work on numpy arrays

import numpy as np

def maxx(x, y):
	"""Get the maximum of two items"""
	if x >= y:
		return x
	else:
		return y

def pair_max(arr1, arr2):
	"""Compare two arrays and returns new array consists of max values on each index"""
	newArr = np.array([])

	comparison = (arr1 >= arr2)

	for i, elem in enumerate(comparison):
		if elem:
			newArr = np.append(newArr, arr1[i])
		else:
			newArr = np.append(newArr, arr2[i])

	return newArr


print(maxx(1, 5))

arr1 = np.array([5, 7, 9, 8, 6, 4, 5])
arr2 = np.array([6, 3, 4, 8, 9, 7, 1])

print(pair_max(arr1, arr2))

## other solution

pair_max2 = np.vectorize(maxx, otypes=[float])

print(pair_max2(arr1, arr2))
