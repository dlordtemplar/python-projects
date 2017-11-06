''' 2. Extracting noun phrases (3 Points)

Consider the file "wsj00-pos-oneline" that contains POS tagged text. In this
file, POS information is encoded as follows:

Pierre/NNP Vinken/NNP ,/, 61/CD years/NNS old/JJ ,/, will/MD join/VB 
the/DT board/NN as/IN a/DT nonexecutive/JJ director/NN Nov./NNP 29/CD ./.
...

Implement program that reads this file and prints all noun phrases that occur
in the text. To keep things simple, take noun phrases to be the following 
sequence of words/parts of speech:

    DT + zero or more JJ + NN

where DT is the POS for determiners like "the" or "a", JJ is the POS for
adjectives, and NN is the pos for nouns.

Example:

python3 regexp2.py

should ** print **:

the/DT board/NN
a/DT nonexecutive/JJ director/NN
a/DT nonexecutive/JJ director/NN
this/DT British/JJ industrial/JJ conglomerate/NN
...

'''

import sys
import re


def extract_noun_phrases(line):
    result = []
    m = re.search('([^ ]+/DT([^/JJ]+/JJ)*[^/NN]+/NN)', line)
    if m:
        result.append(m.group(1))
    return result


def main():

    with open('wsj00-pos-oneline.txt') as f:
        for line in f:
            for item in extract_noun_phrases(line):
                print(item)

if __name__ == '__main__':
    main()
