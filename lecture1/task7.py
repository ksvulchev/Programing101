#!/usr/bin/python
def contains_digit(number, digit):
	number = str(number)
	digit = str(digit)
	if digit in number:
		return True
	else:
		return False

print (contains_digit(123, 4))
print (contains_digit(42, 2))
print (contains_digit(1000, 0))
print (contains_digit(12346789, 5))