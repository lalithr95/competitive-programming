#https://www.codechef.com/FEB16/problems/SEAPERMS
N,D = gets.chomp.split(" ").map(&:to_i)
A = gets.chomp.split(" ").map(&:to_i)
PA = A.permutation.to_a
def check_valid_perm?(perm, sum)
	flag = 1
	i = 0
	perm.each_index do |i|
		if i == (perm.count -1)
			break
		end
		if (A[perm[i]-1] + sum) < A[perm[i+1]-1]
			flag = 0
			break
		end
	end
	return flag
end

def main_meth
	m = gets.chomp.to_i
	while m > 0
		p,v = gets.chomp.split(" ").map(&:to_i)
		count1 = 0
		A[p-1] = v
		PA.each do |perm|
			if check_valid_perm?(perm, D)
				count1 += 1
			end
		end
		puts count1
		m -= 1
	end
end
main_meth
