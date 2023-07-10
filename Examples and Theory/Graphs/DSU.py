'''

parent = [None]*10000


# this is  BASIC OVERVIEW OF DFS
def make(a):
    parent[a] = a

# recrursive
def find(v):
    if v == parent[v]: return v
    return find(parent[v])

# iterative
def find_(v):
    while v != parent[v]:
        v = parent[v]
    return v

def union(a, b):
    a = find(a)
    b = find(b)
    if a!=b: parent[b] = a

'''


# BUT FURTHUR OPTIMIZATION IS POSSIBLE
parent = [i for i in range(20)]
size = [1]*20

def find(node):
    if parent[node] == node: 
        return node

    parent[node] = find(parent[node])
    return parent[node]


def union(a, b):

    print(f'-> Before path compression : parent of {a}: {parent[a]}, parent of {b}: {parent[b]}')

    a = find(a)
    b = find(b)


    if a!=b:
        if size[a] < size[b]:
            a, b = b, a

        # we are sure that component of A has more nodes than B
        parent[b] = a
        size[a] += size[b]
    print(f'-> After  path compression : parents of _: {parent[a]}, parent of _: {parent[b]}')


def DSU_workings(u,v):

    print(f'\n----------Adding {u} and {v} to DSU----------\n\n')
    union(u,v)

    print(f'\n\nSo parents array : {parent}')
    print(f'corresponding    : {[i for i in range(20)]}')
    print(f'corresponding    : {size}')




connect_nodes = [
    (0,10),
    (11,9),
    (0,9),
    (18,19),
    (1,2),
    ]

for u,v in connect_nodes: 
    DSU_workings(u,v)