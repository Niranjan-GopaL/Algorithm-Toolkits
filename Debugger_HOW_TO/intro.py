
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
        if self.length == 0:
            self.head = last_node
        self.length += 1

    # def append(self, value):
    #     new_node = Node(value)
    #     if self.head is None:
    #         self.head = new_node
    #         self.tail = new_node
    #     else:
    #         self.tail.next = new_node
    #         self.tail = new_node
    #     self.length += 1

    def print_list(self):
        node = self.head
        if self.length == 0:
            print(None)
            return
        while node:
            print(node.value, end=" ")
            node = node.next
        print()
        print("Length :", self.length)

    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after

   
list_ = LinkedList(12)

# Performing operations on the list

list_.append(1)
list_.append(2)
list_.append(3)
list_.append(4)



list_.print_list()

list_.reverse()

list_.print_list()                                                                                                    