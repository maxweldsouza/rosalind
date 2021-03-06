from solutions import util
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

assert lcsq('BAC', 'A') == 'A'
assert lcsq('A', 'A') == 'A'
assert lcsq('B', 'A') == ''
assert lcsq('AB', 'AB') == 'AB'
assert lcsq('CAB', 'AB') == 'AB'
assert lcsq('CABD', 'EABF') == 'AB'
assert lcsq('CAGBD', 'EAHBF') == 'AB'

def verify(s, ans):
    a = [x for x in reversed(ans)]
    for x in s:
        if len(a) == 0:
            continue
        if a[-1] == x:
            a.pop()

    assert len(a) == 0

def main():
    arr = util.read_fasta('rosalind_lcsq.txt')
    result = lcsq(arr[0], arr[1])
    verify(arr[0], result)
    verify(arr[1], result)
    print (result)

main()
