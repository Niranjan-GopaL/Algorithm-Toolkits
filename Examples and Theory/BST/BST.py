class Node:
    def __init__(self,val):
        self.val = val
        self.l = None
        self.r = None

# lnr
def printInorder(root):
    if root:
        printInorder(root.l)
        print(root.val,end=' ')
        printInorder(root.r)

# nlr
def printPreorder(root):
    if root:
        print(root.val,end=' ')
        printPreorder(root.l)
        printPreorder(root.r)

# lrn
def printPostorder(root):
    if root:
        printPostorder(root.l)
        printPostorder(root.r)
        print(root.val,end=' ')

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
printInorder(root)
print("\n")

print("Postrder")
printPostorder(root)
print("\n")

print("Preorder")
printPreorder(root)
print("\n")