from weapons import Weapon

class Entity:

	def __init__(self, name, health):
		self._MAX_HEALTH = health # this is constant
		self.name = name
		self.health = health
		self.equiped_weapon = None

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
		if self.equiped_weapon is not None:
			return True
		return False

	def equip_weapon(self, weapon):
		self.equiped_weapon = weapon

	def attack(self): #Should be  Replaced
		if self.equiped_weapon is None:
			return 0
		else:
			return self.equiped_weapon.damage

# tyka trqq da e weapon