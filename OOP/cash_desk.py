class CashDesk(object):
	def __init__(self):
		self.money = {100:0, 50:0, 20:0, 10:0, 5:0, 2:0, 1:0}
	def take_money(self, money):
		for i in money:
			self.money[i] += money[i]
		print(self.money)
	def total(self):
		total = 0 
		for i in self.money:
			total += self.money[i] * i 
		return total

cash = CashDesk()
cash.take_money({1:2, 50:1, 20:1})
print (cash.total())