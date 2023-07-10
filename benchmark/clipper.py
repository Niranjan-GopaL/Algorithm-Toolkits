import pyautogui as p
import time

time.sleep(7)
p.typewrite(
'''
def union(u,v):

u = find(u)  
v = find(v)  

if u != v:

if sz[u] < sz[v]:
u,v = v,u

parent[v] = u
sz[u] += sz[v]
'''
)
p.typewrite(['enter'])
