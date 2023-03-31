#  Python has by default a built-in hash table : Dictionary
#  We want prime number of address spaces
#  prime number increases the randomness of how the key value pairs are gonna 
# be distributed in the hash table

class Hash_Table():
    def __init__(self, size = 7) :
        # Creating an address space (list)
        # data_map is a list of None (length = size)
        self.data_map = [None] * size
    
    # private method
    def __hash(self, key):
        my_hash = 0 
        # hash function used
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash
        '''
        % is the IMPORTANT PART 
        23 is just a prime number , insert any prime there 
        '''

    def print_HT(self):
        for i, val in enumerate(self.data_map):
            print(f'{i} : {val}')
        print('\n')


    def set_item(self,key,val):
        index = self.__hash(key)
        # the index in data_map can either be None(if index has never been used)
        # or it can already have some k,v pair
        if self.data_map[index] == None :
            self.data_map[index] = []
        self.data_map[index].append([key,val])

    def get_item(self,key):
        index = self.__hash(key)
        '''
        address = self.data_map(index)
        this raised "List not callable" error 
        cuz data_map is a LIST and IF WE TRY TO accessing elements as if it were a FUNCTION
        i.e list(index) insted of list[index]
        '''
        address = self.data_map[index]
        # so that address can be None (if key is not a key that has been added)
        if address is not None:
            for k,v in address:
                if k == key :
                    return v
        else:
            return None
        # return val
        pass


    def keys(self):
        for address in self.data_map:
            # if address is not None
            if address: 
                for k,v in address:
                    print(k,end = ' ')

ht = Hash_Table()
ht.print_HT()

ht.set_item("bolts",100)
ht.set_item("washers",50)
ht.set_item("nail",40)
ht.set_item("lumber",70)
ht.print_HT()

print(ht.get_item("washers"))
print(ht.get_item("bolts"))
print()

ht.keys()

'''
to set an item in HashTable is O(1)
but to get an item in HashTable would be O(n) cuz in the worst possible case, 
all the items are hashed to the SAME INDEX and we would have to search through as if it were a LL.
BUT this is a very rare case and normally the items would be distributed all across the hashtable.
With a bigger hash table and a better hash function collision would be very unlikely and therefore it
would be safe to say that actually getting a item from hashtable would be O(1).
'''
