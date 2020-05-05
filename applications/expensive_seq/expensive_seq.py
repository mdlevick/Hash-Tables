import sys
sys.path.append('../../hashtable')
from hashtable import HashTable

def expensive_seq(x, y, z, htbl = None):
    if x <= 0:
        return y + z
    
    if htbl is None:
        htbl = HashTable()

    a1 = htbl.get(str((x-1,y+1,z)))
    a2 = htbl.get(str((x-2,y+2,z*2)))
    a3 = htbl.get(str((x-3,y+3,z*3)))

    if a1 is None:
       a1 = expensive_seq(x-1,y+1,z, htbl)
       htbl.put(str((x-1,y+1,z)), a1)
    if a2 is None:
       a2 = expensive_seq(x-2,y+2,z*2, htbl)
       htbl.put(str((x-2,y+2,z*2)), a2)
    if a3 is None:
       a3 = expensive_seq(x-3,y+3,z*3, htbl)
       htbl.put(str((x-3,y+3,z*3)), a3)

    return a1 + a2 + a3

if __name__ == "__main__":
    for i in range(10):
        x = expensive_seq(i*2, i*3, i*4)
        print(f"{i*2} {i*3} {i*4} = {x}")

    print(expensive_seq(150, 400, 800))
