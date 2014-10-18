def member_of_nth_fib_lists(listA, listB, needle):
	fib = []
	fib = listA + listB
	while len(fib) < len(needle):
		listA = listB
		listB = fib
		fib = listA + listB

	if len(fib) != len(needle):
		return False
	else:
		for i in range(len(fib)):
			if fib[i] != needle[i]:
				return False

	return True

print(member_of_nth_fib_lists([7,11], [2], [11,7,2,2,7]))