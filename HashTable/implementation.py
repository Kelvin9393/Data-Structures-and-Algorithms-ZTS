class HashTable():

    def __init__(self, size):
        self.size = size
        self.data = [None] * self.size

    def __str__(self):
        return str(self.__dict__)
    
    def __hash(self, key):
        hash = 0
        for i in range(len(key)):
            hash = (hash + ord(key[i]) * i) % self.size

        return hash
    
    def get(self, key):
        address = self.__hash(key)
        if self.data[address]:
            for i in range(len(self.data[address])):
                if self.data[address][i][0] == key:
                     return self.data[address][i][1]
                     
        return None
    
    def set(self, key, value):
        address = self.__hash(key)
        if not self.data[address]:
            self.data[address] = [[key, value]]
        else:
            self.data[address].append([key, value])
        print(self.data)

    def keys(self):
        keys_array = []
        for items in self.data:
            if items:
                for sub_item in items:
                    keys_array.append(sub_item[0])

        return keys_array


hash_table = HashTable(50)
hash_table.set("grapes", 10000)
hash_table.set("apples", 54)
hash_table.set("oranges", 2)
print(hash_table.get('grapes'))
print(hash_table.get('apples'))
print(hash_table.keys())