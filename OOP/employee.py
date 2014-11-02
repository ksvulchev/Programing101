class Employee:
	def __init__(self, last_name, first_name):
		self.last_name = last_name
		self.first_name = first_name
	def get_name(self):
		return "{} {}".format(self.first_name, self.last_name)

class HourlyEmployee(Employee):
	def __init__(self, last_name, first_name, hourly_wage):
		super().__init__(last_name, first_name)
		self.hourly_wage = hourly_wage

	def weekly_pay(self, hours):
		if hours > 40:
			return (hours - 40 * self.hourly_wage * 1.5) + 40 * self.hourly_wage
		else:
			return hours * self.hourly_wage

class SalariedEmployee(Employee):
	def __init__(self, last_name, first_name, annual_salary):
		super.__init__(last_name, first_name)
		self.annual_salary = annual_salary

	def weekly_pay(self, hours):
		return self.annual_salary / 52

class Manager(SalariedEmployee):
	def __init__(self, last_name, first_name, annual_salary, weekly_bonus):
		super.__init__(last_name, first_name, annual_salary)
		self.weekly_bonus = weekly_bonus

	def weekly_pay(self):
		return annual_salary / 52 + self.weekly_bonus						