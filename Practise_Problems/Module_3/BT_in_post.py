# Using hashing (efficient)

# Python3 program to construct tree using inorder
# and postorder traversals

# A binary tree node has data, pointer to left
# child and a pointer to right child


class Node:

	def __init__(self, x):

		self.data = x
		self.left = None
		self.right = None

# Recursive function to construct binary of size n
# from Inorder traversal in[] and Postorder traversal
# post[]. Initial values of inStrt and inEnd should
# be 0 and n -1. The function doesn't do any error
# checking for cases where inorder and postorder
# do not form a tree


def buildUtil(inn, post, innStrt, innEnd):

	global mp, index

	# Base case
	if (innStrt > innEnd):
		return None

	# Pick current node from Postorder traversal
	# using postIndex and decrement postIndex
	curr = post[index]
	node = Node(curr)
	index -= 1

	# If this node has no children then return
	if (innStrt == innEnd):
		return node

	# Else find the index of this node inn
	# Inorder traversal
	iIndex = mp[curr]

	# Using index in Inorder traversal,
	# construct left and right subtrees
	node.right = buildUtil(inn, post,
						iIndex + 1, innEnd)
	node.left = buildUtil(inn, post, innStrt,
						iIndex - 1)

	return node

# This function mainly creates an unordered_map,
# then calls buildTreeUtil()


def buildTree(inn, post, lenn):

	global index

	# Store indexes of all items so that we
	# we can quickly find later
	for i in range(lenn):
		mp[inn[i]] = i

	# Index in postorder
	index = lenn - 1
	return buildUtil(inn, post, 0, lenn - 1)

# This function is here just to test


def preOrder(node):

	if (node == None):
		return

	print(node.data, end=" ")
	preOrder(node.left)
	preOrder(node.right)


# Driver Code
if __name__ == '__main__':

	inn = [4, 8, 2, 5, 1, 6, 3, 7]
	post = [8, 4, 5, 2, 6, 7, 3, 1]
	n = len(inn)
	mp, index = {}, 0

	root = buildTree(inn, post, n)

	print("Preorder of the constructed tree :")
	preOrder(root)



# Using stacks and sets 


# Python program for above approach

# A binary tree node has data, pointer
# to left child and a pointer to right
# child


class Node:
	def __init__(self, x):
		self.data = x
		self.left = None
		self.right = None

# Tree building function


def buildTree(inorder, post, n):
	# Create Stack of type Node
	st = []
	# Create Set of type Node
	set = []
	# Initialise postIndex with n - 1
	postIndex = n - 1
	# Initialise root with NULL
	root = None

	p = n-1
	i = n-1

	while p >= 0:
		# Initialise node with NULL
		node = None

		# Run loop
		while True:

			# initialize new node
			node = Node(post[p])

			# check if root is equal to null
			if root == None:
				root = node

			# If size of set is greater than 0
			if len(st) > 0:

				# If st top is present in the set s
				if st[-1] in set:
					set.remove(st[-1])
					st[-1].left = node
					st.pop()
				else:
					st[-1].right = node

			st.append(node)

			p -= 1
			if post[p+1] == inorder[i] or p < 0:
				break

		node = None

		# If the stack is not empty and st top data is equal to in[i]
		while len(st) > 0 and i >= 0 and st[-1].data == inorder[i]:
			node = st[-1]
			# Pop elements from stack
			st.pop()
			i -= 1

		# if node not equal to None
		if node != None:
			set.append(node)
			st.append(node)

	# Return root
	return root

# for print preOrder Traversal


def preOrder(node):
	if node == None:
		return
	print(node.data, end=" ")
	preOrder(node.left)
	preOrder(node.right)


# Driver Code
if __name__ == '__main__':
	inorder = [4, 8, 2, 5, 1, 6, 3, 7]
	post = [8, 4, 5, 2, 6, 7, 3, 1]
	n = len(inorder)

	# Function Call
	root = buildTree(inorder, post, n)

	print("Preorder of the constructed tree :")

	# Function Call for preOrder
	preOrder(root)