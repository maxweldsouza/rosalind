from solutions.util import choose

def aspc(n, k):
    result = 0
    for m in range(k, n+1):
        result += choose(n, m)
    return result % 1000000

print aspc(1699, 905)
assert aspc(6, 3) == 42
