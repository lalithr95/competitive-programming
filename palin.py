def check(x) :
	y = x[::-1]
	if x == y:
		return True
	return False

T = int(raw_input())



for i in range(T) :
	num = int(raw_input())
	num +=1
	while not check(str(num)) :
		num += 1

	print num


