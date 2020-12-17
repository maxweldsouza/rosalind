def main():
    with open('rosalind_trie.txt') as f:
        lines = f.readlines()
        t = Trie()
        for line in lines:
            t.add(line.strip())
        t.p()

count = 1
class Trie(object):
    def __init__(self):
        self.d = { 'C': None, 'G': None, 'A': None, 'T': None }
        global count
        self.no = count
        count += 1

    def add(self, s):
        if len(s) == 0:
            return
        c = s[0]
        if not self.d[c]:
            t = Trie()
            self.d[c] = t
        self.d[c].add(s[1:])

    def p(self):
        for k, v in self.d.items():
            if not v:
                continue
            print(f'{self.no} {v.no} {k}')
            v.p()


main()
