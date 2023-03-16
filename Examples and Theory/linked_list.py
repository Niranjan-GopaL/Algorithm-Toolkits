# class Node:
    ## WRITE NODE CONSTRUCTOR HERE ##
    #                               #
    #                               #
    #                               #
    #                               #
    #################################
        
# class LinkedList:
    ## WRITE LL CONSTRUCTOR HERE ##
    #                             #
    #                             #
    #                             #
    #                             #
    ###############################

"""
    EXPECTED OUTPUT:
    ----------------
    Head: 4
    Tail: 4
    Length: 1
    
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self,value):
        first_node = Node(value)
        self.head = first_node
        self.tail = first_node
        self.length = 1

    def append(self, value):
        # O(1) 
        last_node = Node(value)
        temp = self.tail
        self.tail = last_node
        temp.next = last_node
        if self.length == 0:
            self.head = last_node
        self.length += 1


    def prepend(self, value):
        # O(1)
        first_node = Node(value)
        first_node.next = self.head
        self.head = first_node
        if self.length == 0:
            self.tail = first_node
        self.length += 1

    def pop(self):
        # O(n) so in order to pop an element we need to traverse the linked list
        node = self.head
        old_tail = self.tail

        if self.length == 0:
            return None
        
        elif self.length == 1:
            self.head = None
            self.tail = None
            self.length -= 1 
            return node.value
        
        else:
            while node:
                if node.next == self.tail:
                    self.tail = node
                    node.next = None
                    self.length -= 1
                    return old_tail.value
                node = node.next

    def popfirst(self):
        if self.length == 0:
            return None
        elif self.length == 1:
            self.head = None
            self.tail = None
            self.length -= 1 
            return self.head
        else:
            temp = self.head
            self.head = self.head.next
            temp.next = None
            self.length -= 1 
            return temp.value


    def print_list(self):
        node = self.head
        if self.length == 0:
            print(None)
            return
        while node:
            print(node.value, end=" ")
            node = node.next

    def get_at_index(self, index):
        i = 0
        if index > 0 or index < self.length:
            node = self.head
            while node:
                if i == index:
                    return node.value
                i += 1
                node = node.next
        else:
            return None

# Creating a linked list
my_linked_list = LinkedList(0)

# Performing operations on the linked list
my_linked_list.append(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)

my_linked_list.prepend(5)
my_linked_list.prepend(6)
my_linked_list.prepend(7)
my_linked_list.prepend(8)

print(my_linked_list.get_at_index(2))
print(my_linked_list.get_at_index(-1))
print(my_linked_list.get_at_index(7))

print(my_linked_list.pop())
print(my_linked_list.pop())
print(my_linked_list.pop())

print(my_linked_list.popfirst())
print(my_linked_list.popfirst())
print(my_linked_list.popfirst())

print()
my_linked_list.print_list()

print("\n")

# When linked list is empty both head and tail are None , so this will throw attribute error
# since Node has the value attribute , None doesn't
print('Head:', my_linked_list.head.value)
print('Tail:', my_linked_list.tail.value)
print('Length:', my_linked_list.length)
    

                                                                                                                    