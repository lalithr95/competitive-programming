
def coinchange(A, m, N) :
	if N == 0 :
		return 1
	if N < 0 :
		return 0
	if m <= 0 and N >=1 :
		return 0


	return coinchange(A, m-1, N) + coinchange(A, m, N - A[m-1])

A = [int(x) for x in raw_input().split()]
N = int(raw_input())
print coinchange(A, len(A), N)