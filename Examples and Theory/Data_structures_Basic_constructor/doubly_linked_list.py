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

    def print_DLL(self):
        node = self.head
        if self.length == 0:
            print(None)
            return
        while node:
            print(node.value, end=" ")
            node = node.next

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
    

    def pop(self):
        # O(n) so in order to pop an element we need to traverse the linked list
        node = self.head

        if self.length == 0:
            return None
        
        elif self.length == 1:
            self.head = None
            self.tail = None
            self.length -= 1 
            return node.value
        
        else:
            previous_tail = self.tail
            self.tail = previous_tail.prev
            self.tail.next = None
            previous_tail.prev = None
            self.length -= 1
            return previous_tail
    
    def popfirst(self):
        if self.length == 0:
            return None
        elif self.length == 1:
            self.head = None
            self.tail = None
            self.length -= 1 
            return self.head
        else:
            prev_node = self.head
            self.head = prev_node.next
            prev_node.next = None
            self.length -= 1 
            return prev_node.value
        

    def get_at_index(self, index):
        # DLL indexing is assumed to start at 0
        if index >= 0 or index <= self.length-1:
            node = self.head
            # while node:                   CUMBERSOME
            #     if i == index:
            #         return node.value
            #     i += 1
            #     node = node.next
            '''
                MUCH MORE ELEGENT

            for _ in range(index):
                node = node.next
            return node

            But since this is a DLL we can optimize it.
            '''
            if index <= self.length //2 :
                for _ in range(index):
                    node = node.next
                return node
            else:
                tail = self.tail
                for _ in range(self.length - index - 1):
                    tail = tail.prev
                return tail
                # Normally you would have required the comparison but in above for loop NOPE
                # for i in range(self.length - 1,0,-1):
                    # if i == index:
            
        else:
            return None
        
    def set_at_index(self, index, value_to_set):
        # DLL indexing is assumed to start at 0
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
        # YOU CAN RE-USE YOUR CODE!!!!!!!!!!!!!!!!!
        node = self.get_at_index(index)
        print(node.value)
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
            # making important references
            prev_node = self.get_at_index(index-1)
            node_at_that_index = prev_node.next

            # creating a new node
            prev_node.next = new_node = Node(value_to_insert)

            # rearranging the links
            new_node.next = node_at_that_index
            new_node.prev = prev_node
            node_at_that_index.prev = new_node

            self.length += 1
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
            next_node.prev = previous_node
            node_to_remove.next = None
            node_to_remove.prev = None

            self.length -= 1
            return True
        else:
            return False




my_DLL = DoublyLinkedList(1)

my_DLL.append(2)
my_DLL.append(3)
my_DLL.append(4)
my_DLL.append(5)

my_DLL.prepend(3)
my_DLL.prepend(10)

my_DLL.print_DLL()
print("\n")

my_DLL.pop()
my_DLL.pop()
my_DLL.print_DLL()

print("\n")
my_DLL.popfirst()
my_DLL.popfirst()
my_DLL.print_DLL()
print("\n")


'''
Little more debugging to do in get index functions.

suspicion : while popping the last elem is still point to element that was popped. and that is why

'''


print(my_DLL.get_at_index(0).value)
print(my_DLL.get_at_index(1).value)
print(my_DLL.get_at_index(2).value)
print("\n")

print(my_DLL.set_at_index(2,100))
print(my_DLL.set_at_index(3,101))
my_DLL.print_DLL()
print("\n")

my_DLL.insert_at_index(0,100000)
my_DLL.insert_at_index(3,10000)



my_DLL.print_DLL()