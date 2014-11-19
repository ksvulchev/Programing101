import sqlite3

db = sqlite3.connect('mydb')
cursor = db.cursor()

cursor.execute('''
	CREATE TABLE IF NOT EXISTS company(id INTEGER PRIMARY KEY, name TEXT, monthly_salary INTEGER,
		yearly_bonus INTEGER, position TEXT)
''')

employees = [{
	"name": "Ivan Ivanov",
	"monthly_salary": 5000,
	"yearly_bonus": 10000,
	"position": "Softwate Developer"
}, {
	"name": "Rado Rado",
	"monthly_salary": 500,
	"yearly_bonus": 0,
	"position": "Technical Support Intern"
}, {
	"name": "Ivo Ivo",
	"monthly_salary": 10000,
	"yearly_bonus": 100000,
	"position": "CEO Support Intern"
}, {
	"name": "Petar Petrov",
	"monthly_salary": 3000,
	"yearly_bonus": 1000,
	"position": "Marketing Manager"
}, {
	"name": "Georgieva Georgieva",
	"monthly_salary": 8000,
	"yearly_bonus": 10000,
	"position": "COO"
}]

def insert(person, cursor):
	name = person['name']
	monthly_salary = person['monthly_salary']
	yearly_bonus = person['yearly_bonus']
	position = person['position']

	cursor.execute('''INSERT INTO company(name, monthly_salary, yearly_bonus, position)
					VALUES(?,?,?,?)''', (name, monthly_salary, yearly_bonus, position))

for person in employees:
    insert(person, cursor)

db.commit()
db.close()