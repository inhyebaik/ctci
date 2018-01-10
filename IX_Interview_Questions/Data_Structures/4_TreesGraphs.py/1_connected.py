

class GraphNode(object):
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

    def connected_DFS(self, node1, node2):
        """ Checks if there's a route between 2 nodes. """
        to_visit = [node1]
        seen = set()

        while to_visit:
            curr = to_visit.pop()
            seen.add(curr)
            if curr == node2:
                return True
            else:
                for a in curr.adjacent - seen:
                    to_visit.append(a)
                    seen.add(a)
        return False

    def connected_BFS(self, node1, node2):
        """ BFS queue """
        to_visit = [node1]
        seen = set()

        while to_visit:
            curr = to_visit.pop(0)
            seen.add(curr)
            if curr == node2:
                return True
            else:
                for a in curr.adjacent - seen:
                    to_visit.append(a)
                    seen.add(a)

        return False


    def connected_recursive(self, node1, node2, seen=None):
        if node1 == node2:
            return True

        if not seen:
            seen = set()
        seen.add(node1)

        for a in node1.adjacent - seen:
            if self.connected_recursive(a, node2, seen=seen):
                return True
        return False







