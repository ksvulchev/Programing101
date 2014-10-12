#!/usr/bin/python
def number_to_list(n):
	arr = []
	while (n):
	 	modul = n % 10
	 	arr.insert(0, modul)
	 	n = n // 10
	return arr

print (number_to_list(123))
print (number_to_list(99999))