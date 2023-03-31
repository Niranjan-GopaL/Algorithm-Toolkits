# Both adding and removing from LRU is O(1)
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        # for increasing the efficiency even more i made length a 
        # property of LL instead of traversing and finding length each time
        self.length = 0

    def print_DLL(self):
        node = self.head
        if self.length == 0:
            print(None)
            return
        while node:
            print(node.val, end=" ")
            node = node.next

    def append(self, val):
        # O(1) 
        last_node = Node(val)
        temp = self.tail
        self.tail = last_node

        temp.next = last_node
        last_node.prev = temp # ONLY NEW LINE
        if self.length == 0:
            self.head = last_node
        self.length += 1

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
            return prev_node.val
        
    def get_at_index(self, index):
        # DLL indexing is assumed to start at 0
        if index >= 0 or index <= self.length-1:

            if index <= self.length //2 :
                node = self.head
                for _ in range(index):
                    node = node.next
                return node

            else:
                tail = self.tail
                for _ in range(self.length - index - 1):
                    tail = tail.prev
                return tail
        else:
            return None

class LRUCache():
    def __init__(self,capacity):
        self.capacity = capacity
        self.hash_map = {}
        self.dll = DoublyLinkedList()

    def put(self,key,val):
        if not self.hash_map.get(key):
            if self.dll.length < self.capacity:
                self.dll.append({key:val})
                # updating hash_map 
                self.hash_map[key] = [val,self.dll.length - 1]
            else:
                self.dll.append({key:val})
                self.dll.popfirst()
                # updating hash_map 
                self.hash_map[key] = [val,self.capacity - 1]
        else:
            # updating val of an existing key val pair
    
            # updating hash_map
            self.hash_map[key][0] = val

            idx = self.hash_map[key][1]



    def get(self, key):
        if not self.hash_map.get(key):
            return -1
        else:
            # three cases:

            # case 1:
            idx = self.hash_map[key][1]
            if idx == 0:
                tmp = self.dll.head
                self.dll.head = tmp.next
                self.dll.head.prev = None

                self.tail.next = tmp
                tmp.prev = self.dll.tail
                tmp.next = None
                self.dll.tail = tmp
                return self.hash_map[key][0]

            # case 2:
            elif idx == self.capacity - 1 :
                return self.hash_map[key][0]

            # case 3:
            else:
                node = self.dll.get_at_index(idx)   
                tmp = node.prev

                tmp.prev = self.dll.tail
                self.tail.next = tmp
                tmp.next = None
                self.dll.tail = tmp
                return self.hash_map[key][0]

  