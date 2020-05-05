import sys
sys.path.append('../../hashtable')
from hashtable import HashTable

def no_dups(s, htbl = None):
    if htbl is None:
        htbl = HashTable() 

    ret = []

    for w in s.split(" "):
        if htbl.get(w) is None:
            htbl.put(w, True)
            ret.append(w)
            
    return " ".join(ret)

if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))