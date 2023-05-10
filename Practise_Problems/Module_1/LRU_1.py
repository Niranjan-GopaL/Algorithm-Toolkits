class LRUCache:
	# store keys of cache
	def __init__(self, n):
		self.csize = n
		self.dq = []
		self.ma = {}


	# Refers key x with in the LRU cache
	def refer(self, x):
		
		# not present in cache
		if x not in self.ma.keys():
			# cache is full
			if len(self.dq) == self.csize:
				# delete least recently used element
				last = self.dq[-1]

				# Pops the last element
				ele = self.dq.pop();

				# Erase the last
				del self.ma[last]

		# present in cache
		else:
			del self.dq[self.ma[x]]

		# update reference
		self.dq.insert(0, x)
		self.ma[x] = 0;

	# Function to display contents of cache
	def display(self):

		# Iterate in the deque and print
		# all the elements in it
		print(self.dq)

# Driver Code
ca = LRUCache(4)

ca.refer(1)
ca.refer(2)
ca.refer(3)
ca.refer(1)
ca.refer(4)
ca.refer(5)
ca.display()
# This code is contributed by Satish Srinivas
