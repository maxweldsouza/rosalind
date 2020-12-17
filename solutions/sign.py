import itertools

def sign_iter(n):
    signs = [x for x in itertools.product([1, -1], repeat=n)]
    for x in itertools.permutations(range(1, n+1)):
        for y in signs:
            yield [i * j for i, j in zip(x, y)]

def sign(n):
    count = 0
    results = list(sign_iter(n))
    print len(results)
    for x in results:
        print ' '.join(str(i) for i in x)


sign(6)
