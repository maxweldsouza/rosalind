from solutions import util
import itertools

def get_min_length(arr):
    return min(len(x) for x in arr)

assert get_min_length(['de', 'a', 'abc']) == 1
assert get_min_length(['', 'a', 'abc']) == 0
assert get_min_length(['abc', 'adef', 'abc']) == 3

def string_of_length(n):
    return (''.join(x) for x in itertools.product('CGAT', repeat=n))

def generate_strings(prefixes):
    for prefix in prefixes:
        for x in 'CGAT':
            yield prefix + x

assert list(generate_strings(['CG'])) == ['CGC', 'CGG', 'CGA', 'CGT']

def lcsm(arr):
    min_length = get_min_length(arr)

    result = ''
    prefixes = ['C', 'G', 'A', 'T']
    while True:
        new_prefixes = []
        for s in generate_strings(prefixes):
            isLcs = all(s in x for x in arr)
            if isLcs:
                result = s
                new_prefixes.append(s)
        prefixes = new_prefixes
        if len(prefixes) == 0:
            return result
    return result

def main():
    arr = util.read_fasta('rosalind_lcsm.txt')
    return lcsm(arr)

print main()
