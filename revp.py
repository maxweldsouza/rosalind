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
    length = 0
    pos = -1
    while True:
        if j < 0 or k >= len(input):
            break
        if input[j] != complement(input[k]):
            break
        else:
            # print length, pos
            length += 2
            pos = j
        j -= 1
        k += 1
    if 4 <= length <= 12:
        return (pos + 1, length)
    return


def odd_palindrome(input, center):
    j = center - 1
    k = center + 1
    length = 1
    pos = center
    while True:
        if j < 0 or k >= len(input):
            break
        if input[j] != complement(input[k]):
            break
        else:
            # print length, pos
            length += 2
            pos = j
        j -= 1
        k += 1
    if 4 <= length <= 12:
        return (pos + 1, length)
    return

def revp(input):
    results = []

    for i, x in enumerate(input):
        even = even_palindrome(input, i)
        odd = odd_palindrome(input, i)
        if even:
            results.append(even)
        if odd:
            results.append(odd)
    return results
        
print revp('CGACG')

input = 'TCAATGCATGCGGGTCTATATGCAT'

print revp(input)