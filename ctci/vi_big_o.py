L = [1,2,3,4,5]

# Example 1
# O(N)
def foo(L):
    s = 0
    product = 1
    for i in range(len(L)):
        s += L[i]
    for i in range(len(L)):
        product *= L[i]
    print "{}, {}".format(s, product)

# Example 2
# O(N^2)
def print_pairs(L):
    """ N^2 pairs for N=len(L) """
    for i in range(len(L)):
        print ""
        for j in range(len(L)):
            print "({}, {})".format(L[i], L[j]),

# (1, 1) (1, 2) (1, 3) (1, 4) (1, 5) 
# (2, 1) (2, 2) (2, 3) (2, 4) (2, 5) 
# (3, 1) (3, 2) (3, 3) (3, 4) (3, 5) 
# (4, 1) (4, 2) (4, 3) (4, 4) (4, 5) 
# (5, 1) (5, 2) (5, 3) (5, 4) (5, 5) => 25 pairs for N=5 

# Example 3 
# O(N^2) - does half the work as print_pairs, but no duplicate pairs 1,1 or 2,2
def print_unordered_pairs(L):
    """ 
    N = len(L)
    The outer i-loop runs N times.
    The inner j-loop runs N-1 steps in the 1st iteration of the i-loop, N-2 in 
    the 2nd iteration of the i-loop, etc.
    The sum of 1 through N-1 is N(N-1)/2
    """
    for i in range(len(L)):
        print ""
        for j in range(i+1, len(L)):
            print "({}, {})".format(L[i], L[j]),

# (1, 2) (1, 3) (1, 4) (1, 5) 
# (2, 3) (2, 4) (2, 5) 
# (3, 4) (3, 5) 
# (4, 5) => 10 pairs for N=5

# Example 4 
# O(ab)
def print_unordered_pairs(a, b):
    """ 
    The j-loop is a sequence of constant if-statements.
    Each element of a goes through b iterations. 
    """
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i]<b[j]:
                print "{}, {}".format(a[i], b[i])
a=[1,2,3]
b=[5,6,7]

print_unordered_pairs(a,b) 
    # 1, 5
    # 1, 5
    # 1, 5
    # 2, 6
    # 2, 6
    # 2, 6
    # 3, 7
    # 3, 7
    # 3, 7
print_unordered_pairs(b,a) # prints nothing since nothing in b is less than a 
                           # by corresponding indicies

# Example 5 
# O(a*b)
def print_unordered_pairs_k(a, b):
    """ 5 units of work is still constant """
    for i in range(len(a)):
        for j in range(len(b)):
            for k in range(5):
                print "{}, {}".format(a[i], b[i])

# Example 6
# O(N)
def reverse(L):
    for i in range(len(L)/2):
        other = len(L)-i-1
        temp = L[i]
        L[i] = L[other]
        L[other] = temp

# Example 8
# O(a*s(log a + log s))
def sort_strings_and_list(a):
    """
    Sorting a string = O(s log s)
    ...for each string in a = O(s log s)*O(a) = O(a * slogs)

    Sorting all strings:
        each string comparison = O(s)
        # of comparison = O(aloga)
    """
    a = map(lambda s:''.join(sorted(s)), a) 
    a = sorted(a)
    print a

a = ['bac', 'cbacc', 'bcad']

# Example 9
# O(N)
def sum_nodes_bst(node):
    """ Sums all nodes of BST """
    current = node
    if not current:
        return 0
    return sum_nodes_bst(node.left) + node.value + sum_nodes_bst(node.right)

# Example 10
# O(N^0.5)
def is_prime(n):
    if n < 2:
        return False
    for x in range(2, n**0.5+1):
        if n%x == 0:
            return False
    return True

# Example 11
# O(N)
def factorial(n):
    """ This is a recursion fron n to n-1 to n-2 down to 1 ==> O(N) """
    if n < 0:
        return -1
    elif n == 0:
        return 1
    else:
        return n * factorial(n-1)


# Example 12
def permute_string(str):
    if len(str) == 0:
        return ['']
    prev_list = permute_string(str[1:len(str)])
    next_list = []
    for i in range(0,len(prev_list)):
        for j in range(0,len(str)):
            print "\n (i, j) = ", (i, j)
            print "prev_list=", prev_list
            print "prev_list[{}][0:{}] = ".format(i, j), prev_list[i][0:j]
            print "str[0] = ", str[0]
            print "prev_list[{}][{}:{}] = ".format(i, j, len(str)-1), prev_list[i][j:len(str)-1]
            new_str = prev_list[i][0:j] + str[0] + prev_list[i][j:len(str)-1]
            print "new_str = ", new_str
            if new_str not in next_list:
                next_list.append(new_str)
            print "next_list = ", next_list
    return next_list

# Example 13
# O(2^N)
# Generally, algorithms with multiple recursive calls --> exponential runtime
# O(branches ^ depth)
def fib(n):
    """Returns nth Fibonacci number, starting from 1."""
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

# Example 14
def print_fib(n):
    """Prints Fibonacci numbers from 0 through n."""
    for i in range(n):
        print fib(i)

"""
Space complexity of non-memoized function:
Space complexity also includes the callstack. 
Although all 2^n items will enter the callstack by the end of the program, they 
don't sit there all at the same time. 
The biggest your callstack gets is O(n) (for fib(n-1) recursions. They will break 
    the callstack before the fib(n-2) calls start).
The memoized solution: O(n) for callstack, and O(n) for cache table => O(n)
""" 
# Example 15 
# O(N): Fib with memoization  
def fib_m(n):
    def fib_memo(n, m):
        """
        Find the n'th fibonacci number. Uses memoization.

        :param n: the n'th fibonacci number to find
        :param m: dictionary used to store previous numbers
        :return: the value of the n'th fibonacci number
        """
        if n in m:
            return m[n]
        result = fib_memo(n-1, m) + fib_memo(n-2, m)
        m[n] = result
        return result
    m = {1:1, 2:1}
    return fib_memo(n, m)

# Example 16
# O(log N): The number of times we divide 50 by 2 until we reach the basecase(1)
def powers2(n):
    """Prints powers of 2 between 1 and n."""
    if n < 1:
        return 0
    if n == 1:
        print 1
        return 1
    prev = powers2(n/2)
    curr = prev * 2
    print curr
    return curr

# Additional Problems 

# 1. O(b)
def product(a, b):
    """ Computes product of a and b """
    sum = 0
    for i in range(b):
        sum += a
    return sum

# 2. O(b)
def power(a, b):
    """ Computes a ^ b """
    if b < 0:
        return 0 
    elif b == 0: 
        return 1
    else:
        return a * power(a, b-1)

# 3. O(1)
def mod(a, b):
    """ Computes a % b """
    if b <= 0:
        return -1
    div = a/b
    return a - div * b

# 4. O(a/b)
def div(a, b):
    """ Computes integer division"""
    count = 0
    sum = b
    while sum <= a:
        sum += b
        count += 1
    return count

# 5. O(log N)
def sqrt(n):
    """ Computes int sqrt of n. 
    If n is not a perfect square, it returns -1 through successive guessing.
    If n = 100, the first guess is 50. 
    """
    return sqrt_helper(n, 1, n)

def sqrt_helper(n, min, max):
    if max < min:
        return -1 # no square root
    guess = (min + max)/2
    if guess * guess == n:
        print "found it!"
        return guess
    elif guess * guess < n: # too low
        print "too low!Trying min={}, max={}".format(guess + 1, max)
        return sqrt_helper(n, guess + 1, max)
    else: # too high 
        print "too high! Trying min={}, max={}".format(min, guess-1)
        return sqrt_helper(n, min, guess - 1) 

# 6. O(N^0.5)
def sqrt2(n):
    """ Computes int sqrt of n. 
    If n is not a perfect square, it returns -1 by trying increasing large values
    until it finds the right value or is too high.
    """
    guess = 1
    while guess*guess <= n:
        if guess * guess == n:
            return guess
        guess += 1
    return -1

# 9. O(N^2)
def copy_arr(arr):
    copy = [0]
    for value in arr:
        copy = append_to_new(copy, value)
    return copy

def append_to_new(arr, value):
    bigger = [len(arr)+1]
    for i in range(len(arr)):
        bigger[i] = arr[i]
    bigger[len(bigger)-1] = value 
    return bigger

# 10. O(log N) : number of digits. n = 10^d
def sum_digits(n):
    """ Sums digits in a number."""
    sum = 0
    while n > 0:
        sum += n % 10
        n /= 10
    return sum

# 11. 
def print_sorted_str(rem):
    print_sorted_str(rem, "")

def print_sorted_str(rem, prefix):
    """ Prints all strings of length k where characters are sorted by generating 
    all strings of length k and then checking if each is sorted
    """
    pass 

# 12. O(b log b + a log b)
def intersection(a, b): 
    """
    Computes intersection of arrays, assuming no duplicates, by sorting array b
    and iterating through array a checking (binary search) if each value is in b
    """
    b = msort(b) # O(b log b)
    intersect = 0
    for x in a: # O(a)
        if binarysearch(b, x) >= 0:  # O(a) * O(log b) = O(a log b)
            intersect += 1
    return intersect

# O(N log N)
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

# O (log N)
def binarysearch(L, target):
    first = 0 
    last = len(L)-1
    found = False
    while first <= last and not found:
        mid = (first + last)//2 
        if L[mid] == target:
            print "found!"
            found = True
        else:
            if L[mid] > target: # too high
                print "too high! trying first:{}, last:{}".format(first, mid-1)
                last = mid - 1
            else: # too low
                print "too low! trying first: {}, last:{}".format(mid+1, last)
                first = mid + 1















