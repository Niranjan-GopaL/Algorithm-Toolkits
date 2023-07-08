from heapq import heappop,heappush
from queue import PriorityQueue

def Prims_algorithm():
    cost = 0

    pq = []
    heappush(pq,[0,0]) #cost,node

    while pq:
        print(f'\n-----------Queue -------------------\n\n')
        cost_u,u = heappop(pq)
        print(f'cost = {cost} and u = {u} and vis[{u}] = {vis[u]}')

        if vis[u]:continue

        cost += cost_u; vis[u] = 1

        for cost_v,v in graph[u]:
            if not vis[v]:
                heappush(pq,[cost_v,v])
        print(f'\n After looking at all the nieghbours of {u}     heap is : {pq} \n')

    return cost




''' TEST CASES



points = [[3,12],[-2,5],[-4,1]]
'''

# t = int(input())
# points = []

# for _ in range(t):
#     points.append(map(int,input().split()))

points = [[3,12],[-2,5],[-4,1]]

n = len(points)
vis = [0]*n
graph = [[] for _ in range(n)]

for u in range(n):
    x1,y1 = points[u]

    for v in range(u+1,n):
        x2,y2 = points[v]
        d = abs(x1-x2) + abs(y1-y2)

        graph[u].append([d,v])
        graph[v].append([d,u])

print(graph)
print(Prims_algorithm())