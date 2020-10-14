from itertools import permutations

def sign(n):
    count = 0
    numbers = range(1, n + 1)
    result = []
    for perm in permutations(numbers, n):
        count += 1
        result.append(perm)
    print list(permutations([-1, 1] * 2, 2))

    print count
    for perm in result:
        print perm

print sign(2)
