import math
import collections as c

class Node:
    def __init__(self,val):
        self.val = val
        self.l = None
        self.r = None

# lnr
def Inorder(root):
    if root:
        Inorder(root.l)
        print(root.val,end=' ')
        Inorder(root.r)

# nlr
def Preorder(root):
    if root:
        print(root.val,end=' ')
        Preorder(root.l)
        Preorder(root.r)

# lrn
def Postorder(root):
    if root:
        Postorder(root.l)
        Postorder(root.r)
        print(root.val,end=' ')


# <------------------------------------------------------------------------------------------------------------------------
# level order traversal  (BREADTH FIRST SEARCH)
def level(root):

    final = []

    q = c.deque()
    q.append(root)

    while q:
        qLen = len(q)
        level = []
        for i in range(qLen):
            node = q.popleft()
            # we might add null to queue
            if node:
                level.append(node.val)
                q.append(node.l)
            q.append(node.r)
        if level:
            final.append(level)

    return final




def Number_of_nodes(root):
    if root:
        # c = 1
        # c += Find_num_node(root.l)
        # c += Find_num_node(root.r)
        # return c ---------------------------------\||/
        return 1 + Number_of_nodes(root.l) + Number_of_nodes(root.r)
    else:
        return 0


# THIS IS COOL!!!!!!!!  
def Max(root):
    if root:
        return max(root.val, Max(root.l), Max(root.r))
    else:
        return -math.inf




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



print("Inorder")
Inorder(root)
print("\n")

print("Postrder")
Postorder(root)
print("\n")

print("Preorder")
Preorder(root)
print("\n")

print("Level Order Traversal")
print(level(root))
# If you wanna flatten the list then :- flat_list = [item for sublist in l for item in sublist]<TabPanel value={} index={} dir={theme.direction}>
  
print("\n")

print(f'Number of nodes :- {Number_of_nodes(root)}')