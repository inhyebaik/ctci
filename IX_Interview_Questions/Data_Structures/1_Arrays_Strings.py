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
        container = self.hashmap[index]
        if container and container[0] == key: 
            return container[1]
        else:
            raise KeyError(key)

    def keys(self):
        return self._keys

    def values(self):
        values = []
        for container in self.hashmap:
            if container:
                values.append(cointainer[1])
        return values

    def items(self):
        items = []
        for container in self.hashmap:
            if container:
                items.append(container)
        return items

    def resize(self):
        if self.count >= self.capacity: # if full capacity
            self.hashmap += [[] for i in range(self.capacity)] # double capacity
            self.capacity = len(self.hashmap) # update capacity

    def delete(self, key):
        index = hash_key(key, self.capacity)
        container = self.hashmap[index]
        if container and container[0] == key:
            container = [] 
            self.count -= 1
            self._keys.remove(key)
        else:
            raise KeyError(key)


def 