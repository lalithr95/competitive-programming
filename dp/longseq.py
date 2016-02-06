#http://www.geeksforgeeks.org/dynamic-programming-set-3-longest-increasing-subsequence/
A = [int(x) for x in raw_input().split() ]

print A

result = dict()
for i in range(len(A)) :
	result[i] = 1
i = 1
while i < len(A) :
	for j in range(i) :
		if A[i] > A[j] and result[i] < result[j] + 1:
			result[i] = result[j] + 1
	i +=1 

print max(result.values())