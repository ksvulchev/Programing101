import sqlite3

def open_connection(database):
    conn = sqlite3.connect(database)
    return conn

def import_movie(conn, name, rating):
	conn.cursor().execute('''INSERT INTO movies(name,rating)
					VALUES(?,?)''', (name, rating))
	
	conn.commit()

def import_projection(conn, movie_id, type, date_time):
	conn.cursor().execute('''INSERT INTO projections(movie_id,type,date_time)
					VALUES(?,?,?)''', (movie_id, type, date_time))
	
	conn.commit()

def main():
	conn = open_connection('cinemadb.db')
	import_movie(conn, "The Hunger Games: Catching Fire", 7.9)
	import_movie(conn, "Wreck-It Ralph", 7.8)
	import_movie(conn, "Her", 8.3)
	import_projection(conn, 1, "3D", "2014-04-01")
	import_projection(conn, 1, "2D", "2014-04-02")
	import_projection(conn, 2, "3D", "2014-04-03") 
	import_projection(conn, 2, "3D", "2014-04-03") 
	conn.close()

if __name__ == '__main__':
	main()


