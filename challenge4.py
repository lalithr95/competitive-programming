def answer(digest):
	digest_output = list()
	for i in range(len(digest)) :
		if i  == 0 :
			digest_output.append(next_val(digest[i],0))
		else :
			digest_output.append(next_val(digest[i],digest_output[len(digest_output)-1]))

	return digest_output

def next_val(digest, val) :
	i = 0
	while True :
		x = ((digest ^ val) + i *256) % 129
		if x == 0 :
			return ((digest ^ val) + i * 256)/129
		else :
			i +=1
	

# print answer([0, 129, 3, 129, 7, 129, 3, 129, 15, 129, 3, 129, 7, 129, 3, 129])

