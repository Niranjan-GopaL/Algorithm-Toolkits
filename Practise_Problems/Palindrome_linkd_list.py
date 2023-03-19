class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        
    def prepend(self, value):
        # O(1)
        first_node = Node(value)
        first_node.next = self.head
        self.head = first_node
        if self.length == 0:
            self.tail = first_node
        self.length += 1
    
    def create_rev_LL(self):
        node = self.head
        new_LL = LinkedList()
        while node:
            new_LL.prepend(node.value)
            node = node.next
        return new_LL

def is_Palindromic(linked_list):
    head1 = linked_list.head
    head2 = linked_list.create_rev_LL().head
    for i in range(linked_list.length // 2):
        if head1.value != head2.value:
            print("false")
            return
        else:
            head1 = head1.next
            head2 = head2.next
    print("true")


test_cases = int(input())
linked_lists = []

for _ in range(test_cases):
    input_list = list(map(int, input().split(' '))) 
    # creating the given linked list
    linked_list = LinkedList()
    for i in input_list[:-1]:
        linked_list.append(i)
    linked_lists.append(linked_list)


for linked_list in linked_lists:
    is_Palindromic(linked_list)

# handle for 0 test cases later