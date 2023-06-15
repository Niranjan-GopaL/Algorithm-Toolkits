from collections  import deque

class Node:
	def __init__(self, x):
		self.val = x
		self.l = None
		self.r = None



# path to a node
def path_to_node(root,target):
	pass



# iterative version of BT construction from lvl order traversal
def buildTree_from_lvl_order_traversal(nums):
	if not nums:
		return None
	root = Node(nums[0])
	q = deque() 
	q.append(root)
	# to keep track of where we are in the array
	i = 1

	while i < len(nums):
		curr = q.popl()
		# adding next element in nums as l
		if i < len(nums):
			if nums[i] != 'null':
				curr.l = Node(nums[i])
				q.append(curr.l)
			i += 1
		# adding next element in nums as l
		if i < len(nums):
			if nums[i] != 'null':
				curr.r = Node(nums[i])
				q.append(curr.r)
			i += 1
	return root

# BEST WAY TO CREATE BT from lvl order traversal
def build_tree(arr):
    if not arr:
        return None

    # Create root node
    root = Node(arr[0])

    # Traverse the array and build the tree
    n = len(arr)
    for i in range(n):
        # Left child index
        left_child_idx = 2 * i + 1
        # Right child index
        right_child_idx = 2 * i + 2

        # Create left child if within array bounds
        if left_child_idx < n:
            root.left = Node(arr[left_child_idx])

        # Create right child if within array bounds
        if right_child_idx < n:
            root.right = Node(arr[right_child_idx])

        # Update root to the next node
        root = root.left if root.left else root.right

    return root

# construct tree from post and in
def construct_tree_fromPostandIno(post:list, ino:list):
	# Now we can get index of any value in inorder list in O(1)
	ino_idx = {v:i for i,v in enumerate(ino)}

	def build(l,r):
		if l > r:
			return None
	
		root = Node(post.pop())

		# n_idx = ino.index(root.val) <---------- this would have taken O(n) time every time
		n_idx = ino_idx[root.val]

		root.r = build(n_idx+1,r)
		root.l = build(l,n_idx-1)

		return root

	return build(0, len(ino)-1)	



# construct tree from pre and in
def construct_tree_fromPreandIno(pre:list, ino:list):
	if not ino or not pre:
		return None

	root = Node(pre[0])
	n_idx = ino.index(root.val)

	root.l = construct_tree_fromPreandIno(pre[1:n_idx], ino[:n_idx])
	root.r = construct_tree_fromPreandIno(pre[n_idx+1:], ino[n_idx+1:])


# construct tree from pre and in
# doesn't work , still in the works of making more efficient 
def construct_tree_fromPreandIno____EfficientWay(pre:list, ino:list):
	# Now we can get index of any value in inorder list in O(1)
	ino_idx = {v:i for i,v in enumerate(ino)}

	def build(l,r):
		if l > r:
			return None
	
		root = Node(pre[l])

		# n_idx = ino.index(root.val) <---------- this would have taken O(n) time every time
		n_idx = ino_idx[root.val]

		#  l+1 to n is l subtree , n to r is r subtree  (everything in)
		root.l = build(l+1,n_idx-1)
		root.r = build(n_idx+1,r)
		return root
	
	return build(0, len(ino)-1)	



# Sum Root to Leaf 
def Root_to_Leaf(root:Node):

	def nlr(curr:Node,nums):
		if not curr:
			return None
		
		num = num*10 + curr.val

		if not curr.l and not curr.r:
			return nums
		
		return nlr(root.l,nums) + nlr(root.r,nums)

	return nlr(root,0)

	#    1
	#   / \
	#  2   3   
	# 
	# 12 + 13 = 25



# print tree
def printTree(root):
	if not root:
		return
	print(root.val, end=" ")
	printTree(root.l)
	printTree(root.r)


# io
nums = [1, 2, 3, "null", 5, "null", 6, 6, 6]
root = buildTree_from_lvl_order_traversal(nums)
printTree(root)

ino = [2,3,5,4,6]
post =  [2,5,6,4,3]
pre = [3,2,4,5,6]

root = construct_tree_fromPostandIno(post,ino)
printTree(root)

# root = construct_tree_fromPreandIno(pre,ino)
# printTree(root)