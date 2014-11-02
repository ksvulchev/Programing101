from orc import Orc
from  hero import Hero
from weapons import Weapon
import random

class Fight:
	def __init__(self, orc, hero):
		self.orc = orc 
		self.hero = hero
	def equip_weapons(self):

		self.hero.equip_weapon(Weapon("Axe", 20, 0.2))
	def flip_coin(self):
		if random.random() > 0.5:
			return self.hero
		else: 
			return self.orc

	def simulate_fight(self):
		attacker = self.flip_coin()
		
		if attacker == self.hero:
			attacked = self.orc
		else:
			attacked = self.hero

		while self.orc.is_alive() and self.hero.is_alive():
			attacked.take_damage(attacker.attack())
			print("{} hit {} with {} dmg. {} has {} life left".format(attacker.name, attacked.name, attacker.attack(), attacked.name, attacked.health))
			attacker, attacked = attacked, attacker

first_fight = Fight(Orc("Gorlag", 100, 3),Hero("Bron", 100, "DragonSlayer"))
first_fight.equip_weapons();
first_fight.simulate_fight()
