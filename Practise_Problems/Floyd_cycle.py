class Node:
    def __init__(self, next=None , val=None):
        self.next = next
        self.val = val

_ = input()
input_list = list(map(int, input().split(' '))) 

# remember the third input is the position of the node , NOT INDEX in input_list
pos = int(input())

tmp = head = Node(val = input_list[0])
for i in input_list[1:]:
    new_node = Node(val = i)
    tmp.next = new_node
    tmp = new_node

tmp2 = head
count =1
# Creating the cycle ( connecting last node to node at 'pos' position )
if pos > 0 and pos <= len(input_list):
    while tmp2:
        if count == pos:
            tmp.next = tmp2
            break
        else:
            count += 1
        tmp2 = tmp2.next

fast = slow = head
flag = 0
while fast and fast.next:
    if slow == fast:
        print("True")
        flag = 1
        break
    slow , fast = slow.next, fast.next.next

if flag == 0:
    print("False")