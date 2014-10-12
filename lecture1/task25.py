#!/usr/bin/python
def calculate_coins(num):
	coins = [1,2,100,5,10,50,20]
	coins.sort()
	reverse = coins[::-1] 
	num *= 100
	coin = {}

	for i in reverse:
		count = 0

		while (i <= num):
			num = num - i
			count += 1
		coin[i] = count
	return coin
print (calculate_coins(8.94))