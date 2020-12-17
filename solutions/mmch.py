from solutions import util
from collections import Counter

def ways(n, k):
    print n, k
    result = 1
    for i in range(n, n - k, -1):
        result *= i
    return result

assert ways(5, 2) == 5 * 4
assert ways(6, 3) == 6 * 5 * 4
assert ways(4, 3) == 4 * 3 * 2

def mmch(rna):
    d = Counter(rna)
    print d
    result = ways(max(d['C'], d['G']), min(d['C'], d['G']))
    result *= ways(max(d['U'], d['A']), min(d['U'], d['A']))
    return result

def main():
    arr = util.read_fasta('rosalind_mmch.txt')
    rna = arr[0]
    print mmch(rna)

main()

