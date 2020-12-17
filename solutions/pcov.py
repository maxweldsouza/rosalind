def pcov(arr):
    k = len(arr[0])
    s = set()
    for x in arr:
        s.add(x)
    x = s.pop()
    result = [x]
    while len(s) > 0:
        suffix = x[1:]
        j = 0
        match = [y for y in s if y.startswith(suffix)]
        if len(match) != 1:
            raise Exception('Unexpected')

        s.remove(match[0])
        result.append(match[0])
        x = match[0]

    ans = [result[0]]
    for x in result[1:]:
        ans.append(x[len(x)-1])
    return ''.join(ans[0:len(ans) - k + 1])




def main():
    with open('rosalind_pcov.txt') as f:
        lines = f.readlines()
        lines = [x.strip() for x in lines]
        return pcov(lines)

print (main())
