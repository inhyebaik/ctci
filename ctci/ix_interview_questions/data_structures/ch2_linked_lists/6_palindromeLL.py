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

# O(N)
def length(ll):
    l = 0
    c = ll.head 
    while c:
        l += 1
        c = c.next
    return l 

# O(k)
def kth_to_last(ll, k):
    if not ll.head:
        return

    if k == 1:
        return ll.tail 

    c = ll.head
    runner = c
    for i in range(k):
        while runner:
            runner = runner.next
    
    while runner:
        c = c.next
        runner = runner.next
    
    return c

# O(N/2) * O(N/2)
def palindrome(ll):
    """
    1 2 0 0 2 1

    1 2 0 3 0 2 1
    """
    if length(ll) < 4:
        return ll.head.value == ll.tail.value
    
    k = length(ll)/2
    if k % 2 != 0:
        k = k -1

    j = k + 1
        while k > 0:
            if kth_to_last(ll, j).value == kth_to_last(ll, k).value:
                j += 1
                k -= 1
            else:
                return False
        return True

def is_palindrome(ll):
    r = c = ll.head 
    stack = []

    while r and r.next:
        stack.append(c.value)
        c = c.next 
        r = r.next.next
    
    if r: # odd length LL; skip the middle node
        c = c.next
    
    while c:
        top = stack.pop()
        if top != c.value:
            return False
        c = c.next
    return True


ll = LinkedList([1, 2, 3, 3, 2, 1])
ll2 = LinkedList([1,2,3,0,3,2,1])
ll3 = LinkedList([1,2,3])

print is_palindrome(ll)



