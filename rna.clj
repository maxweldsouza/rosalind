(defn dna-to-rna [letter] 
    (if 
        (= letter "T") 
        "U"
        letter))
(defn convert [dna]
    (clojure.string/join 
        ""
        (map dna-to-rna (clojure.string/split dna #""))))

(println (convert (slurp "rosalind_rna.txt")))