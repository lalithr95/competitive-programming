X = str(raw_input())
Y = str(raw_input())

def longcomseq(X,Y) :
	result = [ [0 for i in range(len(X)+1)] for j in range(len(Y)+1)]
	for i in range(1,len(X)+1) :
		for j in range(1,len(Y)+1) :
			if i == 0 or j == 0 :
				result[i][j] = 0
			elif X[i-1] == Y[j-1] :
				result[i][j] = result[i-1][j-1] +1
			else :
				result[i][j] = max(result[i-1][j], result[i][j-1])
	return result[-1][-1]

print longcomseq(X,Y)