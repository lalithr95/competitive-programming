T = int(raw_input())
while T>0:
	result = [ int(i) for i in raw_input().split()]
	A = [ int(i) for i in raw_input().split()]
	B = [ int(i) for i in raw_input().split()]
	matrix = [[0 for j in range(result[0])] for i in range(result[0])]
	for i in range(result[0]):
		for j in range(result[0]):
			matrix[i][j] = ( A[i]*(i+1) + B[j]*(j+1) + result[2] ) % result[3]

	left = 0
	max_sum = 0

	while left<result[0]:
		temp = [0 for i in range(result[0])]
		right = left
		while right<result[0]:
			right+=1
		left+=1

	for i in range(result[0]):
		for j in range(result[0]):
			print matrix[i][j]
	T-=1