(defn cytosine? [base] (fn [nucleotide] (= nucleotide base)))
(defn count-nucleotides [base s]
    (count
        (filter (cytosine? base)
        (clojure.string/split s #""))))
(defn count-all-nucleotides [s]
    (list
        (count-nucleotides "A" s)
        (count-nucleotides "C" s)
        (count-nucleotides "G" s)
        (count-nucleotides "T" s))
)
(println (count-all-nucleotides "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"))