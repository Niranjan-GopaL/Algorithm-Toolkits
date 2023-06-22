import pyautogui as p
import time

time.sleep(7)
p.typewrite(
'''


visited=set()
c=0

for i in range(m):
    for j in range(n):
        if grid[i][j] and (i,j) not in visited:
            c+=1
            bfs(i,j)

print(c)

'''
)
p.typewrite(['enter'])
