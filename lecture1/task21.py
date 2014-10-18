#!/usr/bin/python

def is_int_palindrome(n):
	original = n
	palindrome = 0

	while (n):
		palindrome = palindrome * 10
		modul = n % 10
		n = n //10

		palindrome += modul

	if palindrome == original:
		return True
	else:
		return False

def next_hack(n):
	

	while (True):
		n += 1
		bin = "{0:b}".format(n)
		if bin.count("1") % 2 == 1 and is_int_palindrome(int(bin)):
			return n
		
print(next_hack(0))