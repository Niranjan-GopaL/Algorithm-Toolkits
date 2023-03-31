class LRU:
    def __init__(self,capacity):
        self.hash_map = {}

    def get(self,key):
        if self.hash_map.get(key):
            return self.hash_map[key]
        else:
            return -1

    def put(self,key,value):
        if not self.hash_map():
            pass

_ , capacity = input().split(' ')
cache = LRU(int(capacity))
test = int(input())

for i in range(test):
    inp = input().split()
    if inp[0] == 'get':
        print(cache.get(int(inp[1])))
    else:
        cache.put(int(inp[1]), int(inp[2]))
        print("null")

print(cache.hash_map)