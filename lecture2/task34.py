#!/usr/bin/python	
from fractions import Fraction

def sort_fractions(fractions):
	frac_arr = []
	for i in fractions:
		frac_arr.append(Fraction(str(i)))

	return frac_arr
print (sort_fractions([(2, 3), (1, 2)]))