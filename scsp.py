import util
from collections import deque

def backtrack(dp, x, y, i, j):
    result = deque()
    while True:
        if i == 0:
            break
        if j == 0:
            break
        if x[i-1] == y[j-1]:
            result.appendleft(x[i-1])
            i = i-1
            j = j-1
        elif dp[i-1][j] > dp[i][j-1]:
            i = i - 1
        else:
            j = j - 1
    return ''.join(result)

def lcsq(x, y):
    cx = len(x)
    cy = len(y)
    dp = [[0 for y in range(cy + 1)] for i in range(cx + 1)]
    dp[0][0] = 0
    for i in range(1, cx + 1):
        for j in range(1, cy + 1):
            left = dp[i][j-1]
            top = dp[i-1][j]
            if x[i-1] == y[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(left, top)

    return backtrack(dp, x, y, cx, cy)

def scsp(x, y):
    x, y = list(x), list(y)
    l = list(lcsq(x, y))
    result = []
    while True:
        if len(x) == 0 and len(y) == 0 and len(l) == 0:
            break
        elif len(l) == 0:
            for i in x:
                result.append(i)
            x = []
            for j in y:
                result.append(j)
            y = []
        elif l[0] == x[0] == y[0]:
            result.append(l[0])
            x = x[1:]
            y = y[1:]
            l = l[1:]
        elif len(x) > 0 and x[0] != l[0]:
            result.append(x[0])
            x = x[1:]
        elif len(y) > 0 and y[0] != l[0]:
            result.append(y[0])
            y = y[1:]
    return ''.join(result)

assert scsp('AEB', 'CED') == 'ACEBD'
assert scsp('AB', 'AC') == 'ABC'
assert scsp('A', 'A') == 'A'
assert scsp('ABC', 'AC') == 'ABC'
assert scsp('ABE', 'CDE') == 'ABCDE'
assert scsp('IA', 'BCDEFGHA') == 'IBCDEFGHA'

def main():
    with open('rosalind_scsp.txt') as f:
        lines = f.readlines()
        lines = [list(x.strip()) for x in lines]
        print (scsp(lines[0], lines[1]))

main()