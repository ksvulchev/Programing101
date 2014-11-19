import sqlite3

def parse_command(command):
	return tuple(command.split(" ")) # ---> what does this do

def is_command(command_tuple, command_string): # ---> and what does this do
	return command_tuple[0] == command_string

def open_connection(database):
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    return cursor

def list_employees(cursor):
	employees = "SELECT id, name, position FROM company"
	for person in cursor.execute(employees):
		print ("{} - {} - {}".format(person[0], person[1], person[2])) 

def monthly_spending(cursor):
	total = 0
	employee_salary = "SELECT monthly_salary FROM company" 
	for salary in cursor.execute(employee_salary):
		total += salary[0]
	return total

def yearly_spending(cursor):
	year_bonus = 0
	employee_bonus = "SELECT yearly_bonus FROM company"
	for bonus in cursor.execute(employee_bonus):
		year_bonus += bonus[0]

	year_total = year_bonus + (12 * monthly_spending(cursor))
	return year_total

def add_employee(cursor):
	name = input('name: ')
	monthly_salary = int(input('monthly_salary: '))
	yearly_bonus = int(input('yearly_bonus: '))
	position = input('position: ')
	cursor.execute('''INSERT INTO company(name, monthly_salary, yearly_bonus, position)
					VALUES(?,?,?,?)''', (name, monthly_salary, yearly_bonus, position))
	
	conn.commit()

def delete_employee(cursor, index):
	cursor.execute("DELETE FROM company WHERE id = ? ", (index,))
	conn.commit()

def update_employee(cursor, index):
	name = input('name: ')
	monthly_salary = int(input('monthly_salary: '))
	yearly_bonus = int(input('yearly_bonus: '))
	position = input('position: ')
	cursor.execute('''UPDATE company SET name = ?, monthly_salary = ?,
			yearly_bonus = ?, position = ? WHERE id = ? ''', 
			(name, monthly_salary, yearly_bonus, position, index))
	
	conn.commit()

def main():
	cursor = open_connection('mydb')

	while True:
		command = parse_command(input("command>"))

		if is_command(command, "list_employees"):
			list_employees(cursor)

		elif is_command(command, "monthly_spending"):
			print(monthly_spending(cursor))

		elif is_command(command, "yearly_spending"):
			print(yearly_spending(cursor))

		elif is_command(command, "answer"):
			trigger_answer(conn, command)

		elif is_command(command, "finish"):
			break
		else:
			print(trigger_unknown_command())

	conn.close()
	

	#yearly_spending(cursor)
	#add_employee(cursor)
	#list_employees(cursor)
	#delete_employee(cursor, 3)
	#list_employees(cursor)
	#update_employee(cursor,1)

if __name__ == '__main__':
    main()

















# srqda relacii m/y bazi danni
# ORM
# sum direktno v SQL
# dependancy injection


#python script that loads inital data - decapling