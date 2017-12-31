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

# You need to concatenate lots of string elements. 
# Java we use a StringBuilder for this
# Python solution: Use a list, and join the elements of the list at the end. 
# This is much more efficient than concatenating strings since strings are 
# immutable objects, thus if you concatenate a string with another, the result 
# is a NEW string object (the problem is the same with Java strings).
def string_builder(*words): 
    return ''.join(words) # words = tuple of args

def reverse_in_place(word):
    letters = list(word) # strings are immutable 
    for i in range(0, len(word)/2): 
        letters[i], letters[len(word)-1-i] = letters[len(word)-1-i], letters[i]
    return ''.join(letters)






