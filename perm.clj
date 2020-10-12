(ns combs.core
    (:require [clojure.math.combinatorics :as combo]))

(let [perms (combo (range 1 3))]
    (println (count perms))
    (println perms))