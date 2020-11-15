import itertools

def lexv(arr, n):
    res = []
    l = len(arr)

    for i in range(n):
        for y in itertools.product(range(l), repeat=i+1):
            res.append(y)

    res = sorted(res)
    for x in res:
        print (''.join(arr[y] for y in x))

arr = list(map(str, input().split(' ')))
n = int(input())
lexv(arr, n)