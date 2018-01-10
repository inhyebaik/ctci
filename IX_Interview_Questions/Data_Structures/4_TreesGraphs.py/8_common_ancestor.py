class BTNode(object):
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent
    
    def __repr__(self):
        return str(self.value)

    def add_left_child(self, n2):
        self.left = n2
        n2.parent = self

    def add_right_child(self, n2):
        self.right = n2 
        n2.parent = self

    def has_parent(self):
        return self.parent

    def get_ancestors(self):
        ancestors = set()
        curr = self
        while curr.parent:
            ancestors.add(curr.parent)
            curr = curr.parent
        return ancestors

node7 = BTNode(value=7)
node6 = BTNode(value=6)
node5 = BTNode(value=5)
node4 = BTNode(value=4)
node2 = BTNode(value=2)
node3 = BTNode(value=3)
root = BTNode(value=1)

node2.add_left_child(node4)
node2.add_right_child(node5)

node3.add_left_child(node6)
node3.add_right_child(node7)

root.add_left_child(node2)
root.add_right_child(node3)

class BinaryTree(object):
    def __init__(self, root):
        self.root = root

    def first_common_ancestor(self, node1, node2):
        
        if node1.parent is node2:
            return node2
        if node2.parent is node1:
            return node1

        ancestors1 = set()
        ancestors2 = set()
        
        curr1 = node1
        curr2 = node2
        
        shared = None
        while not shared and curr1.parent and curr2.parent:
            # print shared, curr1, curr2
            ancestors1.add(curr1.parent)
            curr1 = curr1.parent 
            ancestors2.add(curr2.parent)
            curr2 = curr2.parent
            shared = ancestors1.intersection(ancestors2)
        if shared: 
            return shared.pop()
        else:
            return root

bt = BinaryTree(root)
print bt.first_common_ancestor(node5, node4) # 2 
print bt.first_common_ancestor(node5, node2) # 2 
print bt.first_common_ancestor(node6, node7) # 3
print bt.first_common_ancestor(node4, node7) # 1
    

