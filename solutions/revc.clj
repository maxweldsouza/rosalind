(defn complement [letter] 
    (case letter 
        "A" "T"
        "T" "A"
        "C" "G"
        "G" "C"
        ""))
(defn convert [dna]
    (clojure.string/join 
        ""
        (reverse (map complement (clojure.string/split dna #"")))))

(println (convert (slurp "rosalind_revc.txt")))