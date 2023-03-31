'''
For a normal List:

        0 1 2 3 4 5 6
        A B C D E F G 
        ^           ^
        |           |
    Adding,          Adding,
    Poping          Poping
    is O(n)         is O(1)

    
For a linked list:

        0 1 2 3 4 5 6
        A B C D E F G 
        ^           ^
        |           |
    Adding          Adding
    is O(1)         is O(1)                        
    Poping          Poping
    is O(1)         is O(n)
'''


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    # Stack implementation using a linked list
    def __init__(self,value):
        first_node = Node(value)
        self.top = first_node
        self.height = 1

    def push(self, value):
        first_node = Node(value)
        first_node.next = self.top
        self.top = first_node
        self.length += 1

    def pop(self):
        if self.height == 0:
            return None
        elif self.height == 1:
            self.top = None
            self.height -= 1 
            return self.top
        else:
            temp = self.top
            self.top = self.top.next
            temp.next = None
            self.height -= 1 
            return temp.value
        

    def print_stack(self):
        node = self.top
        if self.height == 0:
            print(None)
            return
        while node:
            print(node.value, end=" ")
            node = node.next
        print()