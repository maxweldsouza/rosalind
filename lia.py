import math

def lia(n, k):
    return (1 - math.pow(0.5, k)) * math.pow(0.5, n - 1)

assert lia(1, 1) == 0.5
assert lia(1, 2) == 1 - math.pow(0.5, 2)
assert lia(1, 3) == 1 - math.pow(0.5, 3)
assert lia(2, 3) == (1 - math.pow(0.5, 3)) * 0.5

print lia(2, 1)

