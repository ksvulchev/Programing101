#!/usr/bin/python
def sum_of_int(num):
	suma = 0
	while(num):
		modul = num % 10
		num = num // 10
		suma += modul
	return suma
def is_number_balanced(n):
	string  = str(n)
	length = len(string)
	if length % 2 == 0:
		left_side = int(string[ : length//2])
		rigth_side = int(string[length//2 : ])
	else:
		left_side = int(string[ : length//2])
		rigth_side = int(string[(length//2)+1 : ])

	if sum_of_int(left_side) == sum_of_int(rigth_side):
		return True
	else:
		return False
print(is_number_balanced(122))