from fractions import Fraction

def sort_fractions(fractions):

	for i in range(len(fractions)):	# malko Bubble sort :D
		for y in range(1,len(fractions)-i): 
			if fractions[y-1][0] / fractions[y-1][1] > fractions[y][0] / fractions[y][1]:


				fractions[y-1],fractions[y] = fractions[y], fractions[y-1]


	return fractions
print (sort_fractions([(2, 3), (1, 2), (1, 3)]))