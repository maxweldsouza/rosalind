from solutions import util


def dist(a, b):
    count = 0
    for x, y in zip(a, b):
        if x != y:
            count += 1
    return float(count) / len(a)


def pdst():
    arr = util.read_fasta('rosalind_pdst.txt')
    n = len(arr)
    result = [[dist(x, y) for x in arr] for y in arr]
    for row in result:
        print ' '.join(map(str, row))

pdst()
