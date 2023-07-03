import queue
from collections import defaultdict,deque

class Graph:
	
	def __init__(self, n):
		self.n = n
		self.l = [[] for i in range(n)]
		
	def addedge(self, V1, V2):
		self.l[V1].append(V2)
		self.l[V2].append(V1)

	# in1 and in2 are two vertices of graph
	# which are actually indexes in pset[]
	def bfs(self, in1, in2):
		visited = [0] * self.n
		que = queue.Queue()
		visited[in1] = 1
		que.put(in1)
		while (not que.empty()):
			p = que.queue[0]
			que.get()
			i = 0
			while i < len(self.l[p]):
				if (not visited[self.l[p][i]]):
					visited[self.l[p][i]] = visited[p] + 1
					que.put(self.l[p][i])
				if (self.l[p][i] == in2):
					return visited[self.l[p][i]] - 1
				i += 1
	
	# Returns true if num1 and num2
	# differ by single digit.


# Finding all 4 digit prime numbers
def SieveOfEratosthenes(v):
	
	# Create a boolean array "prime[0..n]" and
	# initialize all entries it as true. A value
	# in prime[i] will finally be false if i is
	# Not a prime, else true.
	n = 9999
	prime = [True] * (n + 1)

	p = 2
	while p * p <= n:

		# If prime[p] is not changed,
		# then it is a prime
		if (prime[p] == True):

			# Update all multiples of p
			for i in range(p * p, n + 1, p):
				prime[i] = False
		p += 1

	# Forming a vector of prime numbers
	for p in range(1000, n + 1):
		if (prime[p]):
			v.append(p)
	

def compare(num1, num2):

    s1 = str(num1); s2 = str(num2); c = 0

    for i in range(4):
        if (s1[i] != s2[i]):
            c += 1

    return (c == 1)
	

def shortestPath(num1, num2):
	
	pset = []
	# pset is prime set := contains all the 4 digit prime numbers
	SieveOfEratosthenes(pset)

	g = Graph(len(pset))
	
    # making all pairs from this huge pile of prime numbers
	for i in range(len(pset)):
		for j in range(i + 1, len(pset)):
			if (compare(pset[i], pset[j])):
				g.addedge(i, j)	

	# Graph nodes ==> indexes in pset[] 
    # so we retrive the indexes of num1 and num2.
	in1, in2 = None, None
	for i in range(len(pset)):
		if (pset[i] == num1):
			in1 = i
	for i in range(len(pset)):
		if (pset[i] == num2):
			in2 = i

	return g.bfs(in1, in2)



num1 = 1033
num2 = 8179
print(shortestPath(num1, num2))