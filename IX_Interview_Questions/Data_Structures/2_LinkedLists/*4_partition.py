class Node(object):

    def __init__(self, value, next=None):
        self.value = value
        self.next = next 

    def __repr__(self):
        return str(self.value)

class LinkedList(object):

    def __init__(self, values=None):
        self.head = None
        self.tail = None
        if values:
            self.add_multiple(values)

    def __repr__(self):
        values = []
        current = self.head
        while current:
            values.append(current.value)
            current = current.next
        return "-> ".join(values)

    def add(self, value):
        if self.head is None:
            self.tail = self.head = Node(value)
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next
        return self.tail 

    def add_multiple(self, values):
        for v in values:
            self.add(v)

    def add_to_beginning(self, value):
        if self.head is None:
            self.tail = self.head = Node(value)
        else:
            old_head = self.head
            self.head = Node(value)
            self.head.next = old_head
        return self.head

    def generate(self, n, min, max):
        self.tail = self.head = None
        from random import randint
        for i in range(n):
            self.add(randit(min, max))
        return self


def partition(LL, x):
    """
    Write code to partition a linked list around a value x, such that all nodes 
    less than x come before all nodes greater than or equal to x. lf x is 
    contained within the list, the values of x only need to be after the elements 
    less than x (see below).The partition element x can appear anywhere in the 
    "right partition"; it does not need to appear between the left and right 
    partitions.

    EXAMPLE
    Input: 3 -> 5 -> 8 -> 5 ->10 -> 2 -> 1[partition=5) 
    Output: 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8
    """
    current = ll.tail = ll.head
    
    while current:
        next_node = current.next
        current.next = None
        if current.value < x:
            current.next = ll.head
            ll.head = current
        else:
            ll.tail.next = current
            ll.tail = current
        current = next_node

    if ll.tail.next is not None:
        ll.tail.next = None



LL = LinkedList()
ll.generate(10, 0, 99)
print ll 
parition(ll, ll.head.value)
print ll