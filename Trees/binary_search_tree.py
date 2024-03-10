class Node():
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    def __str__(self):
        return str(f"{{value:{self.value}, left:{self.left if self.left else "null"}, right:{self.right if self.right else "null"}}}")

class BinarySearchTree():
    def __init__(self):
        self.root = None

    def __str__(self):
        return str(self.root)

    def insert(self, value):
        new_node = Node(value)
        if self.root:
            current_node = self.root
            while True:
                if new_node.value < current_node.value:
                    if current_node.left is None:
                        current_node.left = new_node
                        break
                    else:
                        current_node = current_node.left
                        
                elif new_node.value > current_node.value:
                    if current_node.right is None:
                        current_node.right = new_node
                        break
                    else:
                        current_node = current_node.right
            
        else:
            self.root = new_node
        

    def lookup(self, value):
        current_node = self.root

        if current_node is None:
            return False
        
        while current_node:
            if current_node.value == value:
                return current_node
            
            elif value < current_node.value:
                current_node = current_node.left

            elif value > current_node.value:
                current_node = current_node.right

        return False


def traverse(node):
    tree = node
    if node.left:
        traverse(node.left)
    else:
        tree.left = None

    if node.right:
        traverse(node.right)
    else:
        tree.right = None

    return tree

my_bst = BinarySearchTree()
my_bst.insert(9)
my_bst.insert(4)
my_bst.insert(6)
my_bst.insert(20)
my_bst.insert(170)
my_bst.insert(15)
my_bst.insert(1)

# print(traverse(my_bst.root))
print(my_bst.lookup(6))