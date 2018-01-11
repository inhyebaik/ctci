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
            self.add_multiple(values)

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

def sum_lists(ll1, ll2):
    """
    You have two numbers represented by a linked list, where each node contains 
    a single digit. The digits are stored in reverse order, such that the 1's 
    digit is at the head of the list. Write a function that adds the two numbers
    and returns the sum as a linked list.
    """

    a, b = ll1.head, ll2.head # start adding the ones digits
    ll = LinkedList()
    carry_over = 0
    
    while a or b:
        result = carry_over
        if a:
            result += a.value 
            a = a.next 
        if b:
            result += b.value 
            b = b.next 

        ll.add(result % 10)
        carry_over = result // 10
    
    return ll

def length(ll):
    length = 0
    curr = ll.head
    while curr:
        length += 1
        curr = curr.next
    return length


def sum_lists_fup(ll_a, ll_b):
    # Pad shorter LL  
    if length(ll_a) > length(ll_b):
        for i in range(length(ll_a) - length(ll_b)):
            ll_b.add_to_beginning(0)
    else:
        for i in range(length(ll_b) - length(ll_a)):
            ll_a.add_to_beginning(0)

    # Find sum
    n1, n2 = ll_a.head, ll_b.head
    result = 0
    while n1 and n2:
        result = (result*10) + n1.value + n2.value 
        n1 = n1.next 
        n2 = n2.next

    # Create new LL 
    ll = LinkedList()
    ll.add_multiple([int(i) for i in str(result)])

    return ll 


ll1 = LinkedList([7, 1, 6])
ll2 = LinkedList([5, 9, 2])
print sum_lists(ll1, ll2)









