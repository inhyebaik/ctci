# 3.3 
"""
Stack of Plates: Imagine a (literal) stack of plates. If the stack gets too high,
it might topple. Therefore, in real life, we would likely start a new stack when
the previous stack exceeds some threshold. Implement a data structure SetOfStacks
that mimics this. SetOfStacks should be composed of several stacks and should 
create a new stack once the previous one exceeds capacity. SetOfStacks. push () 
and SetOfStacks. pop () should behave identically to a single stack (that is, 
pop ( ) should return the same values as it would if there were just a single 
stack).
"""

class Stack(object):
    def __init__(self, inlist=[]):
        self._list = inlist

    def __repr__(self):
        if not self._list:
            return "<Stack empty>"
        else:
            return self._list

    def push(self, item):
        self._list.append(item)

    def pop(self):
        return self._list.pop()

    def peek(self):
        return self._list[-1]

    def isEmpty(self):
        return not self._list

class SetofStacks(object):
    def __init__(self, capacity=100):
        self._list = [[]]
        self.capacity = capacity
    
    def size(self):
        count = 0
        for stack in self._list:
            count += len(self._list)
        return count

    def resize(self):
        self._list.append([])

    def need_new_stack(self):
        """ Checks if we need to start a new stack. """
        return self.size() >= self.capacity

    def pop(self):
        return self._list[-1].pop()

    def push(self, item):
        if self.need_new_stack():
            self.resize()
        self._list[-1].append(item)

    def peek(self):
        self._list[-1][-1]

# FOLLOW UP: Implmenet .popAt(index) which performs .pop() at a specific stack
    def pop_at(self, index):
        num_stacks = len(self._list)
        if index not in range(-num_stacks, num_stacks):
            return self._list[index].pop()
        else:
            raise "Stack index out of range (Stack count: {})".format(num_stacks)








