import pickle
import itertools
from collections import deque

def sort():
    p = tuple(range(1, 11))
    m = { p: True }
    adj = {}

    q = deque([p])
    while len(q) > 0:
        x = q.pop()
        for i in range(len(x)):
            for j in range(i + 1, len(x)):
                r = x[:i] + tuple(reversed(x[i:j+1])) + x[j+1:]
                if r not in m:
                    m[r] = True
                    adj[r] = (x, i, j)
                    q.appendleft(r)
    return adj

def replacements(x, y):
    r = {}
    for i, j in zip(x, y):
        r[i] = j
    return r

def precompute():
    with open('sort.pickle', 'wb') as f:
        pickle.dump(sort(), f)

def main(adj):
    with open('rosalind_sort.txt') as f:
        arr = f.readlines()
        arr = [x.strip() for x in arr]
        arr = [[int(y) for y in x.split(' ')] for x in arr if x]
        arr = [tuple(x) for x in arr]

        r = replacements(arr[0], range(1, 11))
        r2 = tuple([r[x] for x in arr[1]])

        x = r2
        c = 0
        ans = []
        while x != tuple(range(1, 11)):
            x, i, j = adj[x]
            ans.append((i, j,))
            c += 1
        ans = list(reversed([(i+1, j+1) for i, j in ans]))
        print (c)
        for i, j in ans:
            print (' '.join([str(i), str(j)]))

# precompute()

with open('sort.pickle', 'rb') as f:
    adj = pickle.load(f)
    main(adj)


