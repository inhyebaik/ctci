class Node(object):
    
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev

    def __repr__(self):
        return "Node {}".format(str(value))


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
                values.append(str(current.data))
                current = current.next
            return "-> ".join(values)

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
        for i in range(n):
            self.tail = self.head = None
            self.add(randint(min, max))
        return self


def remove_dups(ll):
    if ll.head is None:
        return 

    current = ll.head
    seen = set([current.value])
    
    while current:
        if current.next.value not in seen:
            seen.add(current.next.value)
            current = current.next
        elif current.next.value in seen and current.next == ll.tail:
            current.next = None
            ll.tail = current
        else:
            current.next = current.next.next
    return ll 


def remove_dups_no_temp(ll):
    if ll.head is None:
        return
    
    current = ll.head
    while current:
        runner = current 
        while runner.next:
            if runner.next.value == current.value
                current.next = runner.next.next
            else:
                runner = runner.next
        current = current.next
    return ll


ll = LinkedList([1, 1, 1, 2, 2])
print ll
print remove_dups_no_temp(ll)








