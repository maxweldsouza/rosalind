# Remove introns and combine exons, then transcribe
codon_table = {
"UUU":"F",
"CUU":"L",
"AUU":"I",
"GUU":"V",
"UUC":"F",
"CUC":"L",
"AUC":"I",
"GUC":"V",
"UUA":"L",
"CUA":"L",
"AUA":"I",
"GUA":"V",
"UUG":"L",
"CUG":"L",
"AUG":"M",
"GUG":"V",
"UCU":"S",
"CCU":"P",
"ACU":"T",
"GCU":"A",
"UCC":"S",
"CCC":"P",
"ACC":"T",
"GCC":"A",
"UCA":"S",
"CCA":"P",
"ACA":"T",
"GCA":"A",
"UCG":"S",
"CCG":"P",
"ACG":"T",
"GCG":"A",
"UAU":"Y",
"CAU":"H",
"AAU":"N",
"GAU":"D",
"UAC":"Y",
"CAC":"H",
"AAC":"N",
"GAC":"D",
"UAA":"Stop",
"CAA":"Q",
"AAA":"K",
"GAA":"E",
"UAG":"Stop",
"CAG":"Q",
"AAG":"K",
"GAG":"E",
"UGU":"C",
"CGU":"R",
"AGU":"S",
"GGU":"G",
"UGC":"C",
"CGC":"R",
"AGC":"S",
"GGC":"G",
"UGA":"Stop",
"CGA":"R",
"AGA":"R",
"GGA":"G",
"UGG":"W",
"CGG":"R",
"AGG":"R",
"GGG":"G",
}

Start = 'AUG'

def transcribe(dna):
    return dna.replace('T', 'U')

assert transcribe('CGAT') == 'CGAU'

def remove_introns(rna, introns):
    result = rna
    for i in introns:
        result = result.replace(i, '')
    return result

assert remove_introns('ATGGTCTACATAGCTGACAAACAGCACGTAGCAATCGGTCGAATCTCGAGAGGCATATGGTCACATGATCGGTCGAGCGTGTTTCAAAGTTTGCGCCTAG', ['ATCGGTCGAA', 'ATCGGTCGAGCGTGT']) == 'ATGGTCTACATAGCTGACAAACAGCACGTAGCATCTCGAGAGGCATATGGTCACATGTTCAAAGTTTGCGCCTAG'

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

def rna_to_protein(rna):
    protein = []
    started = False
    i = 0
    while i < len(rna):
        block = rna[i:i+3]
        if block == Start:
            started = True
        if codon_table[block] == 'Stop':
            started = False
            break
        if started:
            protein.append(codon_table[block])
            i += 3
        if not started:
            i += 1
    return ''.join(protein)

assert rna_to_protein('AUGUAA') == 'M'

def splc(rna, introns):
    result = remove_introns(rna, introns)
    return rna_to_protein(transcribe(''.join(result)))

def main():
    arr = read_fasta('rosalind_splc.txt')
    return splc(arr[0], arr[1:])

print main()