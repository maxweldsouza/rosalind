codon_table = {
"UUU":"F",
"CUU":"L",
"AUU":"I",
"GUU":"V",
"UUC":"F",
"CUC":"L",
"AUC":"I",
"GUC":"V",
"UUA":"L",
"CUA":"L",
"AUA":"I",
"GUA":"V",
"UUG":"L",
"CUG":"L",
"AUG":"M",
"GUG":"V",
"UCU":"S",
"CCU":"P",
"ACU":"T",
"GCU":"A",
"UCC":"S",
"CCC":"P",
"ACC":"T",
"GCC":"A",
"UCA":"S",
"CCA":"P",
"ACA":"T",
"GCA":"A",
"UCG":"S",
"CCG":"P",
"ACG":"T",
"GCG":"A",
"UAU":"Y",
"CAU":"H",
"AAU":"N",
"GAU":"D",
"UAC":"Y",
"CAC":"H",
"AAC":"N",
"GAC":"D",
"UAA":"Stop",
"CAA":"Q",
"AAA":"K",
"GAA":"E",
"UAG":"Stop",
"CAG":"Q",
"AAG":"K",
"GAG":"E",
"UGU":"C",
"CGU":"R",
"AGU":"S",
"GGU":"G",
"UGC":"C",
"CGC":"R",
"AGC":"S",
"GGC":"G",
"UGA":"Stop",
"CGA":"R",
"AGA":"R",
"GGA":"G",
"UGG":"W",
"CGG":"R",
"AGG":"R",
"GGG":"G",
}

reverse_table = {
}

for key, value in codon_table.items():
    if value not in reverse_table:
        reverse_table[value] = 0

    reverse_table[value] += 1


print reverse_table
input = 'MYHAGYAPIEWVDVIACTSEARCEVWEADLSWTWWTVAHLITWFMLLSPLRQSRHELSNWDGSWQDVFVDRSLIEPTHIWFGYVHMPLSHHFFTAVIGFSMQVSWVAEDNQRLQIEPVETINAYNACWEMWAIDDMQRKLHAISDCTHIDNKDVWKYMKPKWMSGLRITTTGIATANSTHKPLCEAAITGRYFELLKCGCATEKNMPHVKSPCEQGKMYYIILEQAPFTCEIKRLLNPIICICRHHEDSHKHNVGTVRETTETIPYRNGMHRFTPDWMKAPHCGRAFRWRENTGNAHHHLATIQPHDGCYSDWISTIQWADHEWENVSCMVWAKFYADFPNDPGKWSMFKSIVVFANIDAINAWEKLCNQSWNGNNPEKNHFYVQTEEGRDRKYTMQMWYVLDYDTAPVYCVTKKVCWKAFIHCFQFHGCDNNTFVSDMVISCTEAVELGYHPDFYRSNWFDKVYINWGPNAFMHFGDQEASPQQYMAPCAQPVISEWWKVNKGGKISEKKEFWGKNSHPCTPPLGYAHDIEFLDPDLSIVIWISFHNYTEWMYHEIMGCMVMTWGSAYHIVDHSHQMYMWACIKSPWDRCTAGIMPLRICVPEVGDPYRNVLLNKYELKYRWTCCVWVVKYVDYWADCWYHGYFQARLWHKHIWSALWWLCTPSHYEELSYFQKVRVDLPACCPRTGQHKHMPRNMCPINQHQLNMFAPTEEMLTALTWVWWANLFRMMICDLCTIVQDELRVCFQMFRGWPSKSCPWFPVYHKHEALMRWPRQRPIRQPCFWLAGKDFRHLEACHLQWMNCSIWVWRDYWMWQGTRGHIHKDWETHNLAHEGNRESIMDIGLMQKDHYWLHFIYQFMTTASYACVEAVIWPFSSVQECEIQPQIPSFYKIWCCIGMHMEDNWAEFSIELQPYASRYNDGGEITVDDHPEYWTNDACKLPSFSCTENAFDEQNMEGCEFCSICHDCCSIHGNRQCFYCFLEQMSQQAGIHHGCFTP'

def reverse_transcription_ways(input):
    result = 1
    for x in input:
        result = (result * reverse_table[x]) % 1000000

    result = (result * reverse_table['Stop']) % 1000000
    return result

print reverse_transcription_ways(input)