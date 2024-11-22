# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
#print("Try programiz.pro")
class Node: 
    left = None
    right = None
    #Node parent
    value = None
    
    #constructor to create a node with the value/data
    def __init__(self, value):
        self.value = value
    
class BinaryTree:
    rootNode = None

    def insert(self, value):
        tempNode = Node(value)
        if self.rootNode is None:
            self.rootNode = tempNode
        else:
            parentNode = self.rootNode
            while(parentNode is not None):
                if parentNode.value < tempNode.value:
                    if parentNode.right is None:
                        parentNode.right = tempNode
                        break
                    else:
                        parentNode = parentNode.right
                else:
                    if parentNode.left is None:
                        parentNode.left = tempNode
                        break
                    else:
                        parentNode = parentNode.left
                    
                  
    def printInorder(self, node):
        if node is None:
            return

        # First recur on left subtree
        self.printInorder(node.left)

        # Now deal with the node
        print(node.value, end=' ')

        # Then recur on right subtree
        self.printInorder(node.right)
            

tree = BinaryTree()
tree.insert(10)
tree.insert(5)
tree.insert(20)
tree.insert(1)
tree.insert(15)
tree.printInorder(tree.rootNode)
                
        
        
        
        
