# Much easier to understand
def dfs(i):
    global t # we can refer to global variable lists no problem, but for int, you need to make it global
    label[i] = 1
    t+=1; strt_time[i]= t
    for x in edges[i]:
        if not label[x]:
            phi[x]=i
            dfs(x)
    t+=1; finish_time[i]=t


    
def stack_dfs(i):
    t = 0
    st = [i]
    while st:
        x = st.pop()

        if not label[x]:
            label[x] = 1; t+=1
            strt_time[x]=t
            for y in edges[x]:
                if not label[y]:
                    phi[y]=x
                    st.append(y)
        else:
            if finish_time[x] == 0:
                t+=1; finish_time[x] = t





''' TEST CASES
7
10
0 1 0 2 0 3 1 3 3 2 2 4 4 5 5 6 6 4 6 7
'''

# normal inputing and storing graphs

# n = int(input())
# m = int(input())

# # creating adjacency list
# edges = [ [] for _ in range(n)]
# label = [0]*(n)

# pairs = list(map(int,input().split()))
# for i in range(0,m*2,2):
#     edges[pairs[i]].append(pairs[i+1])
#     edges[pairs[i+1]].append(pairs[i])
# print(edges)



n = 8
label = [0]*(n)
edges = [[1, 2, 3], [0, 3], [0, 3, 4], [0, 1, 2], [2, 5, 6], [4, 6], [5, 4, 7], [6]]

 
t = 0
strt_time = [0]*n; finish_time= [0]*(n)
phi = [-2]*n; phi[0]="_"   

for i in range(n):
    if not label[i]:
        dfs(i)

# print stuff
print();print();print()
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




for i in range(n):
    if not label[i]:
        stack_dfs(i)



# print stuff
print();print();print()
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



