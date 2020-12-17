'''
n = no of months
m = life in months
'''
def fibd(n, m):
    babies = [0] * n
    adults = [0] * n

    babies[0] = 1
    for i in range(n):
        if i < n - 1:
            babies[i+1] += adults[i]
        for j in range(i+1, i+m):
            if j < n:
                adults[j] += babies[i]
    return [adults[n-1], babies[n-1]]

assert fibd(6, 3)[0] == 2
assert fibd(6, 3)[1] == 2

print sum(fibd(100, 19))




