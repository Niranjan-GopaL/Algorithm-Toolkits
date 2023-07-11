class DSU:
    def __init__(self):
        self.parents = [i for i in range(n)]
        self.sz = [1]*n

    def find(self,x):
        if x == self.parents[x]: return x
        self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self,u,v):
        u = self.find(u); v = self.find(v)
        if u != v:
            if self.sz[u] < self.sz[v]:
                u,v = v,u
            self.parents[v] = u
            self.sz[u] += self.sz[v]



n,m = map(int(input().split()))
edges = []

for _ in range(m):
    u,v,w = map(int(input().split()))
    edges.append((w,u,v))

edges.sort(key = lambda x: x[0] )