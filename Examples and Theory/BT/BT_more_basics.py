from collections  import deque

class Node:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

# 


# path to a node

#  iterative version of BT construction from lvl order traversal
def buildTree_from_lvl_order_traversal(nums):
	if not nums:
		return None
	root = Node(nums[0])
	q = deque() 
	q.append(root)
	# to keep track of where we are in the array
	i = 1
	
	while i < len(nums):
		curr = q.popleft()
		# adding next element in nums as left
		if i < len(nums):
			if nums[i] != 'null':
				curr.left = Node(nums[i])
				q.append(curr.left)
			i += 1
		# adding next element in nums as left
		if i < len(nums):
			if nums[i] != 'null':
				curr.right = Node(nums[i])
				q.append(curr.right)
			i += 1
	return root


# construct tree from post and in


# construct tree from pre and in


def printTree(root):
	if not root:
		return
	print(root.val, end=" ")
	printTree(root.left)
	printTree(root.right)



nums = [1, 2, 3, "null", 5, "null", 6, 6, 6]
root = buildTree_from_lvl_order_traversal(nums)
printTree(root)
