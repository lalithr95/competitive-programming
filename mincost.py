def cost(A, x, y) :
	result = [[0 for j in range(len(A[0]))] for i in range(len(A)) ]

	result[0][0] = 0
	for i in range(len(A)) :
		result[i][0] = result[i-1][0] + A[i][0]
	for j in range(len(A[0])) :
		result[0][j] = result[0][j-1] + A[0][j]

	for i in range(1,len(A)) :
		for j in range(1, len(A[0])) :
			result[i][j] += min(result[i-1][j-1], result[i-1][j], result[i][j-1])

	return result[x][y]

print cost([ [1, 2, 3], [4, 8, 2], [1, 5, 3] ],2 ,2)


