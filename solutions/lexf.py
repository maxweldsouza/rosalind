from itertools import product

def lexf(symbols, n):
    for x in product(symbols, repeat=n):
        print ''.join(x)

lexf('ABCDEFGH', 3)
