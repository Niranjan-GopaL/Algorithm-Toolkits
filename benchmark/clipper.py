import pyautogui as p
import time

time.sleep(7)
p.typewrite(
'''
class Node:
    def __init__(self,val):
        self.val = val
        self.l = None
        self.r = None

def build(arr,i,n):
    if i>=n :return None

    root = Node(arr[i])
    root.l = build(arr,2*i+1)
    root.r = build(arr,2*i+2)

    return root

def kthSmallest(root, k):
    n=0
    stack=[]
    cur=root
    while cur or stack :
        while cur :
            stack.append(cur)
            cur=cur.left
        cur=stack.pop()
        n +=1
        if n==k :
            return cur.val
        cur = cur.right

l = input().split()
k = int(input())
l = [int(i) for i in l if i != 'null']
root = build(l,0,len(l))
print(kthSmallest(root, k))'''
)
p.typewrite(['enter'])
