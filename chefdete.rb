#https://www.codechef.com/FEB16/problems/CHEFDETE

N = gets.chomp.to_i
result = {}
people = [*1..N]
people.each do |x|
	result[x] = 0
end
R = gets.chomp.split(" ").map(&:to_i)
people.each_with_index do |x,i|
	result[R[i-1]] += 1 if R[i-1] != 0
end

final = []
result.each do |x,y|
	if result[x] == 0
		final << x
	end
end

puts final.join(" ")
