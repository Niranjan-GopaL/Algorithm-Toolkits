class Node:
    def __init__(self, key=0 , val=0):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class LRUCache:

    def __init__(self, capcity):
        self.capcity = capcity

        self.hash_map = {}

        self.front = Node()
        self.back = Node()
        self.front.prev ,self.back.next = self.back , self.front


    def remove(self, node):
        before , after = node.prev, node.next
        before.next , after.prev = after, before

    def insert(self, node):
        before , after = self.front.prev, self.front
        before.next = after.prev = node 
        node.next , node.prev = after , before

    def get(self, key):
        if key in self.hash_map:
            self.remove(self.hash_map[key])
            self.insert(self.hash_map[key])
            return self.hash_map[key].val
        return -1
    
    def put(self, key, value):
        if key in self.hash_map:
            self.remove(self.hash_map[key])
        self.hash_map[key] = Node(key,value)
        self.insert(self.hash_map[key])

        if len(self.hash_map) > self.capcity:
            lru = self.back.next
            self.remove(lru)
            del self.hash_map[lru.key]

