import unittest
from sets import Set

def main():
    pass

alphabet = Set(['C', 'G', 'A', 'T'])

class SuffixTreeNode:
    def __init__(self):
        self.branches = {
            'C': None,
            'G': None,
            'A': None,
            'T': None
        }
        self.string = None
        self.startIndex = None
        self.stringNumber = None

    def insert(self, s):
        pass

    def insert_suffix(self, s):
        if len(s) == 0:
            return
        first = s[0]
        if first not in alphabet:
            raise 'Suffix contains characters not in alphabet'

        if not self.branches[first]:
            self.branches[first] = SuffixTreeNode()
            self.branches[first].string = s + '$'
        else:
            if len(s) > 1:
            
            else:




class TestStringMethods(unittest.TestCase):
    def test_create(self):
        st = SuffixTreeNode()
        self.assertEqual(st.branches['A'], None)

    def test_insert_suffix(self):
        st = SuffixTreeNode()
        st.insert_suffix('G')
        self.assertEqual(st.branches['G'].string, 'G$')

    def test_insert_multiple_suffixes(self):
        st = SuffixTreeNode()
        st.insert_suffix('G')
        self.assertEqual(st.branches['G'].string, 'G$')
        st.insert_suffix('AG')
        self.assertEqual(st.branches['A'].branches['G'].string, 'G$')

if __name__ == '__main__':
    unittest.main()
