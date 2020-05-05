from collections import Counter
import re

def word_count(s):
    c = Counter()

    for w in re.split("\s", s):
        if w not in '":;,.-+=/\\|[]{}()*^&!?':
            c[w.lower().strip('":;,.-+=/\\|[]{}()*^&!?')] += 1

    itms = list(dict(c).items())

    itms.sort(key=(lambda x: (-x[1], x[0])))

    for word, o in itms:
        str = word
        str += " " * (17 - len(str))
        str += "#" * o
        print(str)

    print('\n')

with open("robin.txt") as f:
    word_count(f.read())