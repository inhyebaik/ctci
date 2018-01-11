# Hash Tables
# ArrayList & Resizable Arrays 
# StringBuilder

def hash_key(key, capacity):
    """ Returns hash code address (or index) for key (str) within capacity (%) """
    return hash(str(key)) % capacity

class HashTable(object):

    def __init__(self, capacity=1000):
        self.capacity = capacity # default is 1000 to decrease P(collisions)
        self.count = 0
        self.hashmap = [[] for i in range(self.capacity)]
        self._keys = []

    def __repr__(self):
        pairs = []
        for item in self.hashmap:
            if item:
                key, value = item[0], item[1]
                pair = "{}: {}".format(str(key), str(value))
                pairs.append(pair)
        return "{ " + ", ".join(pairs) + " }"

    def set(self, key, value):
        index = hash_key(key, self.capacity)
        if self.count >= self.capacity: # if no room, resize
            self.resize()
        if self.hashmap[index] == []:   # if new key, add to keys and count
            self.count += 1
            self._keys.append(key)
        self.hashmap[index] = (key, value) # update hashmap

    def get(self, key):
        index = hash_key(key, self.capacity)
        bucket = self.hashmap[index]
        if bucket and bucket[0] == key: 
            return bucket[1]
        else:
            raise KeyError(key)

    def keys(self):
        return self._keys

    def values(self):
        values = []
        for bucket in self.hashmap:
            if bucket:
                values.append(cointainer[1])
        return values

    def items(self):
        items = []
        for bucket in self.hashmap:
            if bucket:
                items.append(bucket)
        return items

    def resize(self):
        if self.count >= self.capacity: # if full capacity
            self.hashmap += [[] for i in range(self.capacity)] # double capacity
            self.capacity = len(self.hashmap) # update capacity

    def delete(self, key):
        index = hash_key(key, self.capacity)
        bucket = self.hashmap[index]
        if bucket and bucket[0] == key:
            bucket = [] 
            self.count -= 1
            self._keys.remove(key)
        else:
            raise KeyError(key)
 

def string_builder(*words): 
    """
    This is much more efficient than concatenating strings since strings are 
    immutable objects, thus if you concatenate a string with another, the result 
    is a NEW string object (the problem is the same with Java strings).
    """
    return ''.join(words) # words = tuple of args

def reverse_in_place(word):
    letters = list(word) # strings are immutable 
    for i in range(0, len(word)/2): 
        letters[i], letters[len(word)-1-i] = letters[len(word)-1-i], letters[i]
    return ''.join(letters)


# Interview Questions 
# 1.1 
def is_unique(string):
    """ 
    Check if string has all distinct characters, not using other data 
    structures
    """
    for s in string: 
        if string.count(s) > 1:
            return False
    return True

# 1.2 
def is_permutation(a, b):
    """ Check if string a is a permutation of string b """
    alist = permutation(a)
    return b in alist

def permutation(a):
    """ Return list of permutations of string a """
    if len(a) < 2:
        return [a]
    result = []
    for i in range(len(a)):
        part = a[i:] + a[i+1]
        for m in permutation(part):
            result.append(a[i:i+1]+m)
    return result

# 1.3
def urlify(s, l):
    """ 
    Replace spaces in given string (with length l) with '%20' 
    Input:  "Mr John Smith      ", 13
    Output: "Mr%20John%20Smith"
    """
    h = s.split()
    return '%20'.join(h)


# 1.4
def palindrome_permutation(string):
    """
    Check if a string is permutation of a palindrome
    input: 'Tact Coa'
    Output: True (permutations: 'taco cat', 'atco cta', etc.)
    """
    counts = {}
    odds = 0
    # remove white space and make all chars lowercase
    string = ''.join(string.lower().split())
    # track character counts
    for s in string:
        if s is not ' ':
            counts[s] = string.count(s)
    # track number of even-count letters and odd-count letters
    for s in counts.keys():
        if counts[s] % 2 != 0:
            odds += 1
    if odds > 1:  # too many odds, can't be a palindrome
        return False
    elif odds == 0 and len(string) % 2 == 0: # if no odds, the length has to be even
        return True
    elif odds == 1 and len(string) % 2 != 0: # if odds = 1, the length has to be odd
        return True
    else:
        return False

# 1.5 
def one_away(s1, s2):
    """
    Check if string a is one edit away (insert, delete, or replace a character) 
    from string b --> order matters
    """
    a = list(s1)
    b = list(s2)
    if len(a) + 1 == len(b): # check for insertion
        if len(b) == len(set(b)): # no duplicates 
            diff = set(b).difference(set(a)).pop()
            index = b.index(diff)
            del b[index]
            if a == b:
                return True
        else:
            for l in b:
                if b.count(l) > 1:
                    index = b.index(l)
                    rindex = s2.rindex(l)
                    if a[index] == b[index]: # use rindex
                        del b[rindex]
                    elif a[rindex] == b[rindex]: # use index
                        del b[index]
                    if a == b: 
                        return True
    elif len(a) - 1 == len(b) or len(a) == len(b): # check for deletion and replacement
        if len(a) == len(set(a)): # no duplicates; automatic for replacement
            diff = set(a).difference(set(b)).pop()
            index = a.index(diff)
            b.insert(index, diff)
            if a == b:
                return True
        else: # there are duplicates! cat vs. catt; cat vs. ctat
            for l in a:
                if a.count(l) == 2:
                    index = a.index(l)
                    rindex = s1.rindex(l) # rindex works on strings but not lists
                    print index, rindex
                    print a[index], b[index]
                    if a[index] == b[index]: # use rindex
                        del a[rindex]
                    elif a[rindex] == b[rindex]: # use index
                        del a[index]
                    if a == b: 
                        return True
    else:
        return False

# print one_away('caat', 'cat')

# 1.6 O(N)
def compress_string(s):
    """ 
    Input: 'aabccccaaa' (only upper and lower case letters)
    Output: 'a2b1c4a3'
    If ouput is NOT smaller than original, then return original string.
    Every letter will take 2 spots in output.
    """ 
    compressed = []
    count = 0
    for i in range(len(s)):
        if s[i] != s[i-1] and i != 0:
            compressed.append(s[i-1] + str(count))
            count = 0
        count += 1
    # add last repeated character
    compressed.append(string[-1] + str(counter))
    return min(s, ''.join(compressed), key=len)

# 1.7 O(N^2)
def rotate_matrix(matrix):
    """Return square matrix rotated 90 deg. in place."""
    n = len(matrix)
    for layer in range(n//2):
        first = layer
        last = n - layer - 1
        for i in range(first, last):
            # save top
            top = matrix[layer][i]
            
            # left to top
            matrix[layer][i] = matrix[-i-1][layer]

            # bottom to left
            matrix[-i-1][layer] = matrix[-layer-1][-i-1]

            # right to bottom
            matrix[-layer-1][-i-1] = matrix[i][-layer-1]

            # top to right
            matrix[i][-layer-1] = top


matrix = [  [1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20],
            [21, 22, 23, 24, 25]
        ]




