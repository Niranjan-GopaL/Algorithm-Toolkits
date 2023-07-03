from collections import deque, defaultdict

class Graph:
	
	def __init__(self, n):
		self.n = n
		self.l = defaultdict(list)
		
	def addedge(self, V1, V2):
		self.l[V1].append(V2)
		self.l[V2].append(V1)

	def bfs(self, in1, in2):
		visited = [0] * self.n
		q = deque()
		visited[in1] = 1
		q.append(in1)
		while q:
			p = q.popleft()
			for neighbor in self.l[p]:
				if not visited[neighbor]:
					visited[neighbor] = visited[p] + 1
					q.append(neighbor)
				if neighbor == in2:
					return visited[neighbor] - 1
		return -1



def shortestPath(num1, num2):
	pset = []
	SieveOfEratosthenes(pset)
	g = Graph(len(pset))
	for i in range(len(pset)):
		for j in range(i + 1, len(pset)):
			if compare(pset[i], pset[j]):
				g.addedge(i, j)
	in1, in2 = None, None
	for i in range(len(pset)):
		if pset[i] == num1:
			in1 = i
	for i in range(len(pset)):
		if pset[i] == num2:
			in2 = i
	return g.bfs(in1, in2)





def SieveOfEratosthenes(v):
	n = 9999
	prime = [True] * (n + 1)
	p = 2
	while p * p <= n:
		if prime[p]:
			for i in range(p * p, n + 1, p):
				prime[i] = False
		p += 1
	for p in range(1000, n + 1):
		if prime[p]:
			v.append(p)

def compare(num1, num2):
	s1 = str(num1); s2 = str(num2); c = 0
	for i in range(4):
		if s1[i] != s2[i]:
			c += 1

	return c == 1



num1 = 1033
num2 = 7057
print(shortestPath(num1, num2))
