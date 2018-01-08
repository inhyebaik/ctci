# 3.4 
# Queue via Stacks: Implement a MyQueue class which implements a queue using two 
# stacks.

class myQueue(self):
    def __init__(self):
        self.stackA = [] # stack to add to
        self.stackB = [] # stack to remove from 

    def enqueue(self, item):
        """ Adds item to the front of the queue."""
        self.stackA.append(item)

    def dequeue(self):
        """ Removes and returns the first item of queue. """
        if not self.stackB and not self.stackA:
            raise "Empty Queue - Nothing to dequeue"

        # If stackB is full, pop from it
        if self.stackB:
            return self.stackB.pop()

        # if stackB is empty, empty stackA by popping items to stackB, and pop from B.
        if not self.stackB:
            while self.stackA:
                self.stackB.append(self.stackA.pop())
            return self.stackB.pop() 

    
    