class Node:
    def __init__(self, next=None , val=None):
        self.next = next
        self.val = val

def is_palindrome(head):
    fast = slow = head

    # slow will be at middle node when fast reached last node or None
    while fast and fast.next:
        slow, fast = slow.next , fast.next.next
    
    # reverse the second half so that we can campare the two halves 
    # as if two seperate linked list
    before = None
    while slow:
        tmp = slow.next
        slow.next = before
        before = slow
        slow = tmp

    # h1 , h2
    h1 , h2 = head , before
    while h2:
        if h1.val != h2.val:
            return False
        h1 , h2 = h1.next, h2.next
    return True

_ = int(input())
input_list = input().split()
#Creating a linked list
if input_list:
    tmp = head = Node(val = input_list[0])
else:
    head = Node()

for i in input_list[1:]:
    new_node = Node(val = i)
    tmp.next = new_node
    tmp = new_node

print(is_palindrome(head))