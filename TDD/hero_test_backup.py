import hero
import unittest

class HeroTests(unittest.TestCase):
	def setUp(self):
		self.bron_hero = hero.Hero("Bron", 100, "DragonSlayer")

	def test_hero_init(self):
		self.assertEqual(self.bron_hero.name, 'Bron')
		self.assertEqual(self.bron_hero.health, 100)
		self.assertEqual(self.bron_hero.nickname, 'DragonSlayer')

	def test_hero_known_as(self):
		self.assertEqual(self.bron_hero.known_as(), "Bron the DragonSlayer")

	def test_get_health(self):
		self.assertEqual(self.bron_hero.get_health(), 100)

	def test_is_hero_alive(self):
		self.assertTrue(self.bron_hero.is_alive())
		self.bron_hero.health = 0
		self.assertFalse(self.bron_hero.is_alive())

	def test_get_damage_int(self):
		self.bron_hero.take_damage(30)
		self.assertEqual(self.bron_hero.health, 70)

	def test_get_damage_float(self):
		self.bron_hero.take_damage(1.5)
		self.assertEqual(self.bron_hero.health, 98.5)

	def test_get_more_damage(self):
		self.bron_hero.take_damage(200)
		self.assertEqual(self.bron_hero.health, 0)

	def test_take_healing_if_dead(self):
		self.bron_hero.health = 0
		self.assertEqual(self.bron_hero.take_healing(50), False)

	def test_take_healing_with_max_health(self):
		self.bron_hero.health = 100
		self.assertEqual(self.bron_hero.take_healing(50), False)

	def test_take_healing_above_max_health(self):	
		self.bron_hero.health = 60
		self.assertEqual(self.bron_hero.take_healing(50), True)
		self.assertEqual(self.bron_hero.health, 100)
		
	def test_take_healing(self):	
		self.bron_hero.health = 60
		heal = self.bron_hero.take_healing(30)
		self.assertEqual(self.bron_hero.health, 90)


if __name__ == '__main__':
	unittest.main()