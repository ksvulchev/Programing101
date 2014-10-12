#!/usr/bin/python
def count_words(arr):
	dic = {}

	for i in arr:
		counter = arr.count(i);
		dic[i] = counter

	return dic

print (count_words(["apple", "banana", "apple", "pie"]))
print (count_words(["python", "python", "python", "ruby"]))