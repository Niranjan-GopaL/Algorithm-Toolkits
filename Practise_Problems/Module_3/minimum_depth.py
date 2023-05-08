class Node:
	def __init__(self , key):
		self.val = key
		self.l = None
		self.right = None

def minDepth(root):
	# Corner Case.Should never be hit unless the code is
	# called on root = NULL
	if root.val == None:
		return 0
	
	# Base Case : Leaf node.This accounts for height = 1
	if root.l is None and root.right is None:
		return 1
	
	# If l subtree is Null, recur for right subtree
	if root.l is None:
		return minDepth(root.right)+1
	
	# If right subtree is Null , recur for l subtree
	if root.right is None:
		return minDepth(root.l) +1
	
	return min(minDepth(root.l), minDepth(root.right))+1
	
root = Node(1)
root.l = Node(2)
root.right = Node(3)
root.l.l = Node(4)
root.l.right = Node(5)
print (minDepth(root))