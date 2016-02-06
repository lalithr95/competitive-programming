#https://www.codechef.com/FEB16/problems/STROPR
T = gets.chomp.to_i
while T > 0  do
	N,x,M = gets.chomp.split(" ").map(&:to_i)
	A = gets.chomp.split(" ").map(&:to_i)
	M.times do
		for i in 1..N-1
			A[i] += A[i-1]
		end
	end
	puts A[x-1]% (10 ** 9 + 7)
	T -= 1
end