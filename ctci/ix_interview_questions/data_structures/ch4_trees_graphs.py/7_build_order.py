class Project(object):
    def __init__(self, value, dependents=None, parent=None):
        self.value = value
        self.parent = parent or []
        if dependents:
            self.dependents = dependents
        else:
            self.dependents = set()

    def __repr__(self):
        return self.value

    def add_dependents(self, x):
        self.dependents.add(x)
        x.parent.append(x)

    def is_dependent(self):
        return self.parent

    def has_dependents(self):
        return self.dependents
        
e = Project(value='e')
c = Project(value='c')
d = Project(value='d')
d.add_dependents(c)
b = Project(value='b')
b.add_dependents(d)
a = Project(value='a')
a.add_dependents(d)
f = Project(value='f')
f.add_dependents(a)
f.add_dependents(b)

class BigProject(object):
    def __init__(self):
        self.projects = set()

    def add_projects(self, L):
        for a in L:
            self.projects.add(a)

    def build_order(self):
        order_list = []
        ordered = set()
        to_visit = list(self.projects - ordered)
        
        while to_visit:
            project = to_visit.pop()
            # Add projects w/o parent earlier in ordered_list
            if not project.parent:
                order_list.append(project)
                # of its dependents, notify depedent that it no longer has a parent
                for d in project.dependents:
                    d.parent = None
                # add to ordered so we don't check it again
                ordered.add(project)
            else: 
                # add it back to to_visit; it will pop out once we get rid of its parent
                to_visit.append(project)
        return order_list

bp = BigProject()
bp.add_projects([a, b, c, d, e, f])
print bp.build_order()