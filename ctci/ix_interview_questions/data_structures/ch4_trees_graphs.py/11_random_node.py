class Node(object):
    def __init__(self, value, lc=None, rc=None, parent=None):
        self.value = value
        self.lc = lc
        self.rc = rc
        self.parent = parent

    def is_leaf(self):
        return not self.lc and not self.rc

    def has_any_children(self):
        return self.lc or self.rc

    def has_both_children(self):
        return self.lc and self.rc

    def is_left_child(self):
        return self.parent.lc == self

    def is_right_child(self):
        return self.parent.rc == self

def find_successor(node):
    """ Successor will always be a leaf """
    succ = None
    if node.rc:
        succ = find_min(node.rc)
    return succ

def find_min(root):
    """ will return smallest leaf in BST. """
    curr = root
    while curr:
        if curr.lc:
            curr = curr.lc 
    return curr

def find(root, target):
    curr = root
    
    while curr:
        if curr.value == target:
            return curr
        elif curr.value > target:
            curr = curr.lc
        else:
            curr = curr.rc
    return False

def get_random_node(root):
    


# def delete(root, node):
#     if not node.parent:
#         return 'Cannot remove root!'

#     if node.is_leaf:
#         if node.is_left_child: 
#             node.parent.lc = None
#         else:
#             node.parent.rc = None
    
#     if node.has_both_children:
#         # node's child can be a leaf, 
#         succ = find_successor(node) # successor will always be a leaf
#         if 
#             succ.parent = node.parent
#             node.rc.parent = succ
#             if node.is_left_child:
#                 node.parent.lc = succ
#             else:
#                 node.parent.rc = succ


#     if node.has_any_children:
#         child = node.lc or node.rc
#         if node.is_left_child:
#             node.parent.lc = child
#         elif node.is_right_child:
#             node.parent.rc = child
#         child.parent = node.parent




