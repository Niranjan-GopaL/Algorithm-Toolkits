from collections import deque 



def is_valid(row,column):
    if row in range(m) and column in range(n):
        return True
    return False




# MUCHHHHHH SIMPLER AND EASIER !!!!
directions=[(0,1),(0,-1),(1,0),(-1,0)]

def dfs(i,j):
    if is_valid(i,j) and grid[i][j]:
        grid[i][j]=0
        for dr,dc in directions:
            new_row, new_col = i+dr, j+dc
            dfs(new_row,new_col)









def bfs(i,j):
    queue=deque();queue.append((i,j))

    visited.add((i,j))

    while queue:
        (r,c) = queue.popleft()
        directions=[(0,1),(0,-1),(1,0),(-1,0)]

        for dr,dc in directions:
            new_row, new_col = r+dr, c+dc

            if is_valid(new_row ,new_col)   and\
            grid[new_row][new_col]          and\
            (new_row,new_col) not in visited:  
                
                queue.append((new_row,new_col))
                visited.add((new_row,new_col))


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
            # all the connected islands are traversed in one bfs() call
            bfs(i,j)
            c+=1

print(c)