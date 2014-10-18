#!/usr/bin/python
def magic_square(matrix):
	summ = 0
	for n in matrix[0]:
		summ += n
		print(summ)

	for row in range(len(matrix)):
		col_sum = 0
		for col in range(len(matrix[row])):
			col_sum += matrix[row][col]
		print(col_sum)
		if col_sum != summ:
			return False


	for col in range(len(matrix)):
		row_sum = 0
		for row in range(len(matrix[col])):
			row_sum += matrix[row][col]
		print(row_sum)
		if row_sum != summ:
			return False

	diagonal_sum = 0
	diagonal_two_sum = 0
	for col in range(len(matrix)):
	

		diagonal_sum  += matrix[col][col]
		diagonal_two_sum += matrix[col][len(matrix)-col-1]

	if diagonal_sum != summ or diagonal_two_sum != summ :
		return False



	return True

print (magic_square([[16, 23, 17], [78, 32, 21], [17, 16, 15]]	))