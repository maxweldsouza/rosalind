import util
import itertools
import collections

def kmer():
    d = {}
    for x in itertools.product('ACGT', repeat=4):
        tmp = ''.join(x)
        d[tmp] = 0

    arr = util.read_fasta('rosalind_kmer.txt')

    dna = arr[0]
    for i in range(len(dna) - 3):
        x = dna[i:i+4]
        d[x] += 1

    for x in itertools.product('ACGT', repeat=4):
        tmp = ''.join(x)
        print d[tmp],

kmer()
