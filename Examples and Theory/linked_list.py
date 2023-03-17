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

# you get INSANELY CONFUSED between append and prependf

    def append(self, value):
        # O(1) 
        last_node = Node(value)
        temp = self.tail
        self.tail = last_node
        temp.next = last_node
        if self.length == 0:
            self.head = last_node
        self.length += 1
        return True


    def prepend(self, value):
        # O(1)
        first_node = Node(value)
        first_node.next = self.head
        self.head = first_node
        if self.length == 0:
            self.tail = first_node
        self.length += 1
        return True

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
        # Linked lsit indexing is assumed to start at 0
        i = 0
        if index >= 0 or index <= self.length-1:
            node = self.head
            while node:
                if i == index:
                    return node.value
                i += 1
                node = node.next
        else:
            return None
        

    def set_at_index(self, index, value_to_set):
        # Linked lsit indexing is assumed to start at 0
        '''
        i = 0
        if index >=0 or index <= self.length-1:
            node = self.head
            while node:
                if i == index:
                    node.value = value_to_set
                    return
        else:
            return None
        '''
        # Better solution 
        # YOU CAN RE USE YOUR CODE!!!!!!!!!!!!!!!!!
        node = self.get_at_index(index)
        if node:
            node.value = value_to_set
            return True
        else:
            return False
        
    def insert_at_index(self, index, value_to_insert):
        if index >= 0 or index <= self.length-1:
            if index == 0:
                # self.lenght += 1 ON PREPENDING THE LENGTH IS ALREADY INCREMENTED
                # so the above is unnecessary , it would have double counted 
                return self.prepend(value_to_insert)
            node = self.get_at_index(index-1)
            temp = node.next
            node.next = Node(value_to_insert)
            node.next.next = temp
            self.lenght += 1
            return True
        else:
            return False
        

    def remove_at_index(self, index):
        if index >= 0 or index <= self.length-1:
            if index == 0:
                return self.popfirst()
            if index == self.length-1:
                return self.pop()
            
            previous_node = self.get_at_index(index-1)
            node_to_remove = previous_node.next
            next_node = node_to_remove.next

            previous_node.next = next_node
            node_to_remove.next = None

            self.length -= 1
            return True
        else:
            return False
        

    def reverse(self):
        # HOLY GRAIL!!!!
        self.head, self.tail = self.tail, self.head
        current_node = self.head
        after = current_node.next
        before = None

        '''
        for _ in range(self.length):# We reverse the link as many times as the elements in the list
        #  or while(current_node):
            current_node.next = before
            before = current_node
            current_node = after
            after = after.next

        This was why first thought. BUT THIS FAILS AT THE LAST iteration.
        If lenght = 3 , after each iteration (of the 3 total iterations) 
        each links has to be reversed.

        But this fails at the last iteration. since after would be None 
        and None.next would yield error.


        BUT KEY TAKEAWY :  the loop adtually reverses the links except at the last iterations.
        IN THESE SITUATIONS JUST SEE IF YOU CAN RE-ARRANGE THE OPERATIONS IN FOR LOOP.
        '''

        for _ in range(self.length):
            after = current_node.next    
            current_node.next = before
            before = current_node
            current_node = after

    



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
    

                                                                                                                      