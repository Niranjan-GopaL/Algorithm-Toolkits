
# Naive way of merging
def merge(u,v):
    if label[u] > label[v]:
        for i in range(n):
            if label[i] == label[v]:
                label[i] = label[u]
    else:
        for i in range(n):
            if label[i] == label[u]:
                label[i] = label[v]



# # DSU in very rudimentary form!!!!
# def find(node):
#     while node!= label[node]:
#         node = label[node]
#     return label[node]

# def union_unoptimised(u,v):
#     if find(u) != find(v):
#         label[find(u)] = find(v)


# OPTIMISED with PATH COMPRESSION
def find(node):
    if label[node] == node:
        return node
    
    label[node] = find(label[node])
    return label[node]


def union(u,v):
    u = find(u)
    v = find(v)

    if u != v:

        if size[u] < size[v]:
            u,v = v,u

        label[v] = u
        size[v]+=size[u]




def Kruskal_algo():
    mst = []

    for edge in edges:
        print(f'\n----------- EDGE : {edge}-----------\n\n')
        d,u,v = edge

        print(f'Labels : {u} : {find(u)}      {v} : {find(v)}')

        if find(label[u]) != find(label[v]):
            mst.append(edge)
            # merge(u,v)
            union(u,v)

        print(f'Labels : {u} : {find(label[u])}      {v} : {find(label[v])} after merging\n\n')
        print(f'labels after updation : {label}')
        print(f'MST at the end of the iteration : {mst}\n')
        print("-------------------------------------------------\n\n\n")

    print(mst)
    s = 0
    for i in mst:
        s += i[0]
    return s




points = [[3,12],[-2,5],[-4,1]]
# points = [[0,0],[2,2],[3,10],[5,2],[7,0]]


n = len(points)
label = [ i for i in range(n)]
size = [1]*n
edges = []


for u in range(n):
    x1,y1 = points[u]
    for v in range(u+1,n):
        x2,y2 = points[v]
        d = abs(x1-x2) + abs(y1-y2)
        edges.append([d,u,v])

edges.sort()
print(f' edges ---> {edges}') 
print(Kruskal_algo())