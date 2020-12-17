from solutions import util


def complement(x):
    if x == 'C':
        return 'G'
    if x == 'G':
        return 'C'
    if x == 'A':
        return 'U'
    if x == 'U':
        return 'A'

memo = {}

def catalan(rna):
    if rna in memo:
        return memo[rna]

    if len(rna) == 0:
        return 1
    if len(rna) == 1:
        raise 'Unexpected'
    if len(rna) == 2:
        return 1
    counts = { 'C': 0, 'G': 0, 'A': 0, 'U': 0 }
    head = rna[0]
    counts[head] = 1
    tail = rna[1:]
    # print head, tail
    result = 0
    for i, x in enumerate(tail):
        # print i, x
        counts[x] += 1
        front = tail[0:i]
        back = tail[i+1:]
        if counts['C'] == counts['G'] and counts['A'] == counts['U'] and head == complement(x):
            result += catalan(front) * catalan(back)
    # print rna, result
    memo[rna] = result
    return result
    
# print catalan('CCCGGG')
assert catalan('AUAU') == 2
assert catalan('UAGCGUGAUCAC') == 2
assert catalan('CAUAUGAUAU') == 4

def main():
    arr = util.read_fasta('rosalind_cat2.txt')
    print catalan(arr[0]) % 1000000

main()