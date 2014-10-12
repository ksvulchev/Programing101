#!/usr/bin/python
def list_to_number(digits):
	num = 0 

	for i in digits:
		num *= 10
		num += i
		
	return num
print (list_to_number([1,2,3]))
print (list_to_number([9,9,9,9,9]))	