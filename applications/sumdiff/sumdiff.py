import sys
sys.path.append('../../hashtable')
from hashtable import HashTable
from itertools import permutations

"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""



# q = (1, 3, 4, 7, 12)
q = list(range(1, 10))
# takes a really long time!
# q = list(range(1, 200)) 

def f(x):
    return x * 4 + 6

quads = []

for i, x in enumerate(q):
    for j, y in enumerate(q[i:], start=i):
        for k, z in enumerate(q[j:], start=j):
	        if 3 + x + y + z in q[k:]:
                    quads.append((x, y, z, 3 + x + y + z))

for (x, y, z, c) in quads:
  p = set(permutations([x,y,z]))

  for x, y, z in p:
    print(f"f({x}) + f({y}) = f({c}) - f({z})")
