import collections
import operator

x = [186.07931, 287.12699, 548.20532, 580.18077, 681.22845, 706.27446, 782.27613, 968.35544, 968.35544]
y = [101.04768, 158.06914, 202.09536, 318.09979, 419.14747, 463.17369]

def conv(x, y):
    multiset = [int((a - b) * 10000) for a in x for b in y]
    c = collections.Counter(multiset)

    pairs = [(k, v) for k, v in c.items()]
    m = max(pairs, key=operator.itemgetter(1))
    print (m[1])
    print (m[0]/ 10000)

def main():
    with open('rosalind_conv.txt') as f:
        x = list(map(float, f.readline().split(' ')))
        y = list(map(float, f.readline().split(' ')))

        conv(x, y)


main()
