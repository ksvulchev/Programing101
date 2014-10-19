def nth_fibonacci(n):

	fib = [1,1]

	for i in range(2,n):
		next = fib[i - 1] + fib[i - 2]
		fib.append(next)

	return fib[n - 1]

print(nth_fibonacci(9))