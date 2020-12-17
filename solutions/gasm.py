from solutions import util


def gasm(arr):
    k = len(arr[0])
    s = set()
    for x in arr:
        s.add(x)
        s.add(util.reverse_complement(x))
    x = s.pop()
    s.remove(util.reverse_complement(x))

    result = [x]
    while len(s) > 0:
        suffix = x[2:]

        match = [y for y in s if y.startswith(suffix)]
        if len(match) != 1:
            raise Exception('Unexpected')

        s.remove(match[0])
        s.remove(util.reverse_complement(match[0]))
        result.append(match[0])
        x = match[0]

    ans = [result[0]]
    for x in result[2:]:
        ans.append(x[len(x)-2])
    return ''.join(ans[0:len(ans) - k + 1])




def main():
    with open('gasm.txt') as f:
        lines = f.readlines()
        lines = [x.strip() for x in lines]
        return gasm(lines)

print (main())
