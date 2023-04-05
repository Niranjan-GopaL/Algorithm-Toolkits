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

class LRUCache():
    def __init__(self,capacity):
        self.capacity = capacity
        self.hash_map = {}
        self.dll = DoublyLinkedList()

    def put(self,key,val):
        val_in_list_format = [val]

        if not self.hash_map.get(key):
            if self.dll.length < self.capacity:

                # making the node's val {key : val }
                self.dll.append({key: None })
                self.dll.tail.val[key] = val_in_list_format
                # updating hash_map 
                self.hash_map[key] = [val_in_list_format ,self.dll.length - 1]
            else:
                self.dll.append({key:val})
                self.dll.popfirst()
                # updating hash_map 
                self.hash_map[key] = [val,self.capacity - 1]
        else:
            # updating val of an existing key val pair in O(1)
    
            # updating hash_map
            self.hash_map[key][0].pop()
            self.hash_map[key][0].append(val_in_list_format)




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

_ , capacity = input().split(' ')
cache = LRUCache(int(capacity))
test = int(input())

for i in range(test):
    inp = input().split()
    if inp[0] == 'get':
        print(cache.get(int(inp[1])))
    else:
        cache.put(int(inp[1]), int(inp[2]))
        print("null")

cache.dll.print_DLL()
