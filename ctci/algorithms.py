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

# O(log N)
def binary_search(L, target):
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


def bubble_sort(L):
    """
    Space: O(1)
    Time (worst/average, best): O(N^2), Omega(N)
    """
    if len(L) < 2:
        return
    s = False
    while not s:
        s = True
        for i in range(len(L)-1):
            if L[i] > L[i+1]:
                s = False
                L[i], L[i+1] = L[i+1], L[i]

def quick_sort(L):
    """
    # Space: O(log N)
    # Time (worst, average): O(N^2), O(N log N)
    """
    if len(L) < 2: 
        return L
    lo = quick_sort([x for x in L[1:] if x <= L[0]])
    hi = quick_sort([x for x in L[1:] if x > L[0]])
    return lo + [L[0]] + hi


def msort(L):
    """
    # Space: O(N)
    # Time: O(N log N)
    """
    if len(L) < 2:
        return L
    r = []
    mid = len(L)//2
    a = msort(L[:mid])
    b = msort(L[mid:])
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

def msort2(L):
    if len(L) < 2:
        return L
    r = []
    mid = len(L)//2
    a = msort2(L[:mid])
    b = msort2(L[mid:])
    i, j = 0, 0
    while a and b:
        if a[i] > b[j]:
            r.append(b[j])
            j += 1
        else:
            r.append(a[i])
            i += 1






