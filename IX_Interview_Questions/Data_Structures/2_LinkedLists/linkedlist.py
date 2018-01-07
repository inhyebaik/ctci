class Node(object):

    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev

    def __repr__(self):
        return str(self.value)


class LinkedList(object):

    def __init__(self, values=None):
        self.head = None
        self.tail = None
        if values:
            self.add_mutiple(values)

    def __repr__(self):
        values = []
        curr = self.head
        while curr:
            values.append(str(curr.value))
            curr = curr.next
        return "-> ".join(values)

    def add(self, value):
        if self.head is None:
            self.tail = self.head = Node(value)
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next

    def add_to_beginning(self, value):
        if self.head is None:
            self.tail = self.head = Node(value)
        else:
            old_head = self.head
            self.head = Node(value)
            self.head.next = old_head

    def add_multiple(self, values):
        for v in values:
            self.add(v)

    def generate(self, n, min, max):
        from random import randint
        self.head = self.tail = None
        for i in range(n):
            self.add(randint(min, max))
        return self

    def __len__(self):
        l = 0
        c = self.head 
        while c:
            l += 1
            c = c.next
        return l




