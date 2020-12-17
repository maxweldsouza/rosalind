
package main

import (
	"fmt"
	"strings"
)


func dnaToRna(dna string) string {
	return strings.Replace(dna, "T", "U", -1)
}

func rnaToProtein(rna string) []string {
	codonTable := map[string]string{
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
	protein := ""
	reading := false
	result := make([]string, 0)

	for orf := 0; orf < 3; orf++ {
		protein = ""
		reading = false
		for i := orf; i + 2 < len(rna); i = i + 3 {
			codon := rna[i:i+3]
			aminoAcid := codonTable[codon]
			if codon == "AUG" {
				reading = true
			}
			if aminoAcid == "Stop" {
				reading = false
				result = append(result, protein)
				protein = ""
			}
			if (reading) {
				protein = protein + aminoAcid
			}
		}
	}
	return result
}

func Reverse(s string) (result string) {
	for _,v := range s {
	  result = string(v) + result
	}
	return 
}

func complement(dna string) string {
	result := ""
	c := map[string]string{
		"C": "G",
		"G": "C",
		"A": "T",
		"T": "A",
	}
	for i := 0; i < len(dna); i++ {
		result = result + c[string(dna[i])]
	}
	return result
}

func reverseComplement (dna string) string {
	return Reverse(complement(dna))
}

func candidateProteins (dna string) []string {
	rna := dnaToRna(dna)
	protein := rnaToProtein(rna)
	return protein
}

func allCandiateProteins (dna string) []string {
	return append(candidateProteins(dna), candidateProteins(reverseComplement(dna))...)
}

func unique(elems []string) []string{
	seen := map[string]bool{}
	result := []string{}
	for x := range elems {
		if seen[elems[x]] {

		} else {
			seen[elems[x]] = true
			result = append(result, elems[x])
		}
	}
	return result
}

func subProteins(protein string) []string {
	result := []string{}
	for i := 0; i < len(protein); i++ {
		if (protein[i] == 'M') {
			result = append(result, protein[i:len(protein)])
		}
	}
	return result
}

func getAllSubProteins(proteins []string) []string {
	result := []string{}
	for _, x := range proteins {
		result = append(result, subProteins(x)...)
	}
	return result
}

func main () {
	dna := "GCTTCCCGAGTCATTGCAAGAAAAGTAATTGCAGCGAGGCAAGTAGTAAAGTGTTTCCTAGGCGCAACTGTGACAAATCGTAGATCTTGATTATTGGGGGCACGAGAGGAGGCTGGCGCGCCGGCCTAGTATCAGACAGTATTTCCGCCTCTGTGGGGTTTACGAAACTGAGTACACAGATCTACGACAGTCGAGGAAATGTCACGGGTGGTCGTCATATGCTCTCGGATTTTCATATGCAAGCTGTGGTGACTTCCATCGTCAACAGTCTGTAGTAGTGACGGTTCGAAAACCAAGCTACATGGAACATGCGCGTGCGGCTTAACTGCATCCACCGGTAACCGGACCACTCCAACGGTCCATGAACCTTAGAATAGCCTGATAAAACGGACTTCAAGGCGTATATAACACTTGATGCTAAACCCCTGCGACCGGTGAGCATAGCTATGCTCACCGGTCGCAGGGGTTTAGCATGACACATGCAGCTATTGGCGATGCCGGGACGTTTACGATCCATAAATAACGTAACTCTGGACCAGATATTGAATTTGATGCTAACGCTGTCTCTCAAAAGTCGATCTCAGTATTTGTGTACCCCAGCTGGTAATGAGCTATTGTAAGGCTGACGTTGTCCGCTAGGTCTCGGGTCCCGATCACTTCGGTTCAACTATGTTTAGGCCGCATTACTATTATACAACTGCACAACGACGAAGAGGAGGAAAATTCAGTTAATCCTAGTCGTAACAAGTATGAAAGTAAATGGACGGGGCCTACCCGGTGCCAGTCGACTACAAGAGCTTTTTCTCTCGATCAGGTTGACAGTAATGTATGATATCGAACAAGACTCCGAGATCTCCTTCGACATCGATGAGAGCGACTAAGTGTATA"
	candidates := unique(getAllSubProteins(allCandiateProteins(dna)))
	for _, x := range candidates {
		fmt.Println(x)
	}
}