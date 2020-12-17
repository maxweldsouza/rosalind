from solutions import util


def failure_arr(s):
    b = [-1] * len(s)
    for i, x in enumerate(s):
        j = i - 1
        while j >= 0:
            if s[b[j] + 1] == s[i]:
                b[i] = b[j] + 1
                break
            else:
                j = b[j]
    return [x + 1 for x in b]


assert failure_arr('ABCDE') == [0, 0, 0, 0, 0]
assert failure_arr('CCCCC') == [0, 1, 2, 3, 4]
assert (failure_arr('CAGCATGGTATCACAGCAGAG')) == [ 0, 0, 0, 1, 2, 0, 0, 0, 0, 0, 0, 1, 2, 1, 2, 3, 4, 5, 3, 0, 0]


def main():
    arr = util.read_fasta('rosalind_kmp.txt')
    return ' '.join(str(x) for x in failure_arr(arr[0]))

print (main())