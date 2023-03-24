class Node:
    def __init__(self, next=None , val=None):
        self.next = next
        self.val = val

input_list = list(map(int, input().split(' '))) 

# remember the third input is the position of the node , NOT INDEX in input_list
pos = int(input())

tmp = head = Node(val = input_list[0])
for i in input_list[1:]:
    new_node = Node(val = i)
    tmp.next = new_node
    tmp = new_node

tmp2 = head
count = 1
# Creating the cycle ( connecting last node to node at 'pos' position )
if pos > 0 and pos <= len(input_list):
    while tmp2:
        if count == pos:
            tmp.next = tmp2
            break
        else:
            count += 1
        tmp2 = tmp2.next

# Getting one node inside the cycle
def node_inside_loop(head):
    fast = slow = head
    while fast and fast.next:
        slow , fast = slow.next, fast.next.next
        if slow == fast:
            return slow

# we'll traverse until we find a NODE INSIDE loop WHOSE .next IS the tmp
# and remoce the cycle 
def remove_cycle(head,node_inside_loop):
    tmp = head
    node = tmp1 = node_inside_loop
    while 1:
        if node.next == tmp:
            node.next = None
            return head
        node = node.next
        if node == tmp1:
            tmp = tmp.next


remove_cycle(head,node_inside_loop(head))

while head:
    print(head.val,end = ' ')
    head = head.next


# doesn't work

# def remove_cycle(head,node_inside_loop):
#     tmp = head
#     node = tmp1 = node_inside_loop
#     node = node.next
#     while node != tmp1:
#         if node.next == tmp.next :
#             node.next = None
#             return head
#         node = node.next
#         tmp = tmp.next

