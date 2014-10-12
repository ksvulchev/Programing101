#!/usr/bin/python
def sum_matrix(m):
	sum = 0

	for i in m:
		for y in i:
			sum += y

	return sum
print (sum_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))