class BinTree():
    def __init__(self, value):
        self.root = BinTreeNode(value, 0)
        self.d = {}
        self.d[value] = self.root

    def add_left(self, target, value):
        node = BinTreeNode(value, self.d[target].depth + 1)
        self.d[target].left = node
        self.d[value] = node

    def add_right(self, target, value):
        node = BinTreeNode(value, self.d[target].depth + 1)
        self.d[target].right = node
        self.d[value] = node
    
    def distance(self, node1, node2):
        x = self.distance_from_root(node1)
        y = self.distance_from_root(node2)
        return x + y - 2 * self.distance_from_root(self.lowest_common_ancestor(node1, node2))

    def distance_from_root(self, node):
        return self.d[node].depth

    def lowest_common_ancestor(self, node1, node2):
        return self.root.lowest_common_ancestor(node1, node2)


    def pr(self):
        return self.root.pr()

class BinTreeNode():
    def __init__(self, value, depth):
        self.left = None
        self.right = None
        self.value = value
        self.depth = depth

    def pr(self):
        print self.value + str(self.depth)
        if self.left:
            print '    ',
            self.left.pr()
        if self.right:
            print '    ',
            self.right.pr()

    def lowest_common_ancestor(self, node1, node2):
        if self.value == node1:
            return self.value
        if self.value == node2:
            return self.value
        if self.left and self.right:
            x = self.left.lowest_common_ancestor(node1, node2)
            y = self.right.lowest_common_ancestor(node1, node2)
            if x and y:
                return self.value
        if self.left:
            x = self.left.lowest_common_ancestor(node1, node2)
            if x: 
                return x
        if self.right:
            y = self.right.lowest_common_ancestor(node1, node2)
            if y: 
                return y
        return




tree = BinTree('cat')
tree.add_left('cat', 'dog')
tree.add_left('dog', 'leopard')
tree.add_right('dog', 'lion')
tree.add_right('cat', 'elephant')

tree.pr()

print tree.distance('dog', 'leopard')
print tree.lowest_common_ancestor('lion', 'elephant')

def parse_tree(s):
    pass

def main():
    with open('nwck.input') as f:
        file = f.read()
