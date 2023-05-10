# A simple and tail recursive Python program to reverse
# a linked list
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
	
head1 = None

# a simple and tail-reverse function to reverse
# a linked list. prev is passed as null initially.
def reverseUtil(curr, prev):

	# if last node mark it head
	if(curr.next is None):
		global head1
		head1 = curr
		# update next to prev node
		curr.next = prev
		return
	
	# save curr.next node from recursive call
	next = curr.next
	curr.next = prev
	reverseUtil(next, curr)
	

# this function mainly calls reverseUtil()
# with prev as null
def reverse():
	global head1
	if(head1 is None):
		return
	reverseUtil(head1, None)
	
# utility function to print a linked list
def printlist(head):
	while(head is not None):
		print(head.data , end = " ")
		head = head.next
	print("")

# driver program to test above function
head1 = Node(1)
head1.next = Node(2)
head1.next.next = Node(3)
head1.next.next.next = Node(4)
head1.next.next.next.next = Node(5)
head1.next.next.next.next.next = Node(6)
head1.next.next.next.next.next.next = Node(7)
head1.next.next.next.next.next.next.next= Node(8)
	
print("Given Linked List : ")
printlist(head1)

reverse()

print("Reversed Linked List : ")
printlist(head1)