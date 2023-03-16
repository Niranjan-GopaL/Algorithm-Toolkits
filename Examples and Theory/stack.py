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
        pass