
(defn find-motif [dna search acc i]
    (if (= (count dna) 0)
        acc
        (if (clojure.string/starts-with? dna search)
            (recur (clojure.string/join (rest dna)) search (conj acc i) (+ i 1))
            (recur (clojure.string/join (rest dna)) search acc (+ i 1)))))

(defn main [file]
    (let [lines (clojure.string/split-lines file)]
        (find-motif (first lines) (second lines) (vec []) 1)))

(println (main (slurp "rosalind_subs.txt")))