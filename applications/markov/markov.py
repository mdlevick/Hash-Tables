import sys
sys.path.append('../../hashtable')
from hashtable import HashTable

import re
import random
from collections import Counter

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()

word_chain = {}

input_list = re.split("\s", words)
input_list = list(filter(lambda x: len(x) > 0, input_list))

for w, wp in zip(input_list, input_list[1:]):
    wq = w.lower().strip('":;,.-+=/\\|[]{}()*^&!?')
    wpq = wp.lower().strip('":;,.-+=/\\|[]{}()*^&!?')

    if w not in word_chain:
        word_chain[wq] = Counter()

    if w[-1] in ".!?":
        word_chain[wq]["."] += 1

        # Make sure next word is a valid start.
        if "." not in word_chain:
            word_chain["."] = Counter()

        word_chain["."][wpq] += 1

    else:
        word_chain[wq][wpq] += 1

def random_next(word):
    occ = dict(word_chain[word])
    next = random.choices(list(occ.keys()), weights=list(occ.values()), k=1)[0]
    return next

def gen_sentence():
    sent = []
    
    choice = random_next(".")
    while choice != ".":
        sent.append(choice)
        choice = random_next(choice)
    
    return " ".join(sent) + "."

for i in range(5):
    print(gen_sentence(), "\n")