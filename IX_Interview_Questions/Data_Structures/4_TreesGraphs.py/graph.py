class Node(object):
    def __init__(self, value, adjacent=None): 
        self.value = value
        # in Graphs, adjacent collections must be a set. We want uniques!
        if adjacent:
            assert isinstance(adjacent, set), \
                "adjacent must be a set!"
            self.adjacent = adjacent
        else:
            self.adjacent = set()

    def __repr__(self):
        return "<GraphNode {}>".format(value)

class Graph(object):
    """ Graph holding nodes and their adjacents. """
    def __init__(self):
        self.nodes = set()

    def __repr__(self):
        return "<Graph: {}>".format( [n.value for n in self.nodes] )

    def add_node(self, node):
        self.nodes.add(node)

    def set_adjacent(self, node1, node2):
        node1.adjacent.add(node2)
        node2.adjacent.add(node1)

    def are_connected_BFS(self, node1, node2):
        """ Are 2 nodes connected? BFS. """
        to_visit = Queue() 
        to_visit.enqueue(node1) # to_visit = [node1]
        seen = set() # avoid seeing same nodes again 
        seen.add(node1)

        while not to_visit.is_empty(): # while to_visit
            curr = to_visit.dequeue() # curr = to_visit.pop(0)
            if curr is node2:
                return True
            else:
                for a in curr.adjacent - seen:
                    to_visit.enqueue(a) # to_visit.append(a)
                    seen.add(a)
        return False

    def are_connected_DFS(self, node1, node2):
        """ Are 2 nodes connected? DFS. """
        to_visit = [node1] # Stack
        seen = set() # avoid seeing same people again
        seen.add(node1)

        while to_visit:
            curr = to_visit.pop()
            if curr is node2:
                return True
            else:
                for a in curr.adjacent - seen:
                    to_visit.append(a)
                    seen.add(a)
        return False

    def are_connected_recursive_DFS(self, node1, node2, seen=None):
        if not seen:
            seen = set()
        if node1 is node2:
            return True
        seen.add(node1) # keep track that we've visited here
        for a in node1.adjacent - seen
            if self.are_connected_recursive(a, node2, seen):
                return True
        return False

    