from laptop_bg import Product,Store # importvame si faila koito testvame
import unittest

class ProductTest(unittest.TestCase):

	def test_product_profit(self):
		new_product = Product('Hack Phone', 500, 600)
		self.assertEqual(100, new_product.profit())
	def test_total_store_profit(self):
		store = Store('Laptop.bg')
		new_product = Product('Hack Phone', 500, 600)
		store.load_new_products(new_product, 4)
		for i in range(4):						#for easy testing - easy increase of selled products
			store.sell_product(new_product) 
		
		self.assertEqual(400, store.total_income())
	def test_new_product_is_loaded(self):
		new_product = Product('Hack Phone', 500, 600)
		store = Store('Laptop.bg')
		store.load_new_products(new_product, 2)
		dic = store.products
		self.assertTrue(dic.keys('Hack Phone'))


if __name__ == '__main__':
	unittest.main()
