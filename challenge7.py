from math import factorial
class BinarySearch :

	def __init__(self, *inputs) :
		self.value = None
		self.left = None
		self.right = None

		for i in inputs :
			self.insert(i) 

	def insert(self, value) :
		if not self.value :
			self.value = value

		elif self.value < value :
			if self.right :
				self.right.insert(value)
			else :
				self.right = BinarySearch(value)
		elif self.value > value :
			if self.left :
				self.left.insert(value)
			else :
				self.left = BinarySearch(value)


def answer(seq):
	return permutations(BinarySearch(*seq))
def select(n, k):
    return factorial(n) / (factorial(k) * factorial(n - k))


def length(node):
    return 1 + length(node.left) + length(node.right) if node else 0


def permutations(node):

    if not node:
    	return 1
    l = length(node.left)
    r = length(node.right)
    left_count = permutations(node.left)
    right_count = permutations(node.right)

    return select(l + r, r) * left_count * right_count


# print answer([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print answer([5, 9, 8, 2, 1])
