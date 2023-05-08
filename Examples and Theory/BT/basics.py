class Node:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

def buildTree(nums):
	if not nums:
		return None
	root = Node(nums[0])
	q = [root]
	i = 1
	while i < len(nums):
		curr = q.pop(0)
		if i < len(nums):
			curr.left = Node(nums[i])
			q.append(curr.left)
			i += 1
		if i < len(nums):
			curr.right = Node(nums[i])
			q.append(curr.right)
			i += 1
	return root

def printTree(root):
	if not root:
		return
	printTree(root.left)
	print(root.val, end=" ")
	printTree(root.right)

nums = [1, 2, 3, 4, 5, 6, 6, 6, 6]
root = buildTree(nums)
printTree(root)
