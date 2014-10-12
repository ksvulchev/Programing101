#!/usr/bin/python
def unique_words_count(arr):
	uniqe_arr = set(arr)
	return len(uniqe_arr)

print (unique_words_count(["apple", "banana", "apple", "pie"]))
print (unique_words_count(["python", "python", "python", "ruby"]))
print (unique_words_count(["HELLO!"] * 10))