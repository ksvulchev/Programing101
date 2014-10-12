#!/usr/bin/python
def prime_factorization(n):
	prime = {}
	for i in range(2,n+1):
		count = 0

		if n % i == 0:
			while(n % i == 0):
				n /= i
				count = count + 1
			prime[i] = count
	return prime
print (prime_factorization(356))
