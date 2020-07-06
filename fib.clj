
(defn fib [n k]
    (loop [step n
           i 1
           j 1]
            (if (= step 1)
                i
                (recur (- step 1) j (+ j (* i k))))))
5 4 3 2 1
1 1 4 7 19

(println (fib 30 3))