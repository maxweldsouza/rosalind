from collections import Counter, deque, OrderedDict
import math
import itertools
import operator
import sys
sys.setrecursionlimit(6000)
import functools

M = 1e9 + 7

class BSTree(object):
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

def test():
    b = BSTree('b')
    b.insert('c')
    b.insert('a')
    assert b.find('b') == 0
    assert b.find('a') == 1
    assert b.find('c') == 2


def rest(arr):
    temp = BSTree(key=operator.itemgetter(0))
    for a, b in arr:
        temp.insert((a, 1))
        temp.insert((b, -1))
    ans = 0
    c = 0
    for _, x in temp:
        c += x
        ans = max(ans, c)
    return ans

assert rest([ [1, 20], [2, 19], [3, 18], [4, 17], [5, 16], [6, 15], [7, 14], [8, 13], [9, 12], [10, 11] ]) == 10
assert rest([[5, 8], [2, 4], [3, 9]]) == 2

def main():
    n = int(input())
    arr = []
    for i in range(n):
        a, b = map(int, input().split(' '))
        arr.append((a, b,))
    print (rest(arr))

main()



