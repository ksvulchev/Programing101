
class Product:
	def __init__(self, name, stock_price, final_price):
		self.name = name
		self.stock_price = stock_price
		self.final_price = final_price

	def profit(self):
		self.profita = self.final_price - self.stock_price
		return self.profita #IMMPORTANT AKO self.profita e self.profit 
							#nqma da raboti programata sled purvoto izvinkvane v sell.product
							#zashtoto shte se overritne metoda profit() i shte stane promenlivata
							# profit LOOKUP __str__ metoda na klasa

class Laptop(Product):

	def __init__ (self, name, stock_price, final_price, diskspace, ram):
		super().__init__(name, stock_price, final_price)
		self.diskspace = diskspace
		self.ram = ram



class Smartphone(Product):

	def __init__ (self, name, stock_price, final_price, display_size, mega_pixels):
		super().__init__(name, stock_price, final_price)
		self.display_size = display_size
		self.mega_pixels = mega_pixels



class Store:
	income = 0

	def __init__(self, name):
		self.name = name
		self.products = {}

	def load_new_products (self, producta, count):
		self.products[producta] = count
	def list_products (self, product_class):
		self.product_class = product_class
		for k,v in self.products.items():
			if isinstance(k,self.product_class):
				print (k.name , v)
	def sell_product (self, product):

		if self.products[product] > 0:
			self.products[product] = self.products[product] - 1
			Store.income += product.profit()
			return True


		else:
			return False
	def total_income(self):
		return Store.income






#store = Store('Laptop.bg')
#smarthphone = Smartphone('Hack Phone', 500, 820, 7, 10)
#store.load_new_products(smarthphone, 2)
#store.sell_product(smarthphone) 
#store.sell_product(smarthphone) 
#store.sell_product(smarthphone) 

#print(store.total_income())
