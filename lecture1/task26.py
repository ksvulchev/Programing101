#!/usr/bin/python
""" 
3.21  - 4.20
4.21  - 5.21
5.22  - 6.21
6.22  - 7.22
7.23  - 8.22
8.23  - 9.23
9.24  - 10.23
10.24 - 11.22
11.23 - 12.21
12.22 - 1.20
1.21  - 2.19
2.20  - 3.20 
"""

def what_is_my_sign(day, month):
	arr = [
			["Aries",  		3.21,   4.20],
			["Taurus", 		4.21,   5.21],
			["Gemini", 		5.22,   6.21],
			["Cancer", 		6.22,   7.22],
			["Leo",    		7.23,   8.22],
			["Virgo",  		8.23,   9.23],
			["Libra",  		9.24,  10.23],
			["Scorpio", 	10.24, 11.22],
			["Sagittarius", 11.23, 12.21],
			["Capricorn", 	12.22,  1.20],
			["Aquarius", 	1.21,   2.19],
			["Pisces", 		2.20,   3.20],

		  ]
	num = month + (day / 100.0)

	for i in arr:
		if num >= i[1] and num <= i[2]:
			return i[0]

print (what_is_my_sign(8, 2))