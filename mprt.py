import requests
import re

def get(id):
    r = requests.get('http://www.uniprot.org/uniprot/' + id + '.fasta')
    return  r.text

def get_dna(data):
    arr = data.split('\n')
    return ''.join(arr[1:])

def hasNGlycosylation(dna):
    result = re.finditer(r'N[^P][S|T][^P]', dna)
    return [x.start() + 1 for x in result]


test_input = '''
A2Z669
B5ZC00
P07204_TRBM_HUMAN
P20840_SAG1_YEAST
'''

input = '''
P0C5G9
Q706D1
P10153_RNKD_HUMAN
P01233_CGHB_HUMAN
P08198_CSG_HALHA
Q8CE94
P10761_ZP3_MOUSE
P07925
P02749_APOH_HUMAN
Q2YCH6
Q6GEK4
A8G1M9
'''

def main():
    ids = input.strip().split('\n')

    for id in ids:
        dna = get_dna(get(id))
        results = hasNGlycosylation(dna)
        if results:
            print id
            print ' '.join((str(x) for x in results))
    
main()