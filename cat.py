from collections import Counter
import util

def cat(N):
    if N == 0:
        return 1
    if N == 1:
        return 1
    catalan = [None] * (N+1)
    catalan[0] = 1
    catalan[1] = 1
    for n in range(2, N+1):
        cn = 0
        for k in range(1, n+1):
            cn += catalan[k - 1] * catalan[n - k]
        catalan[n] = cn
    return catalan[N]

def main():
    arr = util.read_fasta('rosalind_cat.txt')
    counts = Counter(arr[0])
    count_u = (counts['U'] + counts['A']) / 2
    count_c = (counts['C'] + counts['G']) / 2
    print count_c
    print count_u

    print (cat(count_c) * cat(count_u)) % 1000000

main()