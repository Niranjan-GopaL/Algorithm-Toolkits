from math import inf
from heapq import heappush,heappop


def prims():
    pq = []; priority = [inf]*n; vis = [0]*n; phi = [-2]*n

    # starting from 0
    priority[0] = 0
    phi[0] = -1

    heappush(pq,[priority[0],0])

    print(pq)
    print(vis)

    while pq:
        u_p , u = heappop(pq)
        print(f'\n\n-------- Queue Iterattion ---------------\n')

        print(f'u_p := {u_p} , u := {u}')

        if vis[u]: continue
        vis[u] = 1

        print(f' neighbours of {u} :\n {edges[u]}')
        for v,cost_v in edges[u]:
            print(f'looking at {u}\'s neighbor := {v} , and it\'s cost := {cost_v}')
            if not vis[v] and priority[v] > cost_v:
                priority[v] = cost_v
                phi[v] = u
                heappush(pq, [priority[v] , v])


    print(f'Priority queue is now : {pq}')
    print(f'Priority array is now : {priority}')
    print(f'--------------------------------------')

    # sum of the priority will give the wieght of the MST
    s = 0
    for i in priority:
        s += i
    return s





points = [[0,0],[2,2],[3,10],[5,2],[7,0]]

n = len(points)
edges =[[] for _ in range(n)]

for i in range(n):
    x1,y1 = points[i]

    for j in range(i+1,n):
        x2,y2 = points[j]
        d = abs(x1-y1) + abs(x2-y2)

        edges[i].append([j,d])
        edges[j].append([i,d])

print(f'edges := {edges}')
print(prims())