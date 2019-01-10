## Create boolean array

import numpy as np

boolArr = np.array([
	[True, True, True],
	[True, True, True],
	[True, True, True]
])

print(boolArr)

## other solution

l = []

for i in range(3):
	l.append([True, True, True])

boolArr2 = np.array(l)

print(boolArr2)

## other solution2

l1 = []

for i in range(3):
	boolList = []

	for j in range(3):
		boolList.append(True)

	l1.append(boolList)

boolArr3 = np.array(l1)

print(boolArr3)

## other solution3

boolArr4 = np.full((3, 3), True, dtype=bool)

print(boolArr4)

## other solution4

boolArr5 = np.ones((3, 3), dtype=bool)

print(boolArr5)

## other solution5

boolArr6 = np.full((3, 3), True)

print(boolArr6)