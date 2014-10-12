	#!/usr/bin/python
def contains_digits(number, digits):
	number = str(number)
	for i in range(len(digits)): 
		dig = str(digits[i])
		if dig not in number:
 			return False

	return True
print (contains_digits(402123, [0, 3, 4]))
print (contains_digits(666, [6,4]))
print (contains_digits(123456789, [1,2,3,0]))
print (contains_digits(456, []))