#!/usr/bin/python
#INCOMPLETE
def matrix_bombing_plan(m):
	original_matrix = m[:]
	suma = 0
	for i in range(len(original_matrix)):
			for y in range(len(original_matrix[i])):

				if i + 1 == len(original_matrix) or (i -1) < 0:
					pass
				else:
					if y + 1 == len(original_matrix) or (y -1) < 0:
						pass
					else:
						suma += original_matrix[i][y]
				print(suma)
				suma = 0
			


matrix_bombing_plan([[1,2,3], [4,5,6], [7,8,9]])