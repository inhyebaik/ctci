class Node(object):
    def __init__(self, value, lc=None, rc=None):
        self.value = value
        self.lc = lc
        self.rc = rc

# O(M*N)
def are_identical(root1, root2):

    # If you cut off the tree at node n, the two trees would be identical.
    if not root1 and not root2: # no excess children
        return True
    if not root1 or not root2: # there's an excess child
        return False

    # Check if root values are equal, and values of their left and right children
    return (root1.value == root2.value and
            are_identical(root1.lc, root2.lc) and 
            are_identical(root1.rc, root2.rc)
           )

# O(M*N)
def is_subtree(tree, subtree):

    if not subtree or not tree:
        return True

    # Check each node of the tree as the root of the subtree:
    if are_identical(tree, subtree):
        return True

    return is_subtree(tree.lc, subtree) or is_subtree(tree.rc, subtree)

