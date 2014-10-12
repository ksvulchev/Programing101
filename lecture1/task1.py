#!/usr/bin/python
def sum_of_digits(n):
	sum = 0

	while (n):
		modul = n%10
		sum = modul + sum
		n = n//10
	return sum

print (sum_of_digits(1325132435356))
