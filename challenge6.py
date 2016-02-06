from operator import itemgetter
def answer(minions) :
	result = []
	for minion in minions :
		result.append((0.0 + minion[0])/((0.0 + minion[1])/minion[2]))
	final = [a[0] for a in sorted(list(enumerate(result)), key=itemgetter(1))]
	# print final
	return final

# answer([[390, 185, 624], [686, 351, 947], [276, 1023, 1024], [199, 148, 250]])

def get(s) :
	for i in s :

print get("abab")
