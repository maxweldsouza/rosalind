import util

def lcsq(x, y):
    dp = [[0 for j in y] for i in x]
    dp[0][0] = x[0] == y[0]
    result = ''
    for i, a in enumerate(x):
        for j, b in enumerate(y):
            left = dp[i][j-1] if j > 0 else 0
            top = dp[i-1][j] if i > 0 else 0
            res = max(left, top)
            if a == b:
                dp[i][j] = res + 1
                result += a
                break
            else:
                dp[i][j] = res

    return result


def main():
    arr = util.read_fasta('lcsq.txt')
    print (lcsq(arr[0], arr[1]))

main()
