import util

def hamming_distance(a, b):
    ans = 0
    for x, y in zip(a, b):
        if not x == y:
            ans += 1
    return ans

def corr(arr):
    m = {}
    for x in arr:
        if not x in m:
            m[x] = 1
        else:
            m[x] += 1
        r = util.reverse_complement(x)
        if not r in m:
            m[r] = 1
        else:
            m[r] += 1

    og = {k: v for k, v in m.items() if v >= 2}

    done = {}
    for k, v in m.items():
        if k not in og:
            match = None
            for x, _ in og.items():
                if hamming_distance(x, k) < 2:
                    match = x
            if match and not k in done and not util.reverse_complement(k) in done:
                done[k] = True
                print (k, '->', match)

def main():
    arr = util.read_fasta('rosalind_corr.txt')
    corr(arr)

main()