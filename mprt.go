// Failing. Off by one for some proteins
package main

import (
	"fmt"
	"regexp"
	"io/ioutil"
	"net/http"
	"strings"
	"strconv"
)

func getUniProt (uniprot_id string) string {
	resp, _ := http.Get("https://www.uniprot.org/uniprot/" + uniprot_id + ".fasta")

	defer resp.Body.Close()

	body, _ := ioutil.ReadAll(resp.Body)

	return string(body)
}

func getPositions(content string) []int {
	re := regexp.MustCompile(`N[^P][S|T][^P]`)
	matches := re.FindAllStringIndex(content, -1)
	result := make([]int, 0)
	for _, match := range matches {
		result = append(result, match[0] + 1)
	}
	return result
}

func removeFastaComment(content string) string {
	lines := strings.Split(content, "\n")
	result := ""
	for _, line := range lines {
		if strings.HasPrefix(line, ">") {
		} else {
			result =  result + line
		}
	}
	return result
}

func printPositions(positions []int) string {
	result := make([]string, 0)
	for _, position := range positions {
		result = append(result, strconv.Itoa(position))
	}
	return strings.Join(result, " ")
}

func main() {
	dat, _ := ioutil.ReadFile("rosalind_mprt.txt")

	uniprot_ids := strings.Split(string(dat), "\n")

	for _, uniprot_id := range uniprot_ids {
		content := getUniProt(uniprot_id)
		content = removeFastaComment(content)
		positions := getPositions(content)
		if len(positions) > 0 {
			fmt.Println(uniprot_id)
			fmt.Println(printPositions(positions))
		}
	}
}
