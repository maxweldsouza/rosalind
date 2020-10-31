import itertools

def choose(n, k):
    result = 1
    for i in range(n, k, -1):
        result *= i
    for i in range(1, n-k+1):
        result /= i
    return result

assert choose(1, 1) == 1
assert choose(2, 1) == 2
assert choose(6, 3) == 6 * 5 * 4 / (3 * 2 * 1)
assert choose(6, 4) == 6 * 5 / (2 * 1)
assert choose(6, 5) == 6 / 1
assert choose(6, 6) == 1

def aspc(n, k):
    result = 0
    for m in range(k, n+1):
        result += choose(n, m)
    return result % 1000000

print aspc(1699, 905)
assert aspc(6, 3) == 42
