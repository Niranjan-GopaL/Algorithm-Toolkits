class Node:
    def __init__(self, next=None , val=None):
        self.next = next
        self.val = val
    
def combine_two_linked_list_sorted_to_single(head_1, head_2):
    tail = tmp_pointer_to_head = Node()

    while head_1 and head_2:
        if head_1.val < head_2.val:
            tail.next = head_1
            head_1 = head_1.next
        else:
            tail.next = head_2
            head_2 = head_2.next
        tail = tail.next
    else:
        if head_1:
            tail.next = head_1
        if head_2:
            tail.next = head_2
    return tmp_pointer_to_head.next


k = int(input())
linked_lists = []

for _ in range(k):
    __ = input()
    input_list = list(map(int, input().split())) 

    #Creating a linked list
    tmp = head = Node(val = input_list[0]) if input_list else Node()
    
    for i in input_list[1:]:
        new_node = Node(val = i)
        tmp.next = new_node
        tmp = new_node

    # appending to the list of linked lists
    linked_lists.append(head)

# MASTERPIECE
while len(linked_lists) > 1:
    merged_lists = []
    
    for i in range(0, len(linked_lists), 2):
        head_1 = linked_lists[i]
        if (i+1) < len(linked_lists): # handling what happens at the end
            head_2 = linked_lists[i+1]
        else:
            head_2 = None
        merged_lists.append(combine_two_linked_list_sorted_to_single(head_1, head_2))
    
    linked_lists = merged_lists

head = linked_lists[0]
while head:
    print(head.val,end = ' ')
    head = head.next