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



# BUT FURTHUR OPTIMIZATION IS POSSIBLE