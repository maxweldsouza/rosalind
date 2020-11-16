from collections import Counter
import util

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

def motz(rna):
    if rna in memo:
        return memo[rna]
    if len(rna) == 0:
        return 1
    if len(rna) == 1:
        return 1
    head = rna[0]
    tail = rna[1:]
    result = 0
    result += motz(tail)
    for i, x in enumerate(tail):
        front = tail[0:i]
        back = tail[i+1:]
        if head == complement(x):
            result += motz(front) * motz(back)
    memo[rna] = result
    return result

assert (motz('AAU') == 3)

def main():
    arr = util.read_fasta('rosalind_motz.txt')
    print (motz(arr[0]) % 1000000)

main()