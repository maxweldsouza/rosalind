
(defn fasta-start? [s] (clojure.string/starts-with? s ">"))

(defn gc? [n] 
    (or 
        (= n \G)
        (= n \C)))

(defn gc-content [seq]
    (float (/ 
        (count (filter gc? seq))
        (count seq)
    )))

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

(defn sort-by-gc [labelled-seqs]
    (into
        (sorted-map-by 
            (fn [key1 key2] 
                (compare (get labelled-seqs key2) (get labelled-seqs key1))))
        labelled-seqs))

(defn get-gc-content [fasta]
    (let [labelled-seqs (generate-map (clojure.string/split-lines fasta)) ] 
        (sort-by-gc
            (zipmap
                (keys labelled-seqs)
                (map 
                    (fn [k]
                        (gc-content (get labelled-seqs k)))
                    (keys labelled-seqs))))
    ))

(println (get-gc-content (slurp "rosalind_gc.txt")))