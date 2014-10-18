#!/usr/bin/python
def groupby(func, seq):

	dictonary = {}
	for i in seq:
		key = func(i)

		if key in dictonary:
			dictonary[key].append(i)
		else:
			dictonary[key] = [i]
	return dictonary

print(groupby(lambda x: x % 3, [0, 1, 2, 3, 4, 5, 6, 7]))

