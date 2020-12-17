from collections import Counter, deque, OrderedDict
import math
import itertools
import operator
import sys
sys.setrecursionlimit(6000)
import functools

M = 1e9 + 7

class BSTree(object):
    size = 0
    def __init__(self, value=None, key=lambda x: x):
        self.value = value
        self.fn = key
        self.left = None
        self.right = None

    def __iter__(self):
        if self.left is not None:
            for x in self.left:
                yield x
        if self.value is not None:
            yield self.value
        if self.right is not None:
            for x in self.right:
                yield x

    def insert(self, x):
        if self.value is None:
            self.value = x
            self.size += 1

        elif self.fn(x) < self.fn(self.value):
            if self.left is None:
                self.left = BSTree(x)
            else:
                self.left.insert(x)
        elif self.fn(x) >= self.fn(self.value):
            if self.right is None:
                self.right = BSTree(x)
            else:
                self.right.insert(x)

    def find(self, x):
        if self.fn(x) == self.fn(self.value):
            return self
        elif self.fn(x) < self.fn(self.value) and self.left is not None:
            return self.left.find(x)
        elif self.fn(x) < self.fn(self.value) and self.right is not None:
            return self.right.find(x)

    def lower_bound(self, x):
        if self.value is None:
            return None
        xval = self.fn(x)
        if xval <= self.fn(self.value) and self.left is not None:
            return self.left.lower_bound(x)
        elif xval >= self.fn(self.value) and self.right is not None and self.fn(self.right.value) <= xval:
            return self.right.lower_bound(x)
        else:
            return self

    def upper_bound(self, x):
        if self.value is None:
            return None
        xval = self.fn(x)
        if xval <= self.fn(self.value) and self.left is not None and self.fn(self.left.value) >= xval:
            return self.left.upper_bound(x)
        elif xval >= self.fn(self.value) and self.right is not None:
            return self.right.upper_bound(x)
        else:
            return self

    def delete(self, node):
        pass

    def to_array(self):
        result = ['(']
        if self.left is not None:
            for x in self.left.to_array():
                result.append(x)
        result.append(str(self.value))
        if self.right is not None:
            for x in self.right.to_array():
                result.append(x)
        result.append(')')
        return result

    def __repr__(self):
        return ' '.join(self.to_array())


def test():
    b = BSTree('b')
    b.insert('c')
    b.insert('a')
    assert b.find('b') == 0
    assert b.find('a') == 1
    assert b.find('c') == 2


def test_lower_bound():
    b = BSTree()
    assert b.lower_bound(1) is None
    b.insert(1)
    b.insert(2)
    b.insert(4)
    b.insert(5)
    l = b.lower_bound(3)
    assert l.value == 2
    l = b.lower_bound(1)
    assert l.value == 1
    l = b.lower_bound(5)
    assert l.value == 5

def test_lower_bound_2():
    b = BSTree()
    assert b.lower_bound(1) is None
    b.insert(4)
    b.insert(1)
    b.insert(5)
    b.insert(2)
    l = b.lower_bound(3)
    assert l.value == 2
    l = b.lower_bound(1)
    assert l.value == 1
    l = b.lower_bound(5)
    assert l.value == 5

test_lower_bound()
test_lower_bound_2()
