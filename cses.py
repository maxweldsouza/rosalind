from collections import Counter, deque, OrderedDict
import math
import itertools
import operator
import sys
sys.setrecursionlimit(10000000)
import functools

M = 1e9 + 7

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

    def __update__(self, node, start, end, idx, val):
        if start == end:
            # range represented by a node is completely outside the given range
            self.tree[node] = val
        else:
            mid = (start + end) // 2
            if start <= idx <= mid:
                self.__update__(2*node, start, mid, idx, val)
            else:
                self.__update__(2*node+1, mid+1, end, idx, val)
            self.tree[node] = self.fn(self.tree[2*node], self.tree[2*node+1])

    def query(self, l, r):
        return self.__query__(1, 1, self.n, l, r)

    def update(self, idx, value):
        return self.__update__(1, 1, self.n, idx, value)

size = 2*10**5+1

def main():
    n, q = list(map(int, input().split(' ')))
    arr = list(map(int, input().split(' ')))
    t = SegmentTree(key=min, size=size, initial=math.inf)
    t.build(arr)
    for x in range(q):
        type, i, j = list(map(int, input().split(' ')))
        if type == 1:
            t.update(i, j)
        elif type == 2:
            print (t.query(i, j))


main()



