# Binary Tree vs. Binary SEARCH tree
# binary tree: each node has at most 2 children (left is smaller, right is larger)
# binary search tree: all left DESCENDENTS <= n <= all right DESCENDENTS
    # aka, even left grandchildren <= n <= all right grandchildren. 

# Balanced vs. Unbalanced Binary Trees

# 1) COMPLETE: a binary tree in which every level of the tree is fully filled, 
# except for perhaps the last level from LEFT to RIGHT. 
# kth level can be missing a RIGHT child, but never a LEFT child! 
# Mnemonic: Completion requires the left wing but not necessarily the right! 

# 2) FULL: each node has 2 or 0 children; but never just 1 child. 
# Mnemonic: Full -- the opposite of 1 child policy in China home of the Full Moon 

# 3) PERFECT: full and complete! Left and right children all there or none at all! 
# Perfect binary trees have exactly ((2^k) - 1) nodes (k = # levels)

class TreeNode(object):
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.leftChild = left
        self.rightChild = right
        self.parent = parent

    def hasLeftChild(self):
        return self.left

    def hasRightChild(self):
        return self.right 

    def isLeftChild(self):
        return self.parent and self.parent.leftChild is self

    def isRightChild(self):
        return self.parent and self.parent.rightChild is self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        """ isChild? """
        return not (self.hasLeftChild or self.hasRightChild)

    def anyChild(self):
        """ Returns node's any child; False if no children """
        return self.leftChild or self.rightChild

    def bothChildren(self):
        """ Returns both children if it has 2. """
        return self.leftChild and self.rightChild

class BinaryTreeNode(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left # left child
        self.right = right # right child

    def __rep__(self):
        return "<BinaryNode {}>".format(self.value)


class BinarySearchTree(object):
    def __init__(self):
        self.root = None 
        self.size = 0

    def length(self):
        return self.size 

    def __len__(self):
        return self.size 

    def __iter__(self):
        return self.root.__iter__()

    def __repr__(self):
        return "<BinaryTree root={}>".format(self.root)

    # Binary Tree Traversals
    def in_order_traversal(self):
        """Visit in ascending order (left, current, then right branches)."""
        node = self.root
        if node:
            in_order_traversal(node.left)
            print node
            in_order_traversal(node.right)

    def pre_order_traversal(self):
        """Visit current before current children. Root is always first node visited."""
        node = self.root
        if node:
            print node 
            pre_order_traversal(node.left)
            pre_order_traversal(node.right)

    def post_order_traversal(self):
        """ Visit current AFTER visiting its children. Root is visited last. """
        node = self.root
        if node:
            post_order_traversal(node.left)
            post_order_traversal(node.right)
            print node

# BST
    def search(self, target):
        """ for BSTs """
        current = self.root

        while current:
            if current.value == target:
                return current
            elif target < current.value:
                current = current.left
            elif target > current.value:
                current = current.right


# Binary Heaps (Min-heaps and Max-heaps)
# Min-heap:
# 1) COMPLETE binary tree (that is, totally filled other than the rightmost elements on the last level)
# 2) SMALLER values on TOP levels; LARGE numbers on LEAF levels

# Inserting into a min-heap
# 1) We always insert at the bottom --> rightmost. (Again, it's a "COMPLETE" BT)
# 2) "Fix" tree by swapping new element with parent -> bubble up smaller 
# 3) O(log N)
    def insert_min_heap(self, value):
        # 1) Locate proper location
        if not self.root:
            self.root = BinaryTreeNode(value)

    def delete_BST(self, value):
        # 1) first find node to delete by searching tree
        if self.size 
        # 2) 
        




