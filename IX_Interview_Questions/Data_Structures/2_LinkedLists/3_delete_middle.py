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
            self.add(randint(min, max))
        return self


def delete_middle(ll, node):
    node.value = node.next.value
    node.next = node.next.next
    return ll

ll = LinkedList([1,2,3,4])
middle_node = ll.add(5)
ll.add_multiple([6,7,8])
print ll 
print delete_middle(ll, middle_node)




