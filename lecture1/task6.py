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

print (is_int_palindrome(1))
print (is_int_palindrome(42))
print (is_int_palindrome(100001))
print (is_int_palindrome(999))
print (is_int_palindrome(123))