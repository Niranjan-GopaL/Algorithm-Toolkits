from collections import deque 

def bfs(i,j):
    queue=deque()
    queue.append((i,j))
    visited.add((i,j))
    while queue:
        r,c=queue.popleft()
        directions=[(0,1),(0,-1),(1,0),(-1,0)]
        for dr,dc in directions:
            row,col=r+dr,c+dc
            if row in range(m) and col in range(n) and grid[row][col]=='1' and (row,col) not in visited:
                queue.append((row,col))
                visited.add((row,col))

n = int(input())
m = int(input())

grid = []

for _ in range(n):
    row = list(map(int,input().split()))
    grid.append(row)


visited=set()
c=0

for i in range(m):
    for j in range(n):
        if grid[i][j] and (i,j) not in visited:
            c+=1
            bfs(i,j)

print(c)