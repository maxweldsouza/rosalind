(defn main [k m n]
    (let [z (+ k m n)]
        (+ 
            (* 
                (/ k z)
                (/ (- k 1) (- z 1)))
            (* 
                (/ k z)
                (/ m (- z 1)))
            (* 
                (/ k z)
                (/ n (- z 1)))

            (* 
                (/ m z)
                (/ k (- z 1)))
            (* 
                (/ m z)
                (/ (- m 1) (- z 1))
                (/ 3 4))
            (* 
                (/ m z)
                (/ n (- z 1))
                (/ 1 2))

            (* 
                (/ n z)
                (/ k (- z 1)))
            (* 
                (/ n z)
                (/ m (- z 1))
                (/ 1 2)))))

(println (float (main 19 25 17)))