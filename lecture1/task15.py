#!/usr/bin/python
def biggest_difference(arr):
	biggest = arr[0]
	smallest = arr[0]

	for i in arr:
		if biggest < i:
			biggest = i
		if smallest > i:
			smallest = i

	return smallest - biggest
print (biggest_difference([1,2,3,4,5]))
print (biggest_difference(range(100)))