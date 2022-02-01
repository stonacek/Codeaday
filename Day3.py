# Given the root to a binary tree, implement serialize(root), 
# which serializes the tree into a string, and deserialize(s), 
# which deserializes the string back into the tree.
# For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

node = Node('root', Node('left', Node('left.left')), Node('right'))
node2 = Node('root', Node('left'), Node('right'))
node2.left.left =  Node('left.left')

for nodes in node:
    x = nodes
    


#------------- Personal Solution ------------
#organize tree starting with root and reading left to right for each generation of children.
#def serialize(node):
#    node
#    stringz = 



#assert deserialize(serialize(node)).left.left.val == 'left.left'
print(node)