def main():
    with open('rosalind_seto.txt') as f:
        n = int(f.readline())
        a = eval(f.readline())
        b = eval(f.readline())

        seto(n, a, b)

def print_set(a):
    print '{', 
    print ', '.join(map(str, a)),
    print '}'

def seto(n, a, b):
    u = set(range(1, n+1))
    print_set(a.union(b))
    print_set(a.intersection(b))
    print_set(a.difference(b))
    print_set(b.difference(a))
    print_set(u.difference(a))
    print_set(u.difference(b))

main()