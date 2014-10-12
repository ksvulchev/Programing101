#!/usr/bin/python
def count_vowels(string):
	string = string.lower()
	count = 0 
	letter = 'aeiouy'
	vowels = []
	for i in letter:
		vowels.append(i)


	for i in vowels:
		count += string.count(i)

	return count
print (count_vowels("Github is the second best thing that happend to programmers, after the keyboard!"))	