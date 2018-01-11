class TreeNode(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left 
        self.right = right
    def __repr__(self):
        return "<TreeNode val={}>".format(self.val)

def minimalBST(sorted_array):

    def arrayToBST(sorted_array, start, end):
        if start > end:
            return
        mid = (start + end)/2
        root = TreeNode(sorted_array[mid])
        root.left = arrayToBST(sorted_array, start, mid-1)
        root.right = arrayToBST(sorted_array, mid+1, end)
        return root

    return arrayToBST(sorted_array, 0, len(sorted_array)-1)