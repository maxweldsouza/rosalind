# np hard
import util

def combine(dna1, dna2):
    for i, x in enumerate(dna2):
        pass

def dna_superstring(arr):
    result = arr[0]

    for i, dna in enumerate(arr[1:]):
        start = result[:6]
        end = result[len(result)-6:]
        print start, end
        for j, dna2 in enumerate(arr[1:]):
            if i == j:
                continue
            if dna2.index(start):
                result = combine(dna2, dna1)
            if dna2.index(end):
                result = combine(dna1, dna2)

def main():
    arr = util.read_fasta('long.txt')
    print dna_superstring(arr)