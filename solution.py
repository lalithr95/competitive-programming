import urllib2
import os
import math
import json
endpoint = "curl --header 'token: oSgDmnvLL9GwKZwFoiKHJE' https://www.find.foo/api/challenge"
# data = os.system(endpoint)
# print data

import subprocess
result = os.popen(endpoint).read()
data = json.loads(result)

challenge = data['challenge']

if challenge[1] == 'b' :
	result = challenge.split()
	if result[1] == '+' :
		data = int(result[0], 2) + int(result[2], 2)
		data = bin(data)
	if result[1] == '-' :
		data = int(result[0], 2) - int(result[2], 2)
		data = bin(data)
	if result[1] == '*' :
		data = int(result[0],2) * int(result[2], 2)
		data = bin(data)
	if result[1] == '/' :
		data = int(result[0], 2) / int(result[2], 2)
		data = bin(data)
	
elif challenge[1] == 'x' :
	result = challenge.split()
	if result[1] == '+' :
		data = int(result[0],16) + int(result[2], 16)
		data = hex(data)
	if result[1] == '-' :
		data = int(result[0], 16) - int(result[2], 16)
		data = hex(data)
	if result[1] == '*' :
		data = int(result[0], 16) * int(result[2], 16)
		data = hex(data)
	if result[1] == '/' :
		data = int(result[0], 16) / int(result[2], 16)
		data = hex(data)
	
new_endpoint = "curl --header 'token: oSgDmnvLL9GwKZwFoiKHJE' --data 'answer="+data+"' https://www.find.foo/api/challenge"
# os.system(new_endpoint)

result = os.popen(new_endpoint).read()
data = json.loads(result)

#### challenge 2 ####
def is_prime(num):
	for j in range(2,int(math.sqrt(num)+1)):
		if (num % j) == 0:
			return False
	return True

odd_num = list()
even_num = list()
prime_num = [2,3]
fib_num = list()
for i in range(101) :
	if i % 2 == 0 :
		even_num.append(i)
	else :
		odd_num.append(i)

fib_num = [0 , 1]
i = 2
while 1 :
	sum_num = fib_num[i-1] + fib_num[i-2]
	if sum_num > 100 :
		break
	fib_num.append(sum_num)
	i +=1

i = 4
while i < 10001 :
	if is_prime(i) :
		prime_num.append(i)
	i +=1

def check(data, ch) :
	result = list()
	if ch == 'O' :
		for i in data :
			if int(i) in odd_num :
				result.append(int(i))
	elif ch == 'E' :
		for i in data :
			if int(i) in even_num :
				result.append(int(i))
	elif ch == 'P' :
		for i in data :
			if int(i) in prime_num :
				result.append(int(i))
	elif ch == 'F' :
		for i in data :
			if int(i) in fib_num :
				result.append(int(i))

	return result

challenge = data['challenge']
challenge2_list = ''
result = list()
index = challenge.index('[')
challenge2_list = challenge[index+1:-1]
challenge2_list = challenge2_list.replace(",", "")
challenge2_list = challenge2_list.split(" ")

if challenge[0] == 'O' :
	result = check(challenge2_list, challenge[0])
elif challenge[0] == 'E' :
	result = check(challenge2_list, challenge[0])
elif challenge[0] == 'F' :
	result = check(challenge2_list, challenge[0])
elif challenge[0] == 'P' :
	result = check(challenge2_list, challenge[0])

new_endpoint = "curl --header 'token: oSgDmnvLL9GwKZwFoiKHJE' --data 'answer="+str(result)+"' https://www.find.foo/api/challenge"
# os.system(new_endpoint)

result = os.popen(new_endpoint).read()
data = json.loads(result)

### challenge 3###
L = data['challenge'][29:33]
R = int(data['challenge'][38:42])
result = 0
i = int(L)
while i <= R :
	if is_prime(int(i)) :
		result += int(i)
	i +=1

new_endpoint = "curl --header 'token: oSgDmnvLL9GwKZwFoiKHJE' --data 'answer="+str(result)+"' https://www.find.foo/api/challenge"
# os.system(new_endpoint)

result = os.popen(new_endpoint).read()
data = json.loads(result)





