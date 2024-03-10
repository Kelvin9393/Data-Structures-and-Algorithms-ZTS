class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

    def __str__(self) -> str:
        return str(self.data)

class DoublyLinkedList():
    def __init__(self):
        self.head = None
        self.tail = self.head
        self.length = 0

    def __str__(self) -> str:
        return f"Head: {self.head}, Tail: {self.tail}, Length: {self.length}"

    def append(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.tail = self.head
        else:
            new_node.previous = self.tail
            self.tail.next = new_node
            self.tail = new_node

        self.length += 1
        self.print_list()

    def prepend(self, data):
        new_node = Node(data)

        if self.head == None:
            self.head = new_node
            self.tail = self.head
        else:
            new_node.next = self.head
            self.head.previous = new_node
            self.head = new_node

        self.length += 1
        self.print_list()

    def insert(self, position, data):
        if position == 0:
            self.prepend(data)
            return
        
        if position >= self.length:
            print("This position is not available. Inserting at the end of the list")
            self.append(data)
            return
        
        new_node = Node(data)
        current_node = self.traverseToPosition(position - 1)

        new_node.previous = current_node
        new_node.next = current_node.next
        current_node.next = new_node
        new_node.next.previous = new_node

        self.length += 1
        self.print_list()

    def delete_from_position(self, position):
        if self.head == None:
            print("Linked List is empty. Nothing to delete.")
            return
        
        if position >= self.length:
            print(f"No element at position {position}")
            return
        
        if position == 0:
            self.head = self.head.next
            if self.head == None:
                self.tail = self.head
            
            if self.head != None:
                self.head.previous = None
        else:
            current_node = self.traverseToPosition(position - 1)
                
            current_node.next = current_node.next.next
            if current_node.next == None:
                self.tail = current_node
            else:
                current_node.next.previous = current_node

        self.length -= 1
        self.print_list()

    def print_list(self):
        if self.head == None:
            print("Empty")
        else:
            current_node = self.head
            while current_node:
                end = " --> "
                if current_node.next == None:
                    end = "\n"
                print(current_node, end = end)
                current_node = current_node.next
        print(self)

    def traverseToPosition(self, position):
        current_node = self.head
        for i in range(position - 1):
            current_node = current_node.next
        
        return current_node
    
    def print_reverse(self):
        if self.tail == None:
            print("Empty")
        else:
            current_node = self.tail
            while current_node:
                end = " --> "
                if current_node.previous == None:
                    end = "\n"
                print(current_node, end = end)
                current_node = current_node.previous
        
        print(self)

my_linked_list = DoublyLinkedList()
my_linked_list.print_list()
# Empty
# Head: None, Tail: None, Length: 0

my_linked_list.delete_from_position(2)
# Linked List is empty. Nothing to delete.

# Insert 10 to position 3 into empty list
my_linked_list.insert(3, 10)
# This position is not available. Inserting at the end of the list

my_linked_list.print_list()
# 10
# Head: 10, Tail: 10, Length: 1

my_linked_list.delete_from_position(1)
# No element at position 1

my_linked_list.delete_from_position(0)
# Empty
# Head: None, Tail: None, Length: 0

my_linked_list.append(6)
# 6
# Head: 6, Tail: 6, Length: 1

my_linked_list.append(5)
# 6 --> 5
# Head: 6, Tail: 5, Length: 2

my_linked_list.append(9)
# 6 --> 5 --> 9
# Head: 6, Tail: 9, Length: 3

# Delete first element
my_linked_list.delete_from_position(0)
# # 5 --> 9
# # Head: 5, Tail: 9, Length: 2

my_linked_list.append(7)
# # 5 --> 9 --> 7
# # Head: 5, Tail: 7, Length: 3

# # Insert 8 at position 1
my_linked_list.insert(1, 8)
# # 5 --> 8 --> 9 --> 7
# # Head: 5, Tail: 7, Length: 4

# # Add 13 to beginning of list
my_linked_list.prepend(13)
# # 13 --> 5 --> 8 --> 9 --> 7
# # Head: 13, Tail: 7, Length: 5

my_linked_list.print_reverse()