# 3.6
""" 
Animal Shelter: An animal shelter, which holds only dogs and cats, operates on 
a strictly "first in, first out" basis. People must adopt either the "oldest" 
(based on arrival time) of all animals at the shelter, or they can select 
whether they would prefer a dog or a cat (and will receive the oldest animal of 
that type). They cannot select which specific animal they would like. Create
the data structures to maintain this system and implement operations such as 
enqueue, dequeueAny, dequeueDog, and dequeueCat. You may use the built-in 
Linked List data structure.
""" 

class Node(object):
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, node):
        if self.tail:
            self.tail.next = node
            self.tail = self.tail.next
        else:
            self.tail = self.head = node

    def add_to_beginning(self, node):
        if self.head:
            old_head = self.head
            self.head = node
            self.head.next = old_head
        else:
            self.add(node)

    def dequeue(self):
        """ Removes first item in LL. """
        if not self.head:
            return 'Nothing to dequeue'
        old_head = self.head
        self.head = self.head.next
        old_head.next = None
        return old_head

    def add_multiple(self, nodes):
        for n in nodes:
            self.add(v)

    def count(self):
        count = 0
        curr = self.head 
        while curr:
            count += 1
            curr = curr.next
        return count


class Animal(object):
    def __init__(self, species, next=None):
        if species.lower() in ['dog', 'cat']:
            self.species = species # cat or dog
        else:
            raise 'species must be dog or cat' 
        self.next = next

class AnimalShelter(object):
    def __init__(self, animals=[]):
        self.head = None
        self.tail = None
        if animals:
            self.add_multiple(animals)

    def add(self, new_animal):
        if not self.head:
            self.tail = self.head = new_animal
        else:
            self.tail.next = new_animal
            self.tail = self.tail.next

    def add_multiple(self, animals):
        for a in animals:
            self.add(a)
    
    def dequeueDog(self):
        if self.head.species is 'dog':
            return self.dequeueAny()
        
        curr = self.head
        while curr and curr.next:

            if curr.next.species is 'dog':
                oldest_dog = curr.next
                
                if curr.next is self.tail:
                    self.tail = curr
                    curr.next = None
                else:
                    curr.next = curr.next.next
                oldest_dog.next = None
                return oldest_dog
            
            else:
                curr = curr.next

        return 'No dogs!'


    def dequeueCat(self):
        if self.head.species is 'cat':
            return self.dequeueAny()
        
        curr = self.head
        while curr and curr.next:

            if curr.next.species is 'cat':
                oldest_cat = curr.next
                if oldest_cat is self.tail:
                    self.tail = curr
                    curr.next = None
                else: 
                    curr.next = curr.next.next
                oldest_cat.next = None
                return oldest_cat
            
            else:
                curr = curr.next
        
        return 'No cats!'


    def dequeueAny(self):
        if not self.head:
            raise "No animals in the shelter!"
        else:
            old_head = self.head
            self.head = self.head.next
            old_head.next = None
            return old_head



# using 2 separate linked lists for cats and dogs, and animals with entry number

class Animal2(object):
    def __init__(self, species, next=None):
        if species.lower() in set(['dog', 'cat']):
            self.species = species.lower()
        else:
            raise "species must be 'dog' or 'cat'"
        self.next = next
        self._entry_num = None

class AnimalShelter2(object):
    """ Using separate linked lists for cats and dogs """
    def __init__(self):
        self.cats = LinkedList()
        self.dogs = LinkedList()
        self.count = 0

    def add(self, new_animal):
        self.count += 1
        new_animal._entry_num = self.count

        if not self.tail:
            self.tail = self.head = new_animal
        else:
            self.tail.next = new_animal
            self.tail = self.tail.next

    def dequeueCat(self):
        if not self.cats.head:
            return "No cats to dequeue"
        else:
            return self.cats.dequeue()

    def dequeueDog(self):
        if not self.dogs.head:
            return 'No dogs to dequeue'
        else:
            return self.dogs.dequeue()

    def dequeueAny(self):
        if not self.cats.head:
            return self.dequeueDog()
        if not self.dogs.head():
            return self.dequeueCat()

        if self.cats.head._entry_num < self.dogs.head._entry_num:
            return self.dequeueCat()
        else:
            return self.dequeueDog()





