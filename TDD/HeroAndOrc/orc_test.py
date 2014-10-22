import orc
import unittest

class OrcTests(unittest.TestCase):
	def setUp(self):
		self.enemy_orc = orc.Orc("Gorlag", 100, 1.5)

	def test_hero_init(self):
		self.assertEqual(self.enemy_orc.name, 'Gorlag')
		self.assertEqual(self.enemy_orc.health, 100)
		self.assertEqual(self.enemy_orc.berserk_factor, 1.5)

	def test_get_health(self):
		self.assertEqual(self.enemy_orc.get_health(), 100)

	def test_is_orc_alive(self):
		self.assertTrue(self.enemy_orc.is_alive())
		self.enemy_orc.health = 0
		self.assertFalse(self.enemy_orc.is_alive())

	def test_get_damage_int(self):
		self.enemy_orc.take_damage(30)
		self.assertEqual(self.enemy_orc.health, 70)

	def test_get_damage_float(self):
		self.enemy_orc.take_damage(1.5)
		self.assertEqual(self.enemy_orc.health, 98.5)

	def test_get_more_damage(self):
		self.enemy_orc.take_damage(200)
		self.assertEqual(self.enemy_orc.health, 0)

	def test_take_healing_if_dead(self):
		self.enemy_orc.health = 0
		self.assertEqual(self.enemy_orc.take_healing(50), False)

	def test_take_healing_with_max_health(self):
		self.enemy_orc.health = 100
		self.assertEqual(self.enemy_orc.take_healing(50), False)

	def test_take_healing_above_max_health(self):	
		self.enemy_orc.health = 60
		self.assertEqual(self.enemy_orc.take_healing(50), True)
		self.assertEqual(self.enemy_orc.health, 100)
		
	def test_take_healing(self):	
		self.enemy_orc.health = 60
		heal = self.enemy_orc.take_healing(30)
		self.assertEqual(self.enemy_orc.health, 90)

if __name__ == '__main__':
	unittest.main()