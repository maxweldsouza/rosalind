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

(defn char-count [seq char]
    (map (fn [x] (if (= x char) 1 0) ) seq))

(defn char-count-all [seq]
    (zipmap 
        "CGAT"
        (map (fn [c] (char-count seq c)) "CGAT")))

(defn merge-profiles [profiles]
    (reduce 
        (fn [a b] 
            { 
                \C (mapv + (get a \C) (get b \C)),
                \G (mapv + (get a \G) (get b \G)),
                \A (mapv + (get a \A) (get b \A)),
                \T (mapv + (get a \T) (get b \T)),
            }) 
        profiles))

(defn print-profile [profile]
    (clojure.string/join
        "\n"
        (map 
            (fn [x]
                (str x ": " (clojure.string/join " " (get profile x)))
            ) 
            "ACGT")))

(defn consensus-string [profile i acc]
    (if 
        (= i (count (get profile \C)))
        acc
        (recur 
            profile 
            (+ i 1) 
            (str 
                acc 
                (max-key 
                    (fn [x] 
                        (nth 
                            (get profile x) 
                            i)) 
                    \C \G \A \T)))))

(defn get-profile [seqs]
    (merge-profiles
        (map
            char-count-all
            seqs)))

(defn seqs-from-file [file]
    (vals (generate-map (clojure.string/split-lines file))))

(defn main [file]
    (let [profile (get-profile (seqs-from-file file))]
        (println 
            (consensus-string
                profile
                0
                ""))
        (println (print-profile profile))))

            
(println (main (slurp "rosalind_cons.txt")))
