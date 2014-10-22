from weapons import Weapon

class Entity:

	def __init__(self, name, health):
		self._MAX_HEALTH = health # this is constant
		self.name = name
		self.health = health
		self.equiped_weapon = []

	def get_health(self):
		return self.health

	def is_alive(self):
		if self.get_health() <= 0:
			return False
		else:
			return True

	def take_damage(self, damage):
		if damage > self.health:
			self.health = 0
		else:
			self.health -= damage

	def take_healing(self, healing_points):	
		if self.is_alive() and self.health < self._MAX_HEALTH:
			if self.health + healing_points > self._MAX_HEALTH:
				self.health = self._MAX_HEALTH
			else:
				self.health += healing_points
			return True			
		else: 
			return False

	def has_weapon(self):
		if len(self.equiped_weapon) < 1:
			return False
		else:
			return True
	def equip_weapon(self, weapon):
		self.equiped_weapon = weapon

	def attack(self):
		if self.has_weapon():
			return self.equiped_weapon[1]
		else:
			return 0

# tyka trqq da e weapon