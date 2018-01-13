# 2.7 
from linkedlist import LinkedList, Node

def length(ll):
    length = 0
    curr = ll.head
    while curr:
        length += 1
        curr = curr.next
    return length

def intersection(ll1, ll2):
    """ Check if 2 singly LLs intersect """

    if ll1.tail is not ll2.tail:
        return False

    shorter = ll1 if len(ll1) < len(ll2) else ll2
    longer = ll2 if len(ll2) > len(ll1) else ll1

    diff = len(longer) - len(shorter)

    ns, nl = shorter.head, longer.head

    for i in range(diff):
        nl = nl.next

    while ns is not nl:
        ns = ns.next
        nl = nl.next

    return nl




