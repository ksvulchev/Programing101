#!/usr/bin/python
def count_consonants(string):
	string = string.lower()
	count = 0 
	letter = "bcdfghjklmnpqrstvwxz"
	vowels = []
	for i in letter:
		vowels.append(i)


	for i in vowels:
		if i in string:
			print (i)
		count += string.count(i)

	return count
print (count_consonants("Github is the second best thing that happend to programmers, after the keyboard!"))	