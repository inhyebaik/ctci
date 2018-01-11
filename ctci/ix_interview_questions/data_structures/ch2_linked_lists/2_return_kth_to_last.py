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

    def add(self, value):
        if self.head is None:
            self.tail = self.head = Node(value)
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next
        return self.tail

    def add_to_beginning(self, value):
        if self.head is None:
            self.tail = self.head = Node(value)
        else:
            old_head = self.head
            self.head = Node(value)
            self.head.next = old_head
        return self.head 

    def add_multiple(self, values):
        for v in values:
            self.add(v)

    def generate(self, n, min, max):
        from random import randint
        self.tail = self.head = None
        for i in range(n):
            self.add(randint(min, max))
        return self


def return_kth_to_last(ll, k):
    if ll.head is None:
        return self
        
    runner = current = ll.head
    # set runner so that curr is k nodes behind
    for i in range(k):
        runner = runner.next

    # traverse until runner is at the tail
    # current will be k away from the tail 
    while runner.next:
        current = current.next
        runner = runner.next

    # remove kth node (current.next is kth)
    current.next = current.next.next
    return self

ll = LinkedList([1,2,3,4,5,6])
print return_kth_to_last(ll, 2)




