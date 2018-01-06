
# 2.1

a2 = Node('A')
a1 = Node('A', a2)
b3 = Node('B', a1)
b2 = Node('B', b3)
b1 = Node('B', b2)
c1 = Node('C', b1)

LL = LinkedList(c1, a2)

def remove_dups(LL):
    """
    Removes duplicates from an unsorted linked list.
    Follow up: how would you solve this if a temporary buffer isn't allowed?
    """
    curr = LL.head
    seen = [curr.data]

    print "Original LL:"
    LL.print_nodes()

    while curr.next is not None:
        if curr.next.data not in seen:
            seen.append(curr.next.data)
            curr = curr.next
        elif curr.next.data in seen and curr.next == LL.tail:
            LL.tail = curr
            curr.next = None
        else:
            dup = curr.next
            curr.next = curr.next.next
            dup.next = None

    print "After removing duplicates:"
    LL.print_nodes()


a = Node(1, b) # 5th to last
b = Node(2, c) # 4th to last
c = Node(3, d) # 3rd to last
d = Node(4, e) # 2nd to last
e = Node(5)
ll = LinkedList(a, e)


# 2.2
def kth_to_last(LL, k):
    """Find the kth to last element of a singly linked-list."""
    if k == 1:
        return LL.tail
    nodes = []
    while curr is not None:
        nodes.append(curr)
        curr = curr.next
    return nodes[-k]

def kth_to_last2(LL, k):
    runner = curr = LL.head

    # set runner to be k nodes ahead of curr
    for i in range(k):
        if runner is None:
            return None
        runner = runner.next

    while runner:
        curr = curr.next
        runner = runner.next

    return curr



# 2.3 
def delete_middle_node(LL, access_node):
    """
    Delete a node in middle (any node but the first and last, not exact middle) 
    of a singly linked list, give only access to that node.
    Input: node c from linked list a-b-c-d-e-f
    Result: returns nothing, but now linked list looks like a-b-d-e-f
    """
    print "original LL:"
    LL.print_nodes()
    access_node.data = access_node.next.data
    print "changing middle node to its next:"
    LL.print_nodes()
    access_node.next = access_node.next.next
    print "after removing middle:"
    LL.print_nodes()
delete_middle_node(ll, c)

# 2.4 
def partition(LL, x):
    pass






