def dfs(i,b1,pos):
    if vis[i]: return 0

    vis[i] = 1
    for x in edges[i]:
        if not vis[x]:

            print("--------------")
            print(f'x id {x}')
            print(f'b1 id {b1}')
            print(f'pos : {pos}')
            print("--------------")
            if x == b1:
                return 1

            pos = dfs(x,b1,pos)

    return pos

'''
5
4
0 1 1 2 2 3 0 3
4
0 3 3 2 4 2 1 3
'''


n = int(input())
t = int(input())



edges = [ [] for _ in range(n)]
#  THIS IS DIFFERENT , EACH ELEMENT WOULD POINT TO SAME OBJE
# DON'T MAKE THIS MISTAKE !!!!!!!!!!!!
# edges = [[]]*n 
# print(edges)
prereq = list(map(int,input().split()))
for i in range(0,len(prereq),2):
    edges[prereq[i]].append(prereq[i+1])
    print(f" index i : {i} and {prereq[i]} ---> {prereq[i+1]}")
    print(f"edges : {edges}")
print(edges)



q = int(input())
Q = list(map(int,input().split()))
a = []
for i in range(0,q*2,2):
    vis = [0]*n
    a1,b1 = Q[i:i+2]
    print(a1,b1)
    a.append(dfs(a1,b1,0))
    print(f'a : {a}')


for j in a:
    print(j,end=' ')