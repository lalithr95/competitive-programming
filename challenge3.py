base = dict()
for i in "abcdefghijklmnopqrstuvwxyz" :
	base[i] = ord(i) - 96


def calculate(s) :
	sum = 0
	for j in s :
		sum += base[j]
	return sum

def answer(names):
	
	new_data = dict()
	data = list()
	sum_data = list()
	for i in names :
		sum = calculate(i)
		if sum in new_data :
			new_data[sum].append(i)
		else :
			new_data[sum] = []
			new_data[sum].append(i)
		if sum not in sum_data :
			sum_data.append(sum)
	sum_data = sorted(sum_data, reverse=True)
	#print sum_data

	temp_str = list()
	for each in range(len(sum_data)) :
		temp_str.append(new_data[sum_data[each]])
	# temp_str is list of lists
	result = list()
	for i in temp_str :
		i = sorted(i, reverse=True)
		for x in i :
			result.append(x)
	return result

# print answer(["annie", "bonnie", "liz"])