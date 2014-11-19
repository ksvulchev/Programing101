import sqlite3

def open_connection(database):
	conn = sqlite3.connect(database)
	return conn

def format_command(command):
	command_list = command.split(" ")
	return(command_list)

def show_movies(conn):
	all_movies = "SELECT id, name, rating FROM movies"
	print("Current movies:")
	for movie in conn.cursor().execute(all_movies):
		print("[{}] - {} ({})".format(movie[0], movie[1], movie[2]))

def show_movie_projections(conn, movie_id):
	movie_id = int(movie_id)
	cursor = conn.cursor()
	projections = cursor.execute(
					'''SELECT movies.name, projections.id, projections.date_time  FROM movies  
					INNER JOIN projections ON movies.id = projections.movie_id WHERE movies.id = ?'''
					, (movie_id,))
	rows = cursor.fetchall()
	print ("Projections for movie '{}':".format(rows[0][0]))
	for movie in rows:
		print ("[{}] - {} ".format(movie[1], movie[2])) 

def show_reservations(conn, projection_choice):
	cursor = conn.cursor()
	reservations = cursor.execute('''SELECT col, row FROM reservations WHERE
					projections_id = ?''',(projection_choice,))
	rows = cursor.fetchall()

	matrix = []		
	for x in range(1,11):
		row = []
		for y in range(1,11):		
			row.append('.')
		matrix.append(row)

	for i in rows:
		matrix[i[0] - 1][i[1] - 1] = "X"

	for j in matrix:
		print(" ".join(j))

def make_reservation(conn):

	user = input("Step 1 (User): Choose name>")
	num_of_tickets = int(input("Step 1 (User): Choose number of tickets>"))
	show_movies(conn)
	movie_choice = input("Step 2 (Movie): Choose a movie>")
	show_movie_projections(conn, movie_choice)
	projection_choice = int(input("Step 3 (Projection): Choose a projection>"));
	show_reservations(conn, projection_choice)
	for i in range(num_of_tickets):
		seat_choose = input("Step 4 (Seats): Choose seat {}>".format(num_of_tickets + 1))
		choose_seat(conn, seat_choose[1], seat_choose[3], projection_choice, user)

def choose_seat(conn, col, row, projection_choice, user):
	cursor = conn.cursor()
	insert_seat_choice = '''INSERT INTO reservations(username, projections_id, row, col)
					VALUES(?,?,?,?)'''
	cursor.execute('''INSERT INTO reservations(username, projections_id, row, col)
					VALUES(?,?,?,?)''', (user, projection_choice, row, col))
	conn.commit()

def main():
	conn = open_connection('cinemadb.db')
	while True:
		command = input("command> ")
		command_list = format_command(command)
		if command_list[0] == "show_movies":
			show_movies(conn)
		elif command_list[0] == "show_movie_projections":
			show_movie_projections(conn,command_list[1])
		elif command_list[0] == "make_reservation":
			make_reservation(conn)

	conn.close()

if __name__ == '__main__':
	main()



