from collections import Counter, deque, OrderedDict
import math
import itertools
import sys

M = 1e9 + 7

n, x = list(map(int, input().split(' ')))
h = list(map(int, input().split(' ')))
s = list(map(int, input().split(' ')))

# 1 2 10 6 5 1 7 4 10 4
# 6 3  8 1 7 3 8 6  5 6

print (n, x)
print (h)
print (s)

dp = [0] * (n + 1)
dp[0] = 0
total = [0] * (n + 1)
for i in range(1, n+1):
    if dp[i-1] < dp[i-1] + s[i-1] and total[i-1] + h[i-1] <= x:
        dp[i] = dp[i-1] + s[i-1]
        total[i] = total[i-1] + h[i-1]
    else:
        dp[i] = dp[i-1]
        total[i] = total[i-1]

print (dp)
print (total)
print (dp[n])
