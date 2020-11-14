from collections import Counter, deque, OrderedDict
import math
import itertools
import sys

M = 1e9 + 7

n, x = map(int, input().split(' '))
c = list(map(int, input().split(' ')))

dp = [0] * (x + 1)
dp[0] = 1
for i in range(1, x + 1):
    for coin in c:
        if i - coin >= 0:
            dp[i] += dp[i - coin]
            dp[i] = dp[i] % M

print(int(dp[x]))

