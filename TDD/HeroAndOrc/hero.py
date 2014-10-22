class Hero:

	def __init__(self, name, health, nickname):
		self._MAX_HEALTH = health # this is constant
		self.name = name
		self.health = health
		self.nickname = nickname

	def known_as(self):
		return "{} the {}".format(self.name, self.nickname)

	def get_health(self):
		return self.health

	def is_alive(self):
		if self.get_health() <= 0:
			return False
		else:
			return True
	def take_damage(self, damage):

		#self.health -= damage
		#if self.health < 0:
		#	self.health = 0
		#return self.health

		# dolnoto e ot primera na duskata  V
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

