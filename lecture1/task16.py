#!/usr/bin/python
def is_increasing(seq):

	for i in range(1,len(seq)):
		if seq[i] <= seq[i-1]:
			return False

	return True
print (is_increasing([1,2,3,4,5]))
print (is_increasing([1]))
print (is_increasing([5,6,-10]))
print (is_increasing([1,1,1,1]))