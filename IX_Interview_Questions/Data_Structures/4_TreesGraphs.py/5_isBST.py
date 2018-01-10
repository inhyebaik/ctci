# Time:  O(n)
# Space: O(1)
# 
# Given a binary tree, determine if it is a valid binary search tree (BST).
# 
# Assume a BST is defined as follows:
# 
# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.
#

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

def is_valid_BST(root):
    return is_valid_BST(root, float("-inf"), float('inf'))

def is_valid_BST_rec(root, low, high):
    if not root:
        return True

    return low < root.val and root.val < high \
        and is_valid_BST_rec(root.left, low, root.val) \
        and is_valid_BST_rec(root.right, root.val, high)

