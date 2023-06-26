from collections import deque

n = int(input())
m = int(input())

'''
3
3
1 2 2 3 3 1

1 2 3
W


4
2
1 2 3 4

1 2 1 2
W

4
6
1 2 2 3 3 4 4 1 1 3 2 4

1 2 3 4
W (sort the adjacent elements)
'''


edges = [ [] for _ in range(n+1)]
# label will act as the vistited array
label = [0]*(n+1)
pairs = list(map(int,input().split()))
for i in range(0,m*2,2):
    edges[pairs[i]].append(pairs[i+1])
    edges[pairs[i+1]].append(pairs[i])
print(edges)


for i in range(1,n+1):
    if not label[i]:
        q = deque([i])

        while q:
            print("\n---------Queue iteration--------------")
            x = q.popleft()
            print(f' x : {x}')
            options = [1,2,3,4]

            for y in edges[x]:
                if label[y]: options.remove(label[y])

            print(f"options x had was : {options}")
            label[x] = options[0]
            print(f"label[{x}] : {label[x]}")

            for y in edges[x]:
                if not label[y]:q.append(y)
            print(f'queue : {q}')
            print("--------------------------------------\n")

for i in range(1,n+1):
    print(label[i],end=' ')