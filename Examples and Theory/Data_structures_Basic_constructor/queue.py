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

So we don this to implement a queue:

    A0 -> A1 -> A2 -> A3 -> A4 -> A5 -> A6
     ^                                  ^
     |                                  |
   FIRST                               LAST

'''


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    # Queue implementation using a linked list
    def __init__(self,value):
        first_node = Node(value)
        self.first = first_node
        self.last = first_node
        self.length = 1

    def enqueue(self, value):
        # O(1) 
        last_node = Node(value)
        temp = self.last
        self.last = last_node
        temp.next = last_node
        if self.length == 0:
            self.first = last_node
        self.length += 1
        return True
    
    def dequeue(self):
        # O(1)
        if self.length == 0:
            return None
        elif self.length == 1:
            self.first = None
            self.last = None
            self.length -= 1 
            return self.first
        else:
            temp = self.first
            self.first = self.first.next
            temp.next = None
            self.length -= 1 
            return temp.value
        
    def print_queue(self):
        node = self.first
        if self.length == 0:
            print(None)
            return
        while node:
            print(node.value, end=" ")
            node = node.next  