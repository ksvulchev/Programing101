class Orc:

	def __init__(self, name, health, berserk_factor):
		self._MAX_HEALTH = health # this is constant
		self.name = name
		self.health = health
		self.__set_berserk_factor(berserk_factor)

	def __set_berserk_factor(self, berserk_factor):
		if berserk_factor > 1 and berserk_factor < 2:
			self.berserk_factor = berserk_factor
		else:
			raise ValueError


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