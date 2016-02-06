def lengthOfLastWord(A) :
	if len(A.replace(" ","")) == 0 :
		return 0
	A = A[::-1]
	A = A.split()
	return len(A[0])

# print lengthOfLastWord("   ")

def reverseWords(A):
	if len(A) == 0 :
		return ""
	A = A.split()
	A = A[::-1]
	# print A
	i = 0
	s = str()
	while i < len(A) :
		if i == len(A) -1  :
			s+= A[i]
			break
		s += A[i] + " "
		i+=1
	# if s[len(s)-1] == ' ' :
	# 	s[len(s)-1] = ''
	return s
# print reverseWords("the sky is blue")

def strStr(haystack, needle) :
	if len(haystack) == 0 or len(needle) == 0 :
		return -1
	i = 0
	flag = 0
	while i < len(haystack) :
		j = 0
		prev = i
		while j < len(needle) :
			if haystack[i] != needle[j] :
				break
			j += 1
			i +=1
		if j == len(needle) :
			flag = 1
			break
		i = prev+1
	if flag :
		return i - j
	else :
		return -1
	# return i - j

# print strStr("Lalith","th")

def compareVersion(A, B):
	if len(A) == 0 and len(B) == 0 :
		return 0
	# A = str(A)
	A = A.split(".")
	# B = str(B)
	B = B.split(".")
	i = 0
	j = 0
	while j < len(B) and i < len(A):
		if int(B[j]) > int(A[i]) :
			return -1
		elif int(B[j]) < int(A[i]) :
			return 1
		i +=1
		j +=1
	if i == len(A) and j == len(B) :
		return 0
	if j < len(B) or i < len(A) :
	    if i == len(A) :
	        
	        if B[j] == '0' :
	            return 0
	        return -1
	    elif j == len(B) :
	        
	        if A[i] == '0' :
	            return 0
	        return 1

# print compareVersion("1.13.4","1.1")

def atoi(A) :
	A = A.split()
	A = A[0]
	flag = 0

	for i in len(A) :
		if A[i] >'9' or A[i] < '0' :
			flag = 1
			break
	if flag :
		if i == 0:
			return int(A[1:-1])
		return int(A[:i])
	if A <= '9' and A >= '0' :
		return int(A)
	else :
		return 0
		

