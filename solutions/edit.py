from solutions import util
import math

M = 1e9 + 7

def edit(x, y):
    cx = len(x)
    cy = len(y)
    dp = [[0 for y in range(cy + 1)] for i in range(cx + 1)]
    for i in range(1, cx + 1):
        dp[i][0] = i
    for j in range(1, cy + 1):
        dp[0][j] = j
    for i in range(1, cx + 1):
        for j in range(1, cy + 1):
            dp[i][j] = math.inf
            left = dp[i][j-1]
            top = dp[i-1][j]
            topleft = dp[i-1][j-1]
            if x[i-1] == y[j-1]:
                dp[i][j] = topleft
            else:
                dp[i][j] = min(left, top, topleft) + 1

    return dp[cx][cy]

assert edit('A', 'B') == 1
assert edit('A', 'A') == 0
assert edit('AB', 'AC') == 1
assert edit('AB', 'A') == 1
assert edit('BA', 'A') == 1
assert edit('ABC', 'DEF') == 3
assert edit('ABC', 'F') == 3
assert edit('TWXFUABGBNLTBFNSUVQW', 'GPNJILFXJUIZPLTVUIB') == 19
assert edit('L', 'LLLLLLL') == 6

def main():
    arr = util.read_fasta('rosalind_edit.txt')
    print (edit(arr[0], arr[1]))

main()
