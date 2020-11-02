# np hard
import util

def combine_index(dna1, dna2, i):
    return dna1[0:i] + dna2

assert combine_index('ABCDEFG', 'EFGHIJK', 4) == 'ABCDEFGHIJK'

def get_join_index(dna1, dna2):
    for i, x in enumerate(dna1):
        j = 0
        temp = i
        while True:
            if i >= len(dna1):
                # found
                return temp
            if j >= len(dna2):
                return temp
            if dna1[i] == dna2[j]:
                i += 1
                j += 1
            else:
                break
    return -1

assert get_join_index('ABCDEFGHI', 'EFGHIJ') == 4
assert get_join_index('ABCDEFGHI', 'EF') == 4
assert get_join_index('ABCD', 'CEFDGHD') == -1

def combine(dna1, dna2):
    for i, x in enumerate(dna2):
        pass

def array_to_dict(arr):
    d = {}
    for i, x in enumerate(arr):
        d[i] = arr[i]
    return d

def combine_all_strings(arr, order, indices):
    result = arr[order[0]]
    offset = 0
    for x, y in zip(order, order[1:]):
        i = indices[(x, y)] + offset
        offset = i
        result = combine_index(result, arr[y], i)
    return result

assert combine_all_strings(['ABCDEFGH', 'CDEFGHI', 'EFGHIJKLM'], [0, 1, 2], { (0, 1): 2, (1, 2): 2}) == 'ABCDEFGHIJKLM'
assert combine_all_strings(['ABCDEFGHI', 'EFGHIJK', 'GHIJKLM'], [0, 1, 2], { (0, 1): 4, (1, 2): 2}) == 'ABCDEFGHIJKLM'
assert combine_all_strings(['EFGHIJK', 'ABCDEFGHI', 'GHIJKLM'], [1, 0, 2], { (1, 0): 4, (0, 2): 2}) == 'ABCDEFGHIJKLM'
assert combine_all_strings(['ATTAGACCTG', 'CCTGCCGGAA', 'AGACCTGCCG', 'GCCGGAATAC' ], [0, 2, 1, 3], {(1, 3): 3, (0, 2): 3, (2, 1): 3}) == 'ATTAGACCTGCCGGAATAC'

def get_order(start, adj_list):
    x = start
    l = []
    while x in adj_list:
        l.append(x)
        x = adj_list[x]
    l.append(x)
    return l

assert get_order(0, { 0: 1, 1: 2, 3: 4, 2: 3 }) == [0, 1, 2, 3, 4]

def dna_superstring(arr):
    adj_list = {}
    indices = {}
    starts = [True] * len(arr)
    for x, dna1 in enumerate(arr):
        for y, dna2 in enumerate(arr):
            if x <= y:
                continue
            i = get_join_index(dna1, dna2)
            if i <= (len(dna1) / 2) and i != -1:
                adj_list[x] = y
                indices[(x, y)] = i
                starts[y] = False
            j = get_join_index(dna2, dna1)
            if j <= (len(dna2) / 2) and j != -1:
                adj_list[y] = x
                indices[(y, x)] = j
                starts[x] = False
    start = starts.index(True)

    order = get_order(start, adj_list)
    return combine_all_strings(arr, order, indices)
    

def main():
    arr = util.read_fasta('rosalind_long.txt')
    result = dna_superstring(arr)

main()