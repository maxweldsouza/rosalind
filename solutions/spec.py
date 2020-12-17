from solutions import util
import operator


def spec(l):
    table = [(p, w) for p, w in util.monoisotopic_mass_table.items()]

    s = sorted(l)
    ans = []
    for i in range(len(s)-1):
        d = s[i+1] - s[i]
        m, _ = min([(p, abs(w-d)) for p, w in table], key=operator.itemgetter(1))
        ans.append(m)

    return ''.join(ans)

assert spec([
3524.8542,
3710.9335,
3841.974,
3970.0326,
4057.0646
]) == 'WMQS'

def main():
    with open('rosalind_spec.txt') as f:
        arr = f.readlines()
        arr = [float(x.strip()) for x in arr]
        print (spec(arr))


main()
