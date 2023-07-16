from math import inf
from heapq import heappop,heappush


def Dijkstras(src):
    dist = [inf]*n
    dist[src] = 0; pq = []
    heappush(pq,[0,src])
    while pq:
        d,u = heappop(pq)
        for v in edges[u]:
            if dist[v] > dist[u] + v:
                dist[v] = dist[u] + v
                heappush(pq,[dist[v],v])
    return dist


n,m,s = map(int,input().split())
v = list(map(int,input().split()))
edges = [[] for _ in range(n)]

for _ in range(m):
    u,v = map(int,input().split())
    edges[u].append(v) 

for i in range(m):
    pass