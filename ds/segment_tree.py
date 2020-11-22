import functools
import operator
import math

class SegmentTree(object):
    # https://www.hackerearth.com/practice/notes/segment-tree-and-lazy-propagation/
    height = 0
    def __init__(self, key=operator.add, size=32):
        self.tree = [0] * size
        self.fn = key
        self.n = size

    @staticmethod
    def left(i):
        return 2 * i + 1

    @staticmethod
    def right(i):
        return 2 * i + 2

    def position(self, i):
        return math.pow(self.height, 2) - 1

    def parent(self, i):
        return (i - 1) // 2

    def build(self, A, node, start, end):
        if start == end:
            # Leaf node will have a single element
            self.tree[node] = A[start]
        else:
            mid = (start + end) // 2
            # Recurse on the left child
            self.build(A, 2*node, start, mid)
            # Recurse on the right child
            self.build(A, 2*node+1, mid+1, end)
            # Internal node will have the sum of both of its children
            self.tree[node] = self.tree[2*node] + self.tree[2*node+1]

    def query(self, node, start, end, l, r):
        if r < start or end < l:
            # range represented by a node is completely outside the given range
            return 0
        if l <= start and end <= r:
            # range represented by a node is completely inside the given range
            return self.tree[node]
        # range represented by a node is partially inside and partially outside the given range
        mid = (start + end) // 2
        p1 = self.query(2*node, start, mid, l, r)
        p2 = self.query(2*node+1, mid+1, end, l, r)
        return p1 + p2


def test():
    t = SegmentTree()
    t.build([1, 1, 1, 1, 1, 1, 1, 1], 1, 0, 7)
    # t.update(0, 0, 3, 0, 5)
    # t.update(0, 0, 3, 2, 1)
    print (t.tree)
    print (t.query(1, 1, 8, 1, 5))
    # print (t.sum(1, 0, 7, 0, 3))
    # print (t.query(0, 2, 0, 1, 0))

test()
