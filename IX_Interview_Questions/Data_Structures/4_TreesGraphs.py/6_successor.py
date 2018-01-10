class Node(object):
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

    def is_leaf(self):
        return not self.left and not self.right

    def has_any_children(self):
        return self.left or self.right

    def has_both_children(self):
        return self.left and self.right

    def find_successor(self):
        
        if self.is_leaf:
            return None

        if self.right:
            succ = self.find_min(self.right)
            return succ

        if self.left:
            


    def find_min(self):
        curr = self
        while curr:
            if self.left:
                curr = self.left
        return curr

