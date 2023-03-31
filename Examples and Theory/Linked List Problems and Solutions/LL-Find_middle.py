class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value , end = ' ')
            temp = temp.next
        print()
        
    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    # WITHOUT USING LENGHT , cuz we'll ONLY be given head of the LL in interviews


    def get_middle_slow(self):
        # If lenght was not an attribute then 
        # we would have to traverse the list once to find length
        # and then run the below code , so it would have been O(n) + O(n//2)
        mid = (self.length // 2 ) + 1
        node = self.head
        for _ in range(1,mid):
            node = node.next
        return node

    def get_middle_fast(self):
        fast = self.head
        slow = self.head
        while fast and fast.next :
            slow = slow.next
            fast = fast.next.next
        return slow
    
my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)

my_linked_list.print_list()
print(my_linked_list.get_middle_slow().value)
print(my_linked_list.get_middle_fast().value)
