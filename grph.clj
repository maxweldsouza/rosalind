; Note: Output contains > prepended to each fasta label
(defn fasta-start? [s] (clojure.string/starts-with? s ">"))

(defn generate-map-helper [acc label lines]
    (if (= (count lines) 0)
        acc
        (if (fasta-start? (first lines))
            (recur
                (assoc acc (first lines) "") 
                (first lines) 
                (rest lines))
            (recur
                (assoc acc label (str (get acc label) (first lines))) 
                label 
                (rest lines))
        )))

(defn generate-map [fasta-lines]
    (generate-map-helper (hash-map) "" fasta-lines))


(defn get-labelled-seqs [file]
    (generate-map (clojure.string/split-lines file)))

(defn prefix-map [labelled-seqs]
    (group-by 
        (fn [label] (take 3 (get labelled-seqs label))) 
        (keys labelled-seqs)))

(defn suffix-map [labelled-seqs]
    (group-by 
        (fn [label] (take-last 3 (get labelled-seqs label))) 
        (keys labelled-seqs)))

(defn print-pairs [pairs]
    (doseq [i (range (count pairs))]
        (println (clojure.string/join " " (nth pairs i)))))

(defn main [file]
    (let [labelled-seqs (get-labelled-seqs file)]
        (let [s-map (suffix-map labelled-seqs)
              p-map (prefix-map labelled-seqs)]
        (print-pairs
            (filter
                (fn [[x y]]
                    (not= x y))
                (partition 
                    2
                    (flatten
                        (map 
                            (fn [source]
                                (map 
                                    (fn [dest]
                                        (list source dest))
                                    (get p-map (take-last 3 (get labelled-seqs source))))) 
                        (keys labelled-seqs)))))))))

(println (main (slurp "rosalind_grph.txt")))