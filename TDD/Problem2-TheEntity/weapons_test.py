import weapons
import unittest

class WeaponTest(unittest.TestCase):

	def setUp(self):
		self.weapon = weapons.Weapon("Mighty Axe", 25, 0.2)

	def test_hero_init(self):
		self.assertEqual(self.weapon.name, 'Mighty Axe')
		self.assertEqual(self.weapon.damage, 25)
		self.assertEqual(self.weapon.critical_strike_percent, 0.2)

	def test_critical_hit(self): 						# needs fixing better test izvikai random 100 puti primerno 												
		critical = self.weapon.critical_hit(0.1)		# i proveri dali pone vednuj vrushta False i pone vednuj True
		self.assertFalse(critical)						# toest pogledni dolnata funkciq

	def test_weapon_crit(self):
		weapon = Weapon("Axe", 10, 0.5)
		result = []
		for x in range(1000):
			result.append(weapon.critical_hit())
		self.assertTrue(True in result)
		self.assertTrue(False in result)

if __name__ == '__main__':
	unittest.main()