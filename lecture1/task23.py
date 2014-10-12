#!/usr/bin/python
def iterations_of_nan_expand(expanded):
	expanded = expanded.lstrip()	

	if not expanded:
		return expanded.count("Not a")
	if "Not a" not in expanded or "NaN" not in expanded:

		return False

	return expanded.count("Not a")

print (iterations_of_nan_expand("Not a Not a Not a Not a Not a Not a Not a Not a Not a Not a NaN"))