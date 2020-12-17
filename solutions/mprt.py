import requests
import re

def get(id):
    r = requests.get('http://www.uniprot.org/uniprot/' + id + '.fasta')
    return  r.text

def get_dna(data):
    arr = data.split('\n')
    return ''.join(arr[1:])

def hasNGlycosylation(dna):
    result = re.finditer(r'(?=(N[^P][S|T][^P]))', dna)
    return [x.start() + 1 for x in result]


test_input = '''
A2Z669
B5ZC00
P07204_TRBM_HUMAN
P20840_SAG1_YEAST
'''

input = '''
P46096_SYT1_MOUSE
P00744_PRTZ_BOVIN
P01044_KNH1_BOVIN
Q8R1Y2
A9QYR8
P02760_HC_HUMAN
P02749_APOH_HUMAN
P00743_FA10_BOVIN
P00304_ARA3_AMBEL
A5WBR3
B4S2L7
Q7S432
P00749_UROK_HUMAN
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