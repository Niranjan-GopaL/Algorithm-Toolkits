from collections import deque

class Node:
	# Utility to create new node
	def __init__(self , val):
		self.val = val
		self.l = None
		self.r = None

def minDepth_recursive(root):
	# Corner Case.Should never be hit unless the code is
	# called on root = NULL
	if root is None:
		return 0
	
	# Base Case : Leaf node.This accounts for height = 1
	if root.l is None and root.r is None:
		return 1
	
	# If l subtree is Null, recur for r subtree
	if root.l is None:
		return minDepth_recursive(root.r)+1
	
	# If r subtree is Null , recur for l subtree
	if root.r is None:
		return minDepth_recursive(root.l) +1
	
	return min(minDepth_recursive(root.l), minDepth_recursive(root.r))+1


def minDepth_iterative(root):
	if root is None:
		return 0
	q = deque()
	q.append({'node': root , 'depth' : 1})

	while(len(q)>0):
		# Remove the front queue item
		curr = q.popleft()
	
		# Get details of the removed item
		node = curr['node']
		depth = curr['depth']
		# If this is the first leaf node seen so far
		# then return its depth as answer
		if node.l is None and node.r is None:
			return depth
		
		# If l subtree is not None, add it to queue
		if node.l:
			q.append({'node' : node.l , 'depth' : depth+1})

		# if r subtree is not None, add it to queue
		if node.r:
			q.append({'node': node.r , 'depth' : depth+1})

root = Node(3)
root.l = Node(9)
root.r = Node(20)
root.r.l = Node(15)
root.r.r = Node(7)


right = Node(1)
right.r= Node(1)
right.r.r= Node(1)
right.r.r.r= Node(1)
right.r.r.r.r= Node(1)
right.r.r.r.r.r= Node(1)

print (minDepth_iterative(root))
print (minDepth_recursive(right))
