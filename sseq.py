import util

arr = util.read_fasta('rosalind_sseq.txt')

def sseq(dna, seq):
    i = 0
    result = []
    for j, x in enumerate(dna):
        if i < len(seq) and x == seq[i]:
            result.append(j + 1)
            i += 1
    return result

for x in  sseq(arr[0], arr[1]):
    print x, 
        
        
