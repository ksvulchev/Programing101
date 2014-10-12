#!/usr/bin/python
def is_an_bn(word):
	length = len(word)
 
	if (length % 2 != 0):
		return False
	letter_a = word[:int(length / 2)+1]
	letter_b = word[int(length / 2):]

	if letter_a.count("a") == length/2 and letter_a.count("a") == letter_b.count("b"):
		return True
	else:
		return False
print (is_an_bn(""))
print (is_an_bn("rado"))
print (is_an_bn("aaabb"))
print (is_an_bn("aaabbb"))
print (is_an_bn("aabbaabb"))
print (is_an_bn("bbbaaa"))
print (is_an_bn("aaaaabbbbb"))