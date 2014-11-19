import sqlite3

db = sqlite3.connect('cinemadb.db')
cursor = db.cursor()
cursor.execute("PRAGMA foreign_keys = ON; ")
cursor.execute('''
	CREATE TABLE IF NOT EXISTS movies(
		id INTEGER PRIMARY KEY, 
		name TEXT, 
		rating REAL)
''')

cursor.execute('''
	CREATE TABLE IF NOT EXISTS projections(
		id INTEGER PRIMARY KEY, 
		movie_id INTEGER,
		type TEXT,
		date_time TEXT,
		FOREIGN KEY (movie_id) REFERENCES movies(id))
''')


cursor.execute('''
	CREATE TABLE IF NOT EXISTS reservations(
		id INTEGER PRIMARY KEY, 
		username TEXT, 
		projections_id INTEGER,
		row INTEGER, 
		col INTEGER,
		FOREIGN KEY (projections_id) REFERENCES projections(id))
''')

db.commit()
db.close()