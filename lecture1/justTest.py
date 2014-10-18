def prepare_meal(number):
	meal = ""
	while (number % 3 == 0 ):
		number /= 3
		meal = meal + "spam "
		if number % 3 != 0 and number % 5 == 0:
			meal = meal + "and "
	while (number % 5 == 0 ):
		number /= 5
		meal = meal + "eggs "
	return meal
print (prepare_meal(5))
print (prepare_meal(3))
print (prepare_meal(27))
print (prepare_meal(15))
print (prepare_meal(2251))
print (prepare_meal(7))