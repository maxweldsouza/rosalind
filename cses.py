from collections import Counter, deque, OrderedDict
import math
import itertools
import operator
import sys
sys.setrecursionlimit(6000)
import functools

M = 1e9 + 7

def range_sum(arr, queries):
    s = [0] * len(arr)
    c = 0
    for i, x in enumerate(arr):
        c += x
        s[i] = c
    for a, b in queries:
        if a == 1:
            print (s[b-1])
        else:
            print (s[b-1] - s[a-2])

def main():
    n, q = map(int, input().split(' '))
    x = list(map(int, input().split(' ')))
    queries = []
    for i in range(q):
        query = tuple(map(int, input().split(' ')))
        queries.append(query)

    range_sum(x, queries)

main()



