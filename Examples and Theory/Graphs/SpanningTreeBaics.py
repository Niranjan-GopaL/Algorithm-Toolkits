from collections import deque

def isSpanningTree(n,graph):

    vis = [0]*n
    c = 0

    q = deque([0])

    while q:
        u = q.popleft()

        for v in graph[u]:
            if vis[v]:
                return False
            else:
                q.append(v)
                vis[v] = 1
                c += 1

    # this is also valid , this implies that the graph isn't connected
    for i in range(n):
        if vis[i] == 0:
            return False

    if c != n-1: return False # this is the easy way to check if the graph is spanning tree 

    return True





















