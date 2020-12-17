from solutions import util


def dbru(arr):
    adj = set()

    for i, dna in enumerate(arr):
        prefix = dna[:len(dna)-1]
        suffix = dna[1:]
        adj.add(( prefix, suffix ))
        rc = util.reverse_complement(dna)
        prefix = rc[:len(rc) - 1]
        suffix = rc[1:]
        adj.add((prefix, suffix))
    return adj

def main():
    with open('rosalind_dbru.txt') as f:
        lines = f.readlines()

        for x in (dbru(line.strip() for line in lines)):
            print (f'({x[0]},{x[1]})')
main()