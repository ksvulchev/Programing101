#!/usr/bin/python
def is_prime(n):
    for i in range(2, n+1):
    	if n == i:
            return True

    	if n % i == 0:
    		return False
    return False

def goldbach(n):
	arr = []
	for i in range(2,n):
		if is_prime(i):
			diff = n - i

			if is_prime(diff):
				pair = (i, diff)
					
				arr.append(pair)
	arr = arr[:int(len(arr)/2)]
	return arr

print (goldbach(100))

