class Node(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return self.val

class LinkedList(object):
    def __init__(self, values=None):
        self.head = None
        self.tail = None
        if values:
            self.add_multiple(values)

    def __repr__(self):
        curr = self.head 
        nodes = []
        while curr:
            nodes.append(curr.val)
            curr = curr.next
        return "-> ".join(nodes)

    def add(self, val):
        if not self.head:
            self.tail = self.head = val
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next

    def add_multiple(self, vals):
        for v in vals:
            self.add(v)


def list_depths(root):
    """ 
    BFS
    Creates linked list of all nodes for each depth of BST 
    """
    current_level = [root]
    while current_level:
        next_level = LinkedList()
        for node in current_level:
            print node.value,
            if node.left: next_level.add(node.left)
            if node.right: next_level.add(node.right)
            print next_level
        current_level = next_level

        
