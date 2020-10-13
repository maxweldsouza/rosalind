import util

arr = util.read_fasta('rosalind_tran.txt')

def main(dna1, dna2):
    transitions = 0
    transversions = 0
    for i, x in enumerate(dna1):
        y = dna2[i]
        if x != y:
            if x == 'G' and y == 'A':
                transitions += 1
            elif x == 'A' and y == 'G':
                transitions += 1
            elif x == 'C' and y == 'T':
                transitions += 1
            elif x == 'T' and y == 'C':
                transitions += 1
            else:
                transversions += 1
    return transitions * 1.0/transversions

print main(arr[0], arr[1])