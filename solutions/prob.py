import math

def probabilities(x):
    return {
        'C': x / 2,
        'G': x / 2,
        'A': (1 - x) / 2,
        'T': (1 - x) / 2,
    }

def prob(dna, a):
    result = []
    for x in a:
        p = probabilities(x)
        common_log = 0
        for b in dna:
            common_log += math.log10(p[b])
        result.append(common_log)
    return result

def main():
    with open('rosalind_prob.txt') as f:
        lines = f.readlines()
        result = prob(lines[0].strip(), map(float, lines[1].split()))
        for x in result:
            print x,


main()