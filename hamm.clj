
(defn hamming-distance [a b acc]
    (if (= (count a) 0)
        acc
        (if (= (first a) (first b))
            (recur (rest a) (rest b) acc)
            (recur (rest a) (rest b) (+ acc 1)))))

(defn main [file]
    (let [lines (clojure.string/split-lines file)]
        (hamming-distance (first lines) (second lines) 0)))

(println (main (slurp "rosalind_hamm.txt")))