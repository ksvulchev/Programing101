import sqlite3

#conn = sqlite3.connect("mydb")
#conn.row_factory = sqlite3.Row 

#cursor = conn.cursor()

#result = cursor.execute("SELECT id, name, position FROM company")

#for row in result:
	#print(row['position'])
def open_connection(database):
    conn = sqlite3.connect(database)
    return conn

def list_employees(conn):
	cursor = conn.cursor()
	employees = "SELECT id, name, position FROM company"
	for person in cursor.execute(employees):
		print (person) 

def monthly_spending(conn):
	cursor = conn.cursor()
	total = 0
	employee_salary = "SELECT monthly_salary FROM company" 
	for salary in cursor.execute(employee_salary):
		total += salary[0]
	return total

def yearly_spending(conn):
	cursor = conn.cursor()
	year_bonus = 0
	employee_bonus = "SELECT yearly_bonus FROM company"
	for bonus in cursor.execute(employee_bonus):
		year_bonus += bonus[0]

	year_total = year_bonus + (12 * monthly_spending(conn))
	print (year_total)

def add_employee(conn):
	cursor = conn.cursor()
	name = input('name: ')
	monthly_salary = int(input('monthly_salary: '))
	yearly_bonus = int(input('yearly_bonus: '))
	position = input('position: ')
	cursor.execute('''INSERT INTO company(name, monthly_salary, yearly_bonus, position)
					VALUES(?,?,?,?)''', (name, monthly_salary, yearly_bonus, position))
	
	conn.commit()

def delete_employee(conn, index):
	cursor = conn.cursor()
	cursor.execute("DELETE FROM company WHERE id = ? ", (index,))
	conn.commit()

def update_employee(conn, index):
	cursor = conn.cursor()
	name = input('name: ')
	monthly_salary = int(input('monthly_salary: '))
	yearly_bonus = int(input('yearly_bonus: '))
	position = input('position: ')
	cursor.execute('''UPDATE company SET name = ?, monthly_salary = ?,
			yearly_bonus = ?, position = ? WHERE id = ? ''', 
			(name, monthly_salary, yearly_bonus, position, index))
	
	conn.commit()

def main():
	conn = open_connection('mydb')

	
	list_employees(conn)
	print(monthly_spending(conn))
	yearly_spending(conn)
	#add_employee(conn)
	#list_employees(conn)
	#delete_employee(conn, 3)
	#list_employees(conn)
	#update_employee(conn,1)

if __name__ == '__main__':
    main()

#monthly_spending()
#yearly_spending()
#add_employee()
#list_employees()
#delete_employee(3)
#list_employees()
#update_employee(1)


# srqda relacii m/y bazi danni
# ORM
# sum direktno v SQL
# dependancy injection


#python script that loads inital data - decapling