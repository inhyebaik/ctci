class Queue(object):

    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, item):
        if not self.head:
            self.tail = self.head = item
        else:
            if self.tail:
                self.tail = 


