import math
from collections import deque


class Node:
    def __init__(self,val):
        self.val = val
        self.l = None
        self.r = None

def number_of_good_nodes(root,maxVal):
    if not root:
        return 0
    
    if root.val >= maxVal:
        return 1 + number_of_good_nodes(root.l,root.val) + number_of_good_nodes(root.r,root.val)  
    else:
        return 0 + number_of_good_nodes(root.l,maxVal) + number_of_good_nodes(root.r,maxVal)
    
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

print(number_of_good_nodes(root,-math.inf))
