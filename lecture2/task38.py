def sudoku_solved(sudoku):
	compare = [1,2,3,4,5,6,7,8,9]
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
			if len(set(arr)) != 9:
				return False
			arr = []
		c += 3
		d += 3
		a = 0
		b = 3

		for i in range(9):
			col = []
			row = []
			for y in range(9):
				col.append(sudoku[y][i])
				row.append(sudoku[i][y])

			if len(set(col)) != 9 or len(set(row)) != 9:
				return False




		return True

print (sudoku_solved([
[1, 2, 3, 4, 5, 6, 7, 8, 9],
[1, 2, 3, 4, 5, 6, 7, 8, 9],
[1, 2, 3, 4, 5, 6, 7, 8, 9],
[1, 2, 3, 4, 5, 6, 7, 8, 9],
[1, 2, 3, 4, 5, 6, 7, 8, 9],
[1, 2, 3, 4, 5, 6, 7, 8, 9],
[1, 2, 3, 4, 5, 6, 7, 8, 9],
[1, 2, 3, 4, 5, 6, 7, 8, 9],
[1, 2, 3, 4, 5, 6, 7, 8, 9]
]))