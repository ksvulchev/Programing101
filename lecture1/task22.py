#!/usr/bin/python
def nan_expand(n):

	text = ""

	while (n):
		text += "Not a "
		n = n - 1

	if "Not a" in text:
		text += "NaN"

	return text

print (nan_expand(3))
