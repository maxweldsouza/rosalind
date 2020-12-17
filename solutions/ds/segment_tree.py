import functools
import operator
import math

class SegmentTree(object):
    # https://www.hackerearth.com/practice/notes/segment-tree-and-lazy-propagation/
    def __init__(self, key=operator.add, initial=0, size=32):
        self.tree = [initial] * 4 * size
        self.fn = key
        self.n = size
        self.initial = initial

    def __build__(self, A, node, start, end):
        if start == end:
            # Leaf node will have a single element
            if node < 0 or node >= len(self.tree):
                print (node)
            self.tree[node] = A[start]
        else:
            mid = (start + end) // 2
            # Recurse on the left child
            self.__build__(A, 2*node, start, mid)
            # Recurse on the right child
            self.__build__(A, 2*node+1, mid+1, end)
            # Internal node will have the sum of both of its children
            self.tree[node] = self.fn(self.tree[2*node], self.tree[2*node+1])

    def build(self, A):
        self.n = len(A)
        self.__build__(A, 1, 0, self.n-1)

    def __query__(self, node, start, end, l, r):
        if r < start or end < l:
            # range represented by a node is completely outside the given range
            return self.initial
        if l <= start and end <= r:
            # range represented by a node is completely inside the given range
            return self.tree[node]
        # range represented by a node is partially inside and partially outside the given range
        mid = (start + end) // 2
        p1 = self.__query__(2*node, start, mid, l, r)
        p2 = self.__query__(2*node+1, mid+1, end, l, r)
        return self.fn(p1, p2)

    def query(self, l, r):
        return self.__query__(1, 1, self.n, l, r)


def test():
    t = SegmentTree()
    t.build([1, 1, 1, 1, 1, 1, 1, 1])
    # t.update(0, 0, 3, 0, 5)
    # t.update(0, 0, 3, 2, 1)
    print (t.tree)
    print (t.query(1, 8))
    # print (t.sum(1, 0, 7, 0, 3))
    # print (t.query(0, 2, 0, 1, 0))

def test_large():
    t = SegmentTree(size=200001)
    a = [1] * 200000
    t.build(a)
    print (t.query(1, len(a)))

test_large()
# test()
