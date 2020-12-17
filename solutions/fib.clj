
(defn fib [n k]
    (loop [step n
           i 1
           j 1]
            (if (= step 1)
                i
                (recur (- step 1) j (+ j (* i k))))))
(println (fib 30 3))