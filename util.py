
def complement(x):
    if x == 'C':
        return 'G'
    if x == 'G':
        return 'C'
    if x == 'A':
        return 'T'
    if x == 'T':
        return 'A'

def reverse_complement(dna):
    ans = [complement(x) for x in dna]
    ans.reverse()
    return ''.join(ans)

def read_fasta(filename):
    strings = []
    current = []
    with open(filename) as f:   
        for line in f.readlines():
            if line.startswith('>'):
                if len(current) > 0:
                    strings.append(''.join(current))
                current = []
            else:
                current.append(line.replace('\n', ''))
    if len(current) > 0:
        strings.append(''.join(current))
    return strings

def choose(n, k):
    result = 1
    for i in range(n, k, -1):
        result *= i
    for i in range(1, n-k+1):
        result /= i
    return result

assert choose(1, 1) == 1
assert choose(2, 1) == 2
assert choose(6, 3) == 6 * 5 * 4 / (3 * 2 * 1)
assert choose(6, 4) == 6 * 5 / (2 * 1)
assert choose(6, 5) == 6 / 1
assert choose(6, 6) == 1

