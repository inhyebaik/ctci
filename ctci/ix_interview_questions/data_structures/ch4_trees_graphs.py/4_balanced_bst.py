# Time:  O(n)
# Space: O(h), h is height of binary tree
#
# Given a binary tree, determine if it is height-balanced.
#
# For this problem, a height-balanced binary tree is defined as a binary tree 
# in which the depth of the two subtrees of every node never differ by more than 1.
#

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def is_balanced(root):
    return check_height(root) != -1

def get_height(root):
        if root is None:
            return 0
        return max(get_height(root.left), get_height(root.right))+1

def check_height(node):
    if node is None:
        return 0

    # check if left subtree is balanced
    left_height = check_height(node.left)
    if left_height == -1:
        return -1

    # check if right subtree is balanced
    right_height = check_height(node.right)
    if right_height == -1:
        return -1 

    # check if current node is balanced
    height_diff = abs(left_height - right_height)
    if  height_diff > 1:
        return -1 
    else:
        return max(left_height, right_height) + 1

