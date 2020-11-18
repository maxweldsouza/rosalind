import itertools
from collections import deque

def rear():
    p = tuple(range(1, 11))
    m = { p: 0 }

    q = deque([p])
    while len(q) > 0:
        x = q.pop()
        for i in range(len(x)):
            for j in range(i + 1, len(x)):
                r = x[:i] + tuple(reversed(x[i:j+1])) + x[j+1:]
                if r not in m:
                    m[r] = m[x] + 1
                    q.appendleft(r)
    return m

def replacements(x, y):
    r = {}
    for i, j in zip(x, y):
        r[i] = j
    return r


def main():
    with open('rosalind_rear.txt') as f:
        arr = f.readlines()
        arr = [x.strip() for x in arr]
        arr = [[int(y) for y in x.split(' ')] for x in arr if x]
        arr = [tuple(x) for x in arr]

        m = rear()

        result = []
        for i in range(0, len(arr), 2):
            r = replacements(arr[i], range(1, 11))
            r2 = tuple([r[x] for x in arr[i+1]])
            result.append(str(abs(m[tuple(range(1, 11))] - m[r2])))
        print (' '.join(result))

main()


