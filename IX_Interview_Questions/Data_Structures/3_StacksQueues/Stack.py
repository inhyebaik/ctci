class Queue(object):
    def __init__(self, queue=[]):
        self.queue = queue

    def __repr__(self):
        return self.queue 

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        return self.queue[0]
        del self.queue[0]

    def is_empty(self):
        return not self.queue

    def peek(self):
        return self.queue[0]


class Stack(object):
    def __init__(self, stack=None):
        if stack:
            self._list = stack
        else:
            self._list = []

    def __repr__(self):
        return self.stack

    def push(self, item):
        self._list.append(item)

    def pop(self):
        if not self._list:
            raise IndexError
        return self._list.pop()

    def peek(self):
        print self._list[-1]

    def is_empty(self):
        return not self._list

    def length(self):
        return len(self._list)

