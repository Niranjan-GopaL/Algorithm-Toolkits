class Node:
    def __init__(self, next=None , val=None):
        self.next = next
        self.val = val

len_LL = int(input())
input_list = list(map(int, input().split(' '))) 

# remember the third input is the position of the node , NOT INDEX in input_list
pos = int(input())

tmp = head = Node(val = input_list[0])
for i in input_list[1:]:
    new_node = Node(val = i)
    tmp.next = new_node
    tmp = new_node
# After this loop tmp points to the last node

tmp2 = head
count =1
# Creating the cycle ( connecting last node to node at 'pos' position )
if pos > 0 and pos <= len_LL:
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
    slow , fast = slow.next, fast.next.next
    if slow == fast:
        print("True")
        flag = 1
        break

if flag == 0:
    print("False")