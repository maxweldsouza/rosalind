from util import read_fasta
from collections import Counter
from math import factorial

def pmch():
    arr = read_fasta('rosalind_pmch.txt')
    rna = arr[0]

    counts = Counter(rna)
    return factorial(counts['U']) * factorial(counts['C'])

print pmch()