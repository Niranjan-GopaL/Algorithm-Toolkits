'''

USE your course to your adv , rememember how we append and do wother simple things like this :\
1 - > Which links move first to where 
2 - > What happens first 
3 - > what happened next

'''



class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
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
        last_node.prev = temp # ONLY NEW LINE
        if self.length == 0:
            self.head = last_node
        self.length += 1
        return True
    
    def prepend(self, value):
        # O(1)
        first_node = Node(value)
        first_node.next = self.head
        self.head.prev = first_node 
        self.head = first_node
        if self.length == 0:
            self.tail = first_node
        self.length += 1
        return True

