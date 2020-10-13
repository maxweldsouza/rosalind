
def complement(x):
    if x == 'C':
        return 'G'
    if x == 'G':
        return 'C'
    if x == 'A':
        return 'T'
    if x == 'T':
        return 'A'

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
