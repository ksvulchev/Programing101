def sudoku_solved(sudoku):
	a = 0
	b = 3
	c = 0
	d = 3
	arr = []
	for i in range(3):
		for y in range(3):
			for row in range(c,d):
				for col in range(a,b):
					arr.append(sudoku[row][col])

			a += 3
			b += 3
			print(arr)
			arr = []
		c += 3
		d += 3
		a = 0
		b = 3

sudoku_solved([
[4, 5, 2, 3, 8, 9, 7, 1, 6],
[3, 8, 7, 4, 6, 1, 2, 9, 5],
[6, 1, 9, 2, 5, 7, 3, 4 ,8],
[9, 3, 5, 1, 2, 6, 8, 7, 4],
[7, 6, 4, 9, 3, 8, 5, 2, 1],
[1, 2, 8, 5, 7, 4, 6, 3, 9],
[5, 7, 1, 8, 9, 2, 4, 6, 3],
[8, 9, 6, 7, 4, 3, 1, 5 ,2],
[2, 4, 3, 6, 1, 5, 9, 8, 7]
])