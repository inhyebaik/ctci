# 3.5 
""" 
Sort Stack: Write a program to sort a stack such that the smallest items are on 
the top. You can use an additional temporary stack, but you may not copy the 
elements into any other data structure (such as an array). The stack supports 
the following operations: push, pop, peek, and isEmpty.
""" 
class Stack(object):
    def __init__(self):
        self._list = []

    def pop(self):
        return self._list.pop()

    def push(self, item):
        self._list.append(item)

    def peek(self):
        return self._list[-1]

    def isEmpty(self):
        return not self._list

class SortedStack(object):
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def push(self, item):
        self.stack1.push(item)

    def sort(self):
        # sort items in stack2 in ascending order
        while not self.stack1.isEmpty(): 
            tmp = self.stack1.pop() 
            while (not self.stack2.isEmpty()) and (self.stack2.peek() > temp):
                self.stack1.push((self.stack2.pop()))
            self.stack2.push(tmp) 

        # since we want smaller items at the end, reverse pop and push to stack1
        while not self.stack2.isEmpty():
            self.stack1.push(self.stack2.pop())

    def pop(self):
        """ Removes and returns the smallest item (at the top) of the stack. """
        self.sort()
        return self.stack2.pop()

    def peek(self):
        return self.stack2.peek()

    def isEmpty(self):
        return (not self.stack1 and not self.stack2











            







