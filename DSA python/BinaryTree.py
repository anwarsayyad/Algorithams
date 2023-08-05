class Node:
    def __init__(self,vlaue):
        self.value = vlaue
        self.right  = None
        self.left = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.len = 0

    def insert(self,value):
        new_node = Node(value)
        if self.root == None:
            self.root = new_node
            return True
        temp = self.root
        while True:
            if temp == new_node or temp.value == new_node.value:
                return False
            if new_node.value > temp.value:
                if temp.right == None:
                    temp.right = new_node
                    self.len += 1
                    return True
                    
                else:
                    temp = temp.right
            else:
                if temp.left == None:
                    temp.left = new_node
                    self.len += 1
                    return True
                else:
                    temp = temp.left
                
    def contains(self,value):
        temp = self.root
        while temp is not None:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True

        
        return False


my_tree = BinarySearchTree()
my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)

print('BST Contains 27:')
print(my_tree.contains(27))

print('\nBST Contains 17:')
print(my_tree.contains(17))
                


"""
    EXPECTED OUTPUT:
    ----------------
    BST Contains 27:
    True

    BST Contains 17:
    False

"""

# my_tree = BinarySearchTree()
# my_tree.insert(2)
# my_tree.insert(1)
# my_tree.insert(3)

# """
#     THE LINES ABOVE CREATE THIS TREE:
#                  2
#                 / \
#                1   3
# """


# print('Root:', my_tree.root.value)            
# print('Root->Left:', my_tree.root.left.value)        
# print('Root->Right:', my_tree.root.right.value)        



# """
#     EXPECTED OUTPUT:
#     ----------------
#     Root: 2
#     Root->Left: 1
#     Root->Right: 3

# """