def dfs(i,t):
    label[i] = 1
    t+=1
    strt_time.append(t)
    for x in edges[i]:
        if not label[x]:
            phi[x]=i
            dfs(x,t)
    t+=1
    finish_time.append(t)





''' TEST CASES
7
10
0 1 0 2 0 3 1 3 3 2 2 4 4 5 5 6 6 4 6 7
'''

# normal inputing and storing graphs

n = int(input())
m = int(input())

# creating adjacency list
edges = [ [] for _ in range(n+1)]
label = [0]*(n+1)

pairs = list(map(int,input().split()))
for i in range(0,m*2,2):
    edges[pairs[i]].append(pairs[i+1])
    edges[pairs[i+1]].append(pairs[i])
print(edges)




 
strt_time = []; finish_time= []
strt_time = []; finish_time= []
strt_time = []; finish_time= []
strt_time = []; finish_time= []
strt_time = []; finish_time= []
strt_time = []; finish_time= []
strt_time = []; finish_time= []
strt_time = []; finish_time= []
strt_time = []; finish_time= []
strt_time = []; finish_time= []
strt_time = []; finish_time= []
strt_time = []; finish_time= []
strt_time = []; finish_time= []
strt_time = []; finish_time= []
phi = [-2]*(n+1); phi[0]=-1
t = 0


for i in range(n):
    if not label[i]:
        dfs(i,t)

print("NODES :       :",end='     ')
for i in range(n):
    print(i,end=' ')
print()


print("Phi           :",end='     ')
for i in range(n):
    print(phi[i],end=' ')
print()

print("strt_time     :",end='     ')
for i in range(n):
    print(strt_time[i],end=' ')
print()


print("finish_time   :",end='     ')
for i in range(n):
    print(finish_time[i],end=' ')
print()



