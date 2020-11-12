import util

def failure_arr(s):
    pass

# assert failure_arr('ABCDE') == [0, 0, 0, 0, 0]
# assert failure_arr('CCCCC') == [0, 1, 2, 3, 4]
print failure_arr('CAGCATGGTATCACAGCAGAG') 
print [ 0, 0, 0, 1, 2, 0, 0, 0, 0, 0, 0, 1, 2, 1, 2, 3, 4, 5, 3, 0, 0]


def main():
    arr = util.read_fasta('rosalind_kmp.txt')
    return failure_arr(arr[0])

# print main()