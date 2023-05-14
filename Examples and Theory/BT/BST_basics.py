import math
from collections import deque


class Node:
    def __init__(self,val):
        self.val = val
        self.l = None
        self.r = None

def LCA(root,a,b):
    curr = root

    while curr:
        if a.val > curr.val and b.val > curr.val:
            curr = curr.right 
        elif a.val < curr.val and b.val < curr:
            curr = curr.left
        else:
            return curr




root = Node(1)

root.l = Node(2)
root.r = Node(3)

root.l.l = Node(4)
root.l.r = Node(5)
root.r.l = Node(6)
root.r.r = Node(7)

root.l.l.l = Node(8)
root.l.l.r = Node(9)
root.l.r.l = Node(10)
root.l.r.r = Node(11)

root.r.l.l = Node(12)
root.r.l.r = Node(13)
root.r.r.l = Node(14)
root.r.r.r = Node(15)


Query = input(input())
for (q1,q2) in Query:
    print(LCA(root,q1,q2))