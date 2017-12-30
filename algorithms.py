"""
Algorithms:
    BFS
    DFS
    Binary Search 
    Merge Sort 
    Quick Sort
    Bubble Sort 
    Heap Sort
    Insertion Sort
"""

# O(log N): Binary Search assumes a sorted list 
def binarysearch(L, target):
    """ Returns boolean whether target is in (sorted) list. """
    first = 0 
    last = len(L)-1
    found = False
    while first =< last and not found:
        mid = (first + last)//2
        print "Trying L[mid] = {}".format(L[mid])
        if L[mid] == target:
            found = True
        elif L[mid] > target:
            print "Too high! Adjusting...first={}, last={}".format(first, mid-1)
            last = mid - 1
        else:
            print "Too low! Adjusting...first={}, last={}".format(mid+1, last)
            first = mid + 1
    return found

def bubblesort(alist):
    if len(alist) < 2:
        return
    s = False
    while not s:
        s = True
        for i in range(len(alist)-1):
            if alist[i] > alist[i+1]:
                s = False
                alist[i], alist[i+1] = alist[i+1], alist[i]

def quicksort(a_list):
    if len(a_list) < 2: 
        return a_list
    lo = quicksort([x for x in a_list[1:] if x <= a_list[0]])
    hi = quicksort([x for x in a_list[1:] if x >  a_list[0]])
    return lo + [a_list[0]] + hi


def msort(alist):
    if len(alist) < 2:
        return alist
    r = []
    mid = len(alist)/2
    a = msort(alist[:mid])
    b = msort(alist[mid:])
    while a and b:
        if a[0] < b[0]:
            r.append(a.pop(0))
        else:
            r.append(b.pop(0))
    if not a:
        r.extend(b)
    else:
        r.extend(a)
    return r

def msort2(alist):
    if len(alist) < 2:
        return alist
    r = []
    mid = len(alist)/2
    a = msort2(alist[:mid])
    b = msort2(alist[mid:])
    i, j = 0, 0
    while a and b:
        if a[i] > b[j]:
            r.append(b[j])
            j += 1
        else:
            r.append(a[i])
            i += 1






