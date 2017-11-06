
'''

Counting tagged words (3 points)

On the lecture's homepage, you can find a part-of-speech (POS) tagged version of the 
file from the third exercise (wsj00-pos.txt), where each line contains a single token consisting
of a word and its POS tag, separated by '/'.

Write a program poscount.py that counts how often each word occurs in the file,
and how often it has been tagged with which POS.
The counts should be written to a new file, which is also given on the command line.

For instance,

    python3 wordcount2.py wsj00-pos.txt counts-wsj00-pos.txt

should produce a output like this:

Mortimer	1	NNP	1
foul	1	JJ	1
...
reported	16	VBN	7	VBD	9
...
before	26	RB	6	IN	20
...
allow	4	VB	2	VBP	2
...

The second column gives the total number of times the word occurs in the 
input file.

It is required to use exactly this format: 
word, tab (\t), number, POS, tab, number, POS, tab, number, ...
word, tab (\t), number, POS, tab, number, POS, tab, number, ...

Hint:

* To split a word/pos pair into two separate strings (word and pos), you can
  use pair.rsplit('/', 1); you can use the following code to assing the word
  and the pos of a word-pos pair to two distinct variables in one step:
  
  word, pos = token.rsplit('/', 1)

'''

import sys

def main():
    if len(sys.argv) != 3:
        print('Usage: python poscount.py <input file>', file=sys.stderr)
        sys.exit(1)

    input_filename = sys.argv[1]
    output_filename = sys.argv[2]

    counts = {}
    with open(input_filename) as inputFile:
        for line in inputFile:
            values = line.strip().rsplit(sep='/', maxsplit=1)
            if len(values) > 1:
                pos = values[1]  # POS
                word = values[0]  # word
                if word not in counts:
                    counts[word] = {}
                if pos not in counts[word]:
                    counts[word][pos] = 0
                else:
                    counts[word][pos] += 1

    with open(output_filename, 'w') as outputFile:
        for item in counts.items():
            toWrite = item[0]
            for pos in item[1].items():
                toWrite += "\t" + pos[0] + "\t" + str(pos[1])
            toWrite += "\n"
            outputFile.write(toWrite)


if __name__ == '__main__':
    main()


