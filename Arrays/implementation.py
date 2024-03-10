class MyArray:
    def __init__(self):
        self.length = 0
        self.data = {}

    def __str__(self):
        return str(self.__dict__)
    
    def get(self, index):
        return self.data[index]
    
    def push(self, item):
        self.data[self.length] = item
        self.length += 1
        return self.length

    def pop(self):
        last_item = self.data[self.length - 1]
        del self.data[self.length - 1]
        self.length -= 1
        return last_item
    
    def delete(self, index):
        item = self.data[index]
        for i in range(index, self.length - 1):
            self.data[i] = self.data[i + 1]
        
        del self.data[self.length - 1]
        self.length -= 1
        return item
    
    def insert(self, index, item):
        for i in range(index, self.length - 1):
            self.data[i] = self.data[i - 1]

    

newArray = MyArray()
newArray.push("hi")
newArray.push("you")
newArray.push("!")
# newArray.pop()
# newArray.pop()
newArray.delete(0)
newArray.push("are")
newArray.push("nice")
newArray.delete(1)

print(newArray)