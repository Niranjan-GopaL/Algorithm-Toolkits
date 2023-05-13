import math
from collections import deque


class Node:
    def __init__(self,val):
        self.val = val
        self.l = None
        self.r = None


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


def inorder(root , inorder_list):
    if root is None:
        return None 
    inorder(root.l , inorder_list)
    inorder_list.append(root.val)
    inorder(root.r, inorder_list)


def helper2(root ,nums):
    if not nums  :
        return None 
    
    index = nums.index(max(nums))
    root =  Node(nums[index]) 

    root.l = helper2(root.l , nums[:index])
    root.r = helper2(root.r , nums[index+1 :])

    return root 



def printTree(root):
	if not root:
		return
	print(root.val, end=" ")
	printTree(root.l)
	printTree(root.r)



nums = [5, 2, 4, "null", 1]
root = buildTree_from_lvl_order_traversal(nums)
# printTree(root)
val = int(input())


inorder_list = []
inorder(root, inorder_list)
inorder_list.append(val)

print(inorder_list)

root = helper2(None , inorder_list)
printTree(root)
