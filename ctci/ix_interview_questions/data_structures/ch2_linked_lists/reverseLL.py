class Node(object):
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def reverse_nondesuctrive(head):
    """ Outputs a new reversed LL instead of modifying input LL. """
    new_head = None
    while head:
        new_head = Node(head.value, new_head)
        head = head.next
    return new_head


def reverse(head):
    last = None
    curr = head
    while curr: # while curr
        next = curr.next # save the next value, because we'll change the pointer
        curr.next = last # now that we've saved the next value, we can change pointer to last
        last = curr # current node will be the 'next' of its next node (in next iteration)
        curr = next # next node we look at is next we saved (since we lost the pointer)
    return last

# iterative solution, pass in LL as argument
def reverse(LL):
    curr = LL.head
    next = curr.next
    prev = None

    # update new tail
    LL.tail = curr
    
    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    
    # update new head
    LL.head = prev
    return LL.head


def reverse_recursive(self, node):
    if not node.next:
        self.head = node
        return
    self.reverse_recursive(node.next)
    temp = node.next
    temp.next = node
    node.next = None