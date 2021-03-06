
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

monoisotopic_mass_table = {
    "A":   71.03711,
    "C":   103.00919,
    "D":   115.02694,
    "E":   129.04259,
    "F":   147.06841,
    "G":   57.02146,
    "H":   137.05891,
    "I":   113.08406,
    "K":   128.09496,
    "L":   113.08406,
    "M":   131.04049,
    "N":   114.04293,
    "P":   97.05276,
    "Q":   128.05858,
    "R":   156.10111,
    "S":   87.03203,
    "T":   101.04768,
    "V":   99.06841,
    "W":   186.07931,
    "Y":   163.06333,
}
