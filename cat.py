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
    print catalan
    return catalan[N]

print cat(1)
print cat(2)
print cat(3)
print cat(4)

def main():
    arr = util.read_fasta('cat.input')
    counts = Counter(arr[0])
    print cat(counts['U'] / 2) * cat(counts['C'] / 2)

main()