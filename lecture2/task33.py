#!/usr/bin/python
from fractions import Fraction
def simplify_fraction(frac):
	num_one = frac[0]
	num_two = frac[1]
	for i in range(2,frac[0]+1):
		while (num_one % i == 0 and num_two % i == 0):
			num_one /= i
			num_two /= i

	return (num_one, num_two)
print (simplify_fraction((63,462)))
