# Given the root to a binary tree, 
# implement serialize(root), which serializes the tree into a string,
# and deserialize(s), which deserializes the string back into the tree.
# For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

node = Node('root', Node('left', Node('left.left')), Node('right'))

# should be able to run -- deserialize(serialize(node)).left.left.val == 'left.left' at the end


#------------- Personal Solution ------------
# Serialize organizes tree starting with root and reading left to right for each generation of children.
# The function searches the tree from the root. It first records the value of each child of the 
# current parent along with their type (left, right) and index value of their parent node. 
# Then the child node is added to a list of nodes to-be-visited. This is a list of parent nodes
# that need to be investigated for children. Thus each node in the tree will be visited and its 
# children's information recorded to the string. 
def serialize(node):
    nodes_to_visit = [node]
    node_string = node.val+",-1,T"
    node_index = [0]
    i = 0
    while nodes_to_visit:
        current_node = nodes_to_visit.pop(0)
        current_node_index = node_index.pop(0)
        if current_node.left != None:
            #list_of_nodes.append(current_node.left)
            nodes_to_visit.append(current_node.left)
            i += 1
            node_index.append(i)
            node_string += ","+current_node.left.val
            node_string += ","+str(current_node_index)
            node_string += ",L"
        if current_node.right != None:
            #list_of_nodes.append(current_node.right)
            nodes_to_visit.append(current_node.right)
            i += 1
            node_index.append(i)
            node_string += ","+current_node.right.val
            node_string += ","+str(current_node_index)
            node_string += ",R"
    return node_string

# Deserialize assumes the string is organized with each generation added sequentially as read from left to right.
# it splits the string into a list then pops the first three indexs cooresponding to the current nodes value,
# the index of its parent, and its type (left or right). The nodes are appended to a list to be able to track 
# parents. Each node is then added as a left or right for its parent, based on parent index and type.
def deserialize(node_string):
    node_string_list = node_string.split(',')
    node_list = []
    while node_string_list:
        current_node_val = node_string_list.pop(0)
        current_node_parent = node_string_list.pop(0)
        current_node_type = node_string_list.pop(0)
        current_node = Node(current_node_val)
        if current_node_type == "T" and current_node_parent == "-1":
            node_list.append(current_node)
        elif current_node_type == "L":
            node_list.append(current_node)
            node_list[int(current_node_parent)].left = current_node
        elif current_node_type == "R":
            node_list.append(current_node)
            node_list[int(current_node_parent)].right = current_node
    return  node_list[0]

x = deserialize(serialize(node)).left.left.val == 'left.left'

#------------- Given Solution ------------
# We can approach this problem by first figuring out what we would like the serialized tree to look like. 
# Ideally, it would contain the minimum information required to encode all the necessary information about 
# the binary tree. One possible encoding might be to borrow S-expressions from Lisp. The tree Node(1, Node(2),
# Node(3)) would then look like '(1 (2 () ()) (3 () ()))', where the empty brackets denote nulls.

# To minimize data over the hypothetical wire, we could go a step further and prune out some unnecessary 
# brackets. We could also replace the 2-character '()' with '#'. We can then infer leaf nodes by their 
# form 'val # #' and thus get the structure of the tree that way. Then our tree would look like 1 2 # # 3 # #.
def serialize(root):
    if root is None:
        return '#'
    return '{} {} {}'.format(root.val, serialize(root.left), serialize(root.right))

def deserialize(data):
    def helper():
        val = next(vals)
        if val == '#':
            return None
        node = Node(int(val))
        node.left = helper()
        node.right = helper()
        return node
    vals = iter(data.split())
    return helper()

pp = serialize(node)
x = deserialize(pp)
x