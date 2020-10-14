import util
# Manacher's algorithm

def complement(x):
    if x == 'C':
        return 'G'
    if x == 'G':
        return 'C'
    if x == 'A':
        return 'T'
    if x == 'T':
        return 'A'

def even_palindrome(input, center):
    j = center
    k = center + 1
    results = []
    pos = -1
    length = 0
    while True:
        if j < 0 or k >= len(input):
            break
        if input[j] != complement(input[k]):
            break
        else:
            # print length, pos
            length += 2
            pos = j
            if 4 <= length <= 12:
                results.append((pos, length))
        j -= 1
        k += 1
    return results

# assert even_palindrome('TA', 0) == (0, 2)
# assert even_palindrome('TTAG', 1) == (1, 2)
# assert even_palindrome('TTAA', 1) == (0, 4)
# assert even_palindrome('ATTAAT', 2) == (0, 6)
# assert even_palindrome('CATTAATT', 3) == (1, 6)

def odd_palindrome(input, center):
    j = center - 1
    k = center + 1
    length = 1
    pos = center
    results = []
    while True:
        if j < 0 or k >= len(input):
            break
        if input[j] != complement(input[k]):
            break
        else:
            # print length, pos
            length += 2
            pos = j
            if 4 <= length <= 12:
                results.append((pos, length))
        j -= 1
        k += 1
    return results

# assert odd_palindrome('T', 0) == (0, 1)
# print odd_palindrome('TTA', 1)
# assert odd_palindrome('TTA', 1) == (0, 3)
# assert odd_palindrome('CTTAG', 2) == (0, 5)
# assert odd_palindrome('TTTAG', 2) == (1, 3)
# assert odd_palindrome('ATTATTG', 2) == (0, 5)
# assert odd_palindrome('CATTATT', 3) == (1, 5)

def revp(input):
    results = []

    for i, x in enumerate(input):
        even = even_palindrome(input, i)
        # odd = odd_palindrome(input, i)
        if even:
            results += even
        # if odd:
        #     results += odd
    for pos, length in results:
        print pos + 1, length
        

input = 'TCAATGCATGCGGGTCTATATGCAT'

arr = util.read_fasta('rosalind_revp.txt')

print arr[0]
revp(arr[0])