from functools import reduce

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
        
    def print_list(self):
        node = self.head
        if self.length == 0:
            print(None)
            return
        while node:
            print(node.value, end=" ")
            node = node.next
        print("\n")

def combine_two_linked_list_sorted_single(linked_list_1 , linked_list_2):
    new_LL = LinkedList()

    node1 = linked_list_1.head
    node2 = linked_list_2.head

    while  node1 and  node2:
        if node1.value < node2.value:
            new_LL.append(node1.value)
            node1 = node1.next
        elif node1.value == node2.value:
            new_LL.append(node1.value)
            new_LL.append(node2.value)
            node1 = node1.next
            node2 = node2.next
        else:
            while node2:
                new_LL.append(node2.value)
                node2 = node2.next
    else:
        if node1:
            while node1:
                new_LL.append(node1.value)
                node1 = node1.next
        if node2:
            while node2:
                new_LL.append(node2.value)
                node2 = node2.next
    return new_LL

LL1 = LinkedList()

LL1.append(1)
LL1.append(2)
LL1.append(3)

LL1.print_list()

LL2 = LinkedList()

LL2.append(1)
LL2.append(32)
LL2.append(39)

LL2.print_list()

combine_two_linked_list_sorted_single(LL1, LL2).print_list()