import weapons
import unittest

class WeaponTest(unittest.TestCase):

	def setUp(self):
		self.weapon = weapons.Weapon("Mighty Axe", 25, 0.2)

	def test_hero_init(self):
		self.assertEqual(self.weapon.name, 'Mighty Axe')
		self.assertEqual(self.weapon.damage, 25)
		self.assertEqual(self.weapon.critical_strike_percent, 0.2)

	def test_weapon_crit(self):

		result = []
		for x in range(1000):
			result.append(self.weapon.critical_hit())
		self.assertTrue(True in result)
		self.assertTrue(False in result)

if __name__ == '__main__':
	unittest.main()