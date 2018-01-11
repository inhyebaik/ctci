# source: https://www.geeksforgeeks.org/print-k-sum-paths-binary-tree/

class Node(object):
    def __init__(self, data, left=None, right=None):
        self.left = left
        self.right = right
        self.data = data

def paths_with_sum(root, path, k):
    if not root:
        return

    # add current node to path
    path.insert(root.data, 0)

    # check if there's a k-sum path in left sub-tree
    paths_with_sum(root.left, path, k)

    # check if there's a k-sum path in right sub-tree
    paths_with_sum(root.right, path, k)

    # check if there's any k-sum path that terminates at this node
    # traverse the entire path as there can be negative elements
    f = 0
    for i in range(len(path)):
        f += path[i]

        if f == k:
            print(path)
    # Remove current element from path
    path.pop(0)



