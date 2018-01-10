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

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

MIN = -99999999999
MAX = 999999999999

def is_valid_BST(root):
    return is_valid_BST_rec(root, MIN, MAX)

def is_valid_BST_rec(node, mini, maxi):

    # an empty tree is a valid BST 
    if node is None:
        return True

    # False if node violates min/max constraint
    if node.value < mini or node.value > maxi:
        return False

    # Else, check subtrees recursively, tightening min or max constraint
    return  ( is_valid_BST_rec(node.left, mini, node.value-1) and \
              is_valid_BST_rec(node.right, node.value+1, maxi) ) 

# Test
root = Node(4)
root.left = Node(2)
root.right = Node(5)
root.left.left = Node(1)
root.left.right = Node(3)