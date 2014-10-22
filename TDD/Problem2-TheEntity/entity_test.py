import entity
import unittest

class EntityTests(unittest.TestCase):

	def setUp(self):
		self.entity_char = entity.Entity("Gorlag", 100)



	def test_hero_init(self):
		self.assertEqual(self.entity_char.name, 'Gorlag')
		self.assertEqual(self.entity_char.health, 100)


	def test_get_health(self):
		self.assertEqual(self.entity_char.get_health(), 100)

	def test_is_orc_alive(self):
		self.assertTrue(self.entity_char.is_alive())
		self.entity_char.health = 0
		self.assertFalse(self.entity_char.is_alive())

	def test_get_damage_int(self):
		self.entity_char.take_damage(30)
		self.assertEqual(self.entity_char.health, 70)

	def test_get_damage_float(self):
		self.entity_char.take_damage(1.5)
		self.assertEqual(self.entity_char.health, 98.5)

	def test_get_more_damage(self):
		self.entity_char.take_damage(200)
		self.assertEqual(self.entity_char.health, 0)

	def test_take_healing_if_dead(self):
		self.entity_char.health = 0
		self.assertEqual(self.entity_char.take_healing(50), False)

	def test_take_healing_with_max_health(self):
		self.entity_char.health = 100
		self.assertEqual(self.entity_char.take_healing(50), False)

	def test_take_healing_above_max_health(self):	
		self.entity_char.health = 60
		self.assertEqual(self.entity_char.take_healing(50), True)
		self.assertEqual(self.entity_char.health, 100)
		
	def test_take_healing(self):	
		self.entity_char.health = 60
		heal = self.entity_char.take_healing(30)
		self.assertEqual(self.entity_char.health, 90)

	def test_has_weapon(self):
		self.assertFalse(self.entity_char.has_weapon())

	def test_equip_weapon(self):
		weapon = ["Axe", 100, 0.2]
		self.entity_char.equip_weapon(weapon)
		self.assertTrue(len(self.entity_char.equiped_weapon) == 3)

	def test_discard_old_weapon(self):
		#The OLD weapon
		weapon = ["Axe", 100, 0.2]
		self.entity_char.equip_weapon(weapon)
		#self.assertTrue(self.entity_char.equiped_weapon[0] == "Sword") #will return false

		#The NEW weapon
		new_weapon = ["Sword", 100, 0.2]
		self.entity_char.equip_weapon(new_weapon)
		self.assertTrue(self.entity_char.equiped_weapon[0] == "Sword")
		
	def test_attack_equiped_weapon(self):
		new_weapon = ["Sword", 100, 0.2]
		self.entity_char.equip_weapon(new_weapon)
		self.assertEqual(self.entity_char.attack(), 100)

	def test_attack_no_weapon(self):
		self.assertEqual(self.entity_char.attack(), 0)





if __name__ == '__main__':
	unittest.main()