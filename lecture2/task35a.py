def nth_fib_lists(listA, listB, n):
	fib = []
	fib.append(listA)
	fib.append(listB)
	while len(fib) <= n:
		next = listA + listB

		fib.append(next)

		listA = listB
		listB = next
	return fib[n-1]

print (nth_fib_lists([], [], 100))

