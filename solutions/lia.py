import math
import itertools
from collections import Counter

def merge(arr):
    return [x + y for x, y in arr]

def mate(x, y):
    zygote1 = merge(itertools.product(x[0:2], x[2:4]))
    zygote2 = merge(itertools.product(y[0:2], y[2:4]))
    return list(''.join(sorted(i + j)) for i, j in itertools.product(zygote1, zygote2))

print mate('AaBb', 'AaBb')
print mate('AABb', 'AaBb')

def main():
    result = []
    gen1 = mate('AaBb', 'AaBb')
    prob = 0
    c = Counter(gen1)
    for x in gen1:
        temp = c[x] / 16.0
        gen2 = mate(x, 'AaBb')
        c2 = Counter(gen2)
        print gen2
        for y in gen2:
            if y == 'ABab':
                prob += temp * 1 / 16.0
    
    return prob

print main()