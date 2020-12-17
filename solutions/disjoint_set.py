class DisjointSet:
    def __init__(self):
        self.parent = {}

    def add(self, item):
        self.parent[item] = item
    
    def find(self, item):
        if self.parent[item] == item:
            return item
        else:
            return self.find(self.parent[item])

    def union(self, a, b):
        parent_a = self.find(a)
        parent_b = self.find(b)
        self.parent[parent_b] = parent_a


x = DisjointSet()
x.add(1)
x.add(2)
x.add(3)
x.add(4)
x.add(5)
x.union(1, 2)
x.union(2, 3)
assert x.find(3) == 1
assert x.find(2) == 1
assert x.find(1) == 1
assert x.find(4) == 4
assert x.find(5) == 5