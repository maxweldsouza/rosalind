import re

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

    def add_left(self, target, value):
        node = BinTreeNode(value, self.depth + 1)
        self.left = node

    def add_right(self, target, value):
        node = BinTreeNode(value, self.depth + 1)
        self.right = node
    
    def distance(self, node1, node2):
        x = self.search(node1).depth
        y = self.search(node2).depth
        return x + y - 2 * self.search(self.lowest_common_ancestor(node1, node2)).depth

    def search(self, value):
        if self.value == value:
            return self
        if self.left:
            left_value = self.left.search(value)
            if left_value:
                return left_value
        if self.right:
            right_value = self.right.search(value)
            if right_value:
                return right_value
        

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




tree = BinTreeNode('cat', 0)
tree.add_left('cat', 'dog')
tree.add_left('dog', 'leopard')
tree.add_right('dog', 'lion')
tree.add_right('cat', 'elephant')

# tree.pr()

# print tree.distance('dog', 'leopard')
# print tree.lowest_common_ancestor('lion', 'elephant')

def tokenize(s):
    result = []
    i = 0
    while i < len(s):
        m = re.match(r'^[a-z]+', s[i:])
        x = s[i]
        if x == '(':
            result.append(x)
            i += 1
        elif x == ')':
            result.append(x)
            i += 1
        elif x == ',':
            result.append(x)
            i += 1
        elif x == ';':
            result.append(x)
            i += 1
        elif m:
            (start, end) = m.span()
            result.append(s[i:i+end])
            i = i + end
    return result

assert tokenize('(cat)dog;') == ['(', 'cat', ')', 'dog', ';']
assert tokenize('(cat,mouse)dog;') == ['(', 'cat', ',', 'mouse', ')', 'dog', ';']

def parse_tree(tokens, root):
    i = 0
    while i < len(tokens):
        t = tokens[i]
        if t == '(':
            j = i
            while j < len(tokens) and tokens[j] != ')':
                j += 1
            internal = BinTreeNode('internal', root.depth+1)
            parse_tree(tokens[i+1:j], internal)
            if not root.left:
                root.left = internal
            elif not root.right:
                root.right = internal
            i = j
        elif t == ')':
            i += 1
        elif t == ',':
            i += 1
        elif t == ';':
            i += 1
        else:
            print t, root.value
            if not root.left:
                root.left = BinTreeNode(t, root.depth+1)
            elif not root.right:
                root.right = BinTreeNode(t, root.depth+1)
            i += 1
    return root
    
# x = parse_tree(tokenize('(cat,mouse);'), BinTreeNode('root', 0))
x = parse_tree(tokenize('(cat,mouse)dog;'), BinTreeNode('root', 0))
x.pr()

    
def main():
    with open('nwck.input') as f:
        x = f.read()
        arr = x.split('\n')
        arr = [x for x in arr if x]
        result = []
        i = 0
        while i < len(arr):
            tree = parse_tree(tokenize(arr[i]), BinTreeNode('root', 0))
            x, y = arr[i+1].split(' ')
            print x, y
            dist = tree.distance(x, y)
            print dist
            result.append(dist)
        
        for x in result:
            print result

main()

    

