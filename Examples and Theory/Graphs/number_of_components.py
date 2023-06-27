def make(i):
    parent[i] = i
    size[i] = 1

def find(i):
    if parent[i] == i:
        return parent[i]
    
    parent[i] = find(parent[i])
    return parent[i]

def union(a,b):
    a = find(a)
    b = find(b)

    if a != b:

        if size[a] < size[b]:
            # this is probably wrong. THINK ABOUT IT FROM GROUND UP
            # parent[a],parent[b] = parent[b],parent[a]
            a,b = b,a

        size[a] += size[b]
        size[b] = size[a]




'''
4
2
1 2
4 1

2

'''

n = int(input())
k = int(input())

# 1-indexed  
size =[0]*(n+1)
parent =[0]*(n+1)

while(k):
    a,b = list(map(int,input()))
    union(a,b)
    k-=1

no_of_components = 0
for  i in range(1,n+1):
    if find(parent[i]) == i:
        no_of_components += 1

print(no_of_components)