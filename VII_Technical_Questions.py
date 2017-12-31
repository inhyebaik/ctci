# p. 67 Optimize and Solve Technique #1: Look for BUD
# (Bottlenecks, Unecessary work, Duplicated work)

# p. 67 Bottlenecks: part of your algo that slows down overall time
# Given an array of unique integers, count number of pairs with difference k
def pairs_k_diff(alist, k):
    h = set(alist)
    count = 0
    for num in h: 
        if num+k in set:
            count += 1
        if num-k in set:
            count += 1

# p. 68 Unnecessary and Duplicate Work
    # Print integer solutions for a**3 + b**3 = c**3 + d**3 where a, b, c, d 
    # are each within 1-1000

n = 10 # for testing

# O(N^4)
# Unnecessary and Duplicate Work
# Finding (a, b) pairs is the same as finding (c, d pairs)
def f(n):
    n += 1
    for a in range(1,n):
        for b in range(1,n):
            for c in range(1,n):
                for d in range(1,n):
                    if a**3 + b**3 == c**3 + d**3:
                        print a, b, c, d

# O(N^3)
# Iterating 1-n for d is unecessary if we have a, b c
def f2(n):
    n += 1
    for a in range(1,n):
        for b in range(1,n):
            for c in range(1,n):
                d = pow(a**3 + b**3 - c**3, (1/3))
                if a**3 + b**3 == c**3 + d**3 and d > 0 and d < n:
                    print a, b, c, d

# O(N^2)
# Eliminate duplicate work of finding a, b pairs
def f3(n):
    m = {}
    n += 1
    for c in range(1,n):
        for d in range(1,n):
            result = c**3 + d**3
            m[result] = m.get(result, [])
            m[result].append((c,d))
    for lst in m.values(): # if only 1 tuple in list, print it twice (c,d), (c,d)
        for pair1 in lst:  # if 2 tuples, print both of them (c1, d1), (c2, d2)
            for pair2 in lst:
                print pair1, pair2


# p. 70 Optimize and Solve Technique #2: DIY. 
    # Think intuitively (BSTs are not intuitive)
    # Given a substring s in string b, find all permutations of s within b;
    # print the location of each permutation

def s_perm_in_b(s, b):
    s_perms = permutations(s)
    b_chunks = b_chunk(s, b)
    for sub in s_perms:
        if sub in b_chunks.keys():
            print sub, b_chunks[sub]

# O(B-S)
def b_chunk(s, b):
    """ 
    Returns dictionary of keys (segments in b with length s)
    and values (indices of where the segment begins)
    
    >>> b_chunk('ca', 'abbcbb') == {'ab': [0], 'bb': [1, 4], 'bc': [2], 'cb': [3]}
    """
    d = {}
    if len(s) > len(b):
        return
    if len(s) == len(b):
        return {b:[0]}
    for i in range(len(b)-len(s)):
        chunk = b[i:i+len(s)]
        d[chunk] = d.get(chunk, [])
        d[chunk].append(i)
    return d

# p. 71 Optimize and Solve Technique #3: Simplify and Generalize.

# p. 72 Optimize and Solve Technique #4: Base Case and Build.
# Particularly for recursions -- try to see the general pattern

# O(N * N!)
def permutations(s):
    """ Returns list of permutations of string s """
    if len(s) < 2:
        return [s]
    else:
        temp = []
        for i in range(len(s)):
            part = s[:i] + s[i+1:]
            for m in permutations(part):
                temp.append(s[i:i+1]+m)
        return temp

# p.72 Optimize & Solve Technique #5: Data Structures Brainstorm.

# keeping track of median as you add numbers to a collection -- not good to use 
# linked list (accessing is hard); a balanced BST's top node can be median but 
# there is an even number of nodes, we'd have to divide the 2 middle nums to float;
# perhaps use heap, etc...

# p.73 An Example of How to Use BCR.
# Given 2 sorted arrays, find the number of elements in common. The arrays are the 
# same length with unique items

a = [13, 27, 35, 40, 49, 55, 59]
b = [17, 35, 39, 40, 55, 58, 60]

# O(N), Space: O(1)
def num_common(a, b):
    common = 0
    j = 0 # tracking index in b
    for i in range(len(a)):
        if a[i] == b[j]:
            common += 1
        elif a[i] > b[j]:
            while a[i] > b[j]:
                j += 1
                if a[i] == b[j]:
                    common += 1
    return common

# p.79 Appropriate Code Reuse.
#Write a functino to check if the value of a binary number passed as a string 
# equals the hex representation of a string

# Using built-in functions.
def built_in_compare(bin, hex):
    return int(bin, 2) == int(hex, 16)

def compare_bin_to_hex(bin, hex):
    return convert_from_base(bin) == convert_from_base(hex)

def bin_to_dec(bin_str):
    """ Converts binary string to decimal int """
    result = 0
    for bit in bin_str:
        result *= 2
        if bit == '1':
            result += 1
    return result

def convert_from_base(num_str, base):
    """ Converts a number string in base (2 or 16) to decimal int """
    if base != 2 or base != 16:
        return -1
    s = '0123456789ABCDEF' 
    result = 0
    for bit in num_str:
        result *= base
        result += s.find(bit)
    return result

# p. 80 Modular Code.
# swap the max and min element in an integer array (e.g. create helper functions)

# O(N)
def swap_min_max(alist):
    min_index = get_min_index(alist)
    max_index = get_max_index(alist)
    alist[min_index], alist[max_index] = alist[max_index], alist[min_index]

# O(N)
def get_min_index(alist):
    if len(alist) == 1:
        return alist[0]
    min_index = 0
    m = alist[0]
    for i in range(len(alist)):
        if alist[i] < m:
            min_index = i
            m = alist[i]
    return min_index

# O(N)
def get_max_index(alist):
    if len(alist) == 1:
        return alist[0]
    max_i = 0
    m = alist[0]
    for i min range(len(alist)):
        if alist[i] > m:
            max_i = i
            m = alist[i]
    return max_i

# The goal is write beautiful code. Don't give up :)
