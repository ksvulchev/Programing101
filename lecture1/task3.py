#!/usr/bin/python
def is_prime(n):
	for i in range(2, n+1):
		if n == i:
	  		return True

		elif n % i == 0:
			return False
	return False
	 
          




print (is_prime(5))
print (is_prime(15))
print (is_prime(2))
print (is_prime(14))