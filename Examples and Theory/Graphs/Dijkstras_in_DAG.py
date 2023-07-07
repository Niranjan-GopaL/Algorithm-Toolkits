from queue import PriorityQueue
from math import inf

def shortest_in_DAG(n, vis):
    pass




n = 10; m = 20
graph = [[] for i in range(n)]

for i in range(m):
    u,v = map(int, input().split())
    graph[u].append(v)


S = [-inf for i in range(n)]
D = [inf for i in range(n)]

vis = [0]*n