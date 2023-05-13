# EFFICIENT ------------------------------------------------------------------------------------------------------------------------------------->
class Node:
	
	def __init__(self, x):
		
		self.data = x
		self.left = None
		self.right = None

# Recursive function to construct binary of size
# len from Inorder traversal in[] and Preorder traversal
# pre[]. Initial values of inStrt and inEnd should be
# 0 and len -1. The function doesn't do any error
# checking for cases where inorder and preorder
# do not form a tree
def buildTree1(inn, pre, inStrt, inEnd):
	
	global preIndex, mp

	if (inStrt > inEnd):
		return None

	# Pick current node from Preorder traversal
	# using preIndex and increment preIndex
	curr = pre[preIndex]
	preIndex += 1
	tNode = Node(curr)

	# If this node has no children then return
	if (inStrt == inEnd):
		return tNode

	# Else find the index of this
	# node in Inorder traversal
	inIndex = mp[curr]

	# Using index in Inorder traversal,
	# construct left and right subtress
	tNode.left = buildTree1(inn, pre, inStrt,
						inIndex - 1)
	tNode.right = buildTree1(inn, pre, inIndex + 1,
							inEnd)

	return tNode

# This function mainly creates an
# unordered_map, then calls buildTree1()
def buldTreeWrap(inn, pre, lenn):
	
	global mp
	
	# Store indexes of all items so that we
	# we can quickly find later
	# unordered_map<char, int> mp;
	for i in range(lenn):
		mp[inn[i]] = i

	return buildTree1(inn, pre, 0, lenn - 1)

# This function is here just to test buildTree1()
def printInorder(node):

	if (node == None):
		return
		
	printInorder(node.left)
	print(node.data, end = " ")
	printInorder(node.right)

if __name__ == '__main__':
	
	mp = {}
	preIndex = 0

	inn = [ 'D', 'B', 'E', 'A', 'F', 'C' ]
	pre = [ 'A', 'B', 'D', 'E', 'C', 'F' ]
	lenn = len(inn)

	root = buldTreeWrap(inn, pre,lenn)

	# Let us test the built tree by printing
	# Inorder traversal
	print("Inorder traversal of "
		"the constructed tree is")
	
	printInorder(root)





"""Recursive function to construct binary of size len from
Inorder traversal in[] and Preorder traversal pre[]. Initial values
of inStrt and inEnd should be 0 and len -1. The function doesn't
do any error checking for cases where inorder and preorder
do not form a tree """
def buildTree(inOrder, preOrder, inStrt, inEnd):
	
	if (inStrt > inEnd):
		return None

	# Pick current node from Preorder traversal using
	# preIndex and increment preIndex
	tNode = Node(preOrder[buildTree.preIndex])
	buildTree.preIndex += 1

	# If this node has no children then return
	if inStrt == inEnd :
		return tNode

	# Else find the index of this node in Inorder traversal
	inIndex = search(inOrder, inStrt, inEnd, tNode.data)
	
	# Using index in Inorder Traversal, construct left
	# and right subtrees
	tNode.left = buildTree(inOrder, preOrder, inStrt, inIndex-1)
	tNode.right = buildTree(inOrder, preOrder, inIndex + 1, inEnd)

	return tNode

# UTILITY FUNCTIONS
# Function to find index of value in arr[start...end]
# The function assumes that value is present in inOrder[]

def search(arr, start, end, value):
	for i in range(start, end + 1):
		if arr[i] == value:
			return i

def printInorder(node):
	if node is None:
		return
	
	# first recur on left child
	printInorder(node.left)
	
	# then print the data of node
	print (node.data,end=' ')

	# now recur on right child
	printInorder(node.right)
	
# Driver program to test above function
inOrder = ['D', 'B', 'E', 'A', 'F', 'C']
preOrder = ['A', 'B', 'D', 'E', 'C', 'F']
# Static variable preIndex
buildTree.preIndex = 0
root = buildTree(inOrder, preOrder, 0, len(inOrder)-1)

# Let us test the build tree by printing Inorder traversal
print ("Inorder traversal of the constructed tree is")
printInorder(root)








