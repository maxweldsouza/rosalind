from itertools import permutations

def pper(n, k):
    result = 1
    for x in range(n-k+1, n+1):
        result = (result * x) % 1000000
    return result

print pper(90, 10)