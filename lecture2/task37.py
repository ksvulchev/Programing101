#!/usr/bin/python
def row_check(matrix, summ):

	for row in range(len(matrix)):
		col_sum = 0
		for col in range(len(matrix[row])):
			col_sum += matrix[row][col]
		print(col_sum)
		if col_sum != summ:
			return False

	return True

def col_check(matrix, summ):

	for col in range(len(matrix)):
		row_sum = 0
		for row in range(len(matrix[col])):
			row_sum += matrix[row][col]
		print(row_sum)
		if row_sum != summ:
			return False

	return True

def diagonal_check(matrix, summ):

	diagonal_sum = 0
	diagonal_two_sum = 0
	for col in range(len(matrix)):
	

		diagonal_sum  += matrix[col][col]
		diagonal_two_sum += matrix[col][len(matrix)-col-1]

	if diagonal_sum != summ or diagonal_two_sum != summ :
		return False



	return True

def magic_square(matrix):
	summ = 0
	for n in matrix[0]:
		summ += n
		print(summ)


	if col_check(matrix,summ) and col_check(matrix,summ) and diagonal_check(matrix,summ):
		return True
	else:
		return False
	


print (magic_square([[1,2,3], [4,5,6], [7,8,9]]))