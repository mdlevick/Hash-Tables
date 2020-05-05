from collections import Counter
import re

def word_count(s):
    c = Counter()
    for w in re.split("\s", s):
        if w not in '":;,.-+=/\\|[]{}()*^&':
            c[w.lower().strip('":;,.-+=/\\|[]{}()*^&')] += 1

    return dict(c)


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))