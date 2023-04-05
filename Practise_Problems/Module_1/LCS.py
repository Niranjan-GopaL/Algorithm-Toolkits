# Function to implement rolling hash
class ComputeHash:

	# Generates hash in O(n(log(n)))
	def __init__(self, s, p, mod):
		n = len(s)
		self.hash = [0] * n
		self.inv_mod = [0] * n
		self.mod = mod
		self.p = p

		p_pow = 1
		hash_value = 0

		for i in range(n):
			c = ord(s[i]) - 65 + 1
			hash_value = (hash_value + c * p_pow) % self.mod
			self.hash[i] = hash_value
			self.inv_mod[i] = pow(p_pow, self.mod - 2, self.mod)
			p_pow = (p_pow * self.p) % self.mod

	# Return hash of a window in O(1)
	def get_hash(self, l, r):

		if l == 0:
			return self.hash[r]

		window = (self.hash[r] - self.hash[l - 1]) % self.mod
		return (window * self.inv_mod[l]) % self.mod

# Function to get the longest common substring
def longestCommonSubstr(X, Y, n, m):

	p1, p2 = 31, 37
	m1, m2 = pow(10, 9) + 9, pow(10, 9) + 7

	# Initialize two hash objects
	# with different p1, p2, m1, m2
	# to reduce collision
	hash_X1 = ComputeHash(X, p1, m1)
	hash_X2 = ComputeHash(X, p2, m2)

	hash_Y1 = ComputeHash(Y, p1, m1)
	hash_Y2 = ComputeHash(Y, p2, m2)

	# Function that returns the existence
	# of a common substring of length k
	def exists(k):

		if k == 0:
			return True

		st = set()
		
		# Iterate on X and get hash tuple
		# of all windows of size k
		for i in range(n - k + 1):
			h1 = hash_X1.get_hash(i, i + k - 1)
			h2 = hash_X2.get_hash(i, i + k - 1)

			cur_window_hash = (h1, h2)
			
			# Put the hash tuple in the set
			st.add(cur_window_hash)

		# Iterate on Y and get hash tuple
		# of all windows of size k
		for i in range(m - k + 1):
			h1 = hash_Y1.get_hash(i, i + k - 1)
			h2 = hash_Y2.get_hash(i, i + k - 1)

			cur_window_hash = (h1, h2)
			
			# If hash exists in st return True
			if cur_window_hash in st:
				return True
		return False

	# Binary Search on length
	answer = 0
	low, high = 0, min(n, m)

	while low <= high:
		mid = (low + high) // 2

		if exists(mid):
			answer = mid
			low = mid + 1
		else:
			high = mid - 1

	return answer


X = ''.join(input().split())
Y = ''.join(input().split())
print(longestCommonSubstr(X, Y, len(X), len(Y)))
