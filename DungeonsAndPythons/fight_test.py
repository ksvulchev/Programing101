import fight_new
from orc import Orc
from  hero import Hero
from  weapons import Weapon
import unittest

class FightTest(unittest.TestCase):
	def setUp(self):
		self.orc = Orc("Gorlag", 100, 3) # ili self.orc_one
		self.hero = Hero("Bron", 100, "DragonSlayer") # ili self.hero_one
		self.fight = fight_new.Fight(self.orc,self.hero) # ili self.fight_one
		self.axe = Weapon("Axe", 20, 0.2)
		self.sword = Weapon("Sword", 12, 0.7)
		self.hero.equiped_weapon = self.sword
		self.orc.equiped_weapon = self.axe # izpozlvame self.hero.weapon za da ne zavisi testa ni ot drygiq test za weapon eqiped

	def test_orc_init(self):
		self.assertTrue(isinstance(self.fight.orc, Orc))
		self.assertEqual(self.fight.orc.name, "Gorlag")
		self.assertEqual(self.fight.orc, self.orc)

	def test_hero_init(self):
		self.assertTrue(isinstance(self.fight.hero, Hero))
		self.assertEqual(self.fight.hero.name, "Bron")
		self.assertEqual(self.fight.hero.nickname, "DragonSlayer")
		self.assertEqual(self.fight.hero, self.hero)

	def test_attack_first(self):
		result = []
		for x in range(10):
			result.append(self.fight.flip_coin())
		self.assertTrue(self.hero in result)
		self.assertTrue(self.orc in result)

	def test_simulate_fight_(self):
		self.orc.health = 0
		self.assertTrue(self.orc.is_alive() or self.hero.is_alive())

	def test_fight(self):
		self.fight.simulate_fight()
		self.assertFalse(self.orc.is_alive() and self.hero.is_alive())

	def test_fight_with_no_weapons(self):
		self.orc.equiped_weapon = None

		self.fight.simulate_fight()
		self.assertFalse(self.orc.is_alive())

if __name__ == '__main__':
	unittest.main()











#kogato ima self. e za celiq klas ako nqma self. pred promenlivata tq se izpolzva samo v konkretniq metod