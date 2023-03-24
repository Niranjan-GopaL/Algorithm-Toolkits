class Node:
    def __init__(self, next=None , val=None):
        self.next = next
        self.val = val

input_list = list(map(int, input().split(' '))) 

# handle the case where list is empty
# apperently you can't , i.e in the input prompt if you enter 'enter'
# gives value error

#Creating a linked list
tmp = head = Node(val = input_list[0])
for node_val in input_list[1:]:
    new_node = Node(val = node_val)
    tmp.next = new_node
    tmp = new_node

# printing the lnked list
while head:
    print(head.val,end = ' ')
    head = head.next

