#https://www.codechef.com/FEB16/problems/SEAPERMS
N,D = gets.chomp.split(" ").map(&:to_i)
A = gets.chomp.split(" ").map(&:to_i)
M = gets.chomp.to_i
PA = A.permutation.to_a

def check_valid? perm, sum
	flag = 1
	perm.each_with_index do |x, i|
		if i == (perm.count -1)
			break
		end
		if A[perm[i]-1] + sum < A[perm[i+1]-1]
			flag = 0
			break
		end
	end
	return flag
end

while M > 0 do
	p,v = gets.chomp.split(" ").map(&:to_i)
	count1 = 0
	A[p-1] = v
	PA.each do |perm|
		if check_valid? perm, D
			count1 += 1
		end
	end
	puts count1
	M -= 1
end
