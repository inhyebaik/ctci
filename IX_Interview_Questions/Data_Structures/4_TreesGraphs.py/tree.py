class Node(object):
    def __init__(self, value, children=None):
        self.value = value
        self.children = children or []

# A naive, incorrect version of this would be:

# class Node(object):
#     def __init__(self, data, children=[]):
#         self.data = data
#         self.children = children

# This looks right, but there’s a subtle bug: that “default list of empty children” 
# is only built once. Every time you make a node without explicitly passing in
# children, those nodes will share the same empty list. As they’re sharing the 
# same list, if you mutate it, all the nodes would reflect that:

# >>> snape = Node("Snape")
# >>> flitwick = Node("Flitwick")

# >>> snape.children.append(Node("Malfoy"))
# >>> snape.children
# [<Node Malfoy>]

# >>> flitwick.children  # ut oh
# [<Node Malfoy>]
# >>> snape.children is flitwick.children
# True

    def __repr__(self):
        return "<Node {}>".format(self.value)

    # DFS: search current node's children (and their children) before siblings
    def find_DFS(self, value):
        """ Start at this node, and return node with given value; else None. """
        
        to_visit = [self]
        
        while to_visit:
            curr = to_visit.pop() # DFS -> .pop() from end -> stack
        
            if curr.value == value:
                return curr
            
            to_visit.extend(curr.children)  

    def find_BFS(self, value):
        """ BFS find AKA find the highest-ranking node with the given value. """
        to_visit = [self]
        while to_visit:
            curr = to_visit.pop(0) # BFS -> .pop(0) -> queue 
            if curr.value == value:
                return curr
            to_visit.extend(curr.children)

class Tree(object):
    def __init__(self, root):
        self.root = root # Node object
    
    def __repr__(self):
        return "<Tree root={}>".format(self.root)

    def find_in_tree_DFS(self, value):
        return self.root.find_DFS(value)

    def find_in_tree_BFS(self, value):
        return self.root.find_BFS(value)

class BinarySearchNode(object):
    def __init__(self, value, lc=None, rc=None):
        self.value = value
        self.lc = lc # left child
        self.rc = rc # right child

    def __rep__(self):
        return "<BinaryNode {}>".format(self.value)

    def find(self, target):
        curr = self
        while curr:
            if curr.value == value:
                return curr
            elif curr.value > target:
                curr = curr.lc 
            elif curr.value < target:
                curr = curr.rc


