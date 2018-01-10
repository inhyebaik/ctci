class Node(object):
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


    def is_leaf(self):
        return not self.left and not self.right and self.parent

    def is_root(self):
        return self.parent and self.has_any_children

    def find_successor(self, node):
        
        if node.is_leaf:
            return None

        # if it has a right subtree, find minimum value in right subtree
        if node.right:
            return self.find_min(node)
        else:
            # if there is no right subtree, then succ is one of the ancestors.
            # travel up using the parent pointer 
            # until you hit a node that is a left child
            p = node.parent
            while p:
                if node is not p.right:
                    break
                node = p
                p = p.parent
            return p 
 

    def find_min(self, node):
        curr = node
        while curr.left:
            curr = curr.left
        return curr

