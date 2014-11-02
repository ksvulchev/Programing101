import random
class Weapon:

	def __init__(self, name, damage, critical_strike_percent):

		self.name = name
		self.damage = damage
		self.critical_strike_percent = critical_strike_percent

	def critical_hit(self): 

		if random.random() > self.critical_strike_percent:
			return False
		else: 
			return True

