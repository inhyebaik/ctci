# 2.8
from linkedlist import LinkedList, Node

def loop_detection(ll):
    """
    Given a circular LL, return node at beginning of loop.
    Circular LL: a corrupt LL in which a node's next pointer points to an 
                 earlier node.
    """
    curr = ll.head
    seen = set([curr.value])
    while curr:
        if curr.next.value not in seen:
            seen.add(curr.value)
            curr = curr.next
        else:
            return curr.next
    return None

def loop_detection2(ll):
    r = curr = ll.head
    while r and r.next:
        r = r.next.next
        curr = curr.next
        if r is curr:
            break
    
    if r is None or r.next is None: # not circular LL
        return None

    curr = ll.head
    while curr is not r:
        curr = curr.next 
        r = r.next
    return r






