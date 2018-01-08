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

class BinarySearchNode(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left # left child
        self.right = right # right child

    def __rep__(self):
        return "<BinaryNode {}>".format(self.value)

    def find(self, target):
        curr = self
        while curr:
            if curr.value == value:
                return curr
            elif curr.value > target:
                curr = curr.left 
            elif curr.value < target:
                curr = curr.right

    # Binary Tree Traversals: in-, pre-, post-order
    # 'visit' = print
    def in_order_traversal(node):
        """Visit in ascending order (left, current, then right branches)."""
        if node:
            in_order_traversal(node.left)
            print node
            in_order_traversal(node.right)

    def pre_order_traversal(node):
        """Visit current before current children. Root is always first node visited."""
        if node:
            print node 
            pre_order_traversal(node.left)
            pre_order_traversal(node.right)

    def post_order_traversal(node):
        """ Visit current AFTER visiting its children. Root is visited last. """
        if node:
            post_order_traversal(node.left)
            post_order_traversal(node.right)
            print node

# Binary Heaps (Min-heaps and Max-heaps)
# Min-heap: a complete binary tree (that is, totally filled other than the 
    # rightmost elements on the last level) where each node is smaller than its 
    # children. The root, therefore, is the minimum element in the tree.


