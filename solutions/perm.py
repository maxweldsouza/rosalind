# Without using the library
# https://en.wikipedia.org/wiki/Heap%27s_algorithm

from itertools import permutations

result = list(permutations(range(1, 7)))
print len(result)
for line in result:
   print ' '.join([str(x) for x in line]) 