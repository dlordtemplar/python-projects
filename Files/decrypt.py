
''' Decryption ("Gold-Bug", not graded)

(see also http://en.wikipedia.org/wiki/The_Gold-Bug)

We are given an encrypted file (using a very simple encryption scheme) in
which letters have been replaced by other letters. Implement the following
simple algorithm that decrypts the file exploiting information about the
relative frequency of characters:

1. Create a list E of characters sorted by the relative frequency of the
   characters in the encrypted file (descending order).

2. Create a list R of characters sorted by the relative frequency of the
   characters in the English reference file (descending order).

3. Replace each character x in the encrypted file as follows: if x is the nth
   character in E, replace x by the nth character in R.

4. Write the decoded text into a new file.

Note:

The decrypted text will not be perfect, i.e., in rare cases the characters are
decoded incorrectly.


Hints:

* The encrypted file is an English text

* The encrypted file only contains only lower-case letters

* Only the letters (a-z) have been encrypted; white spaces, digits and punctuation
  marks are preserved in the encrypted file.

* c.isalpha() tells you whether a character c is a letter (a-z)

* You should use a dictionary to count character frequencies. To obtain a list
  of keys (= characters) sorted by its numerical value, you can use

  sorted(d, key=d.get, reverse=True)

  where d is the dictionary mapping keys to numbers.

* You can use l.index(x) to find the index (= position) of some value x in a
  list l. For instance, ['a', 'b', 'c'].index('b') evaluates to 1.

* The builtin function "zip" might also be useful.
  See http://docs.python.org/py3k/library/functions.html#zip

* Note also that you can create dictionaries from lists of pairs as follows:

  dict([('key1', 'val1'), ..., ('keyn', 'valn')])
  
  creates a dictionary { 'key1' : 'val1', ..., 'keyn': 'valn' }

'''

import sys

def main():
    if len(sys.argv) != 4:
        print('Usage: python decrypt.py <encrypted file> <reference file> <output file>', file=sys.stderr)
        sys.exit(1)

    encfile = sys.argv[1]
    reffile = sys.argv[2]
    outfile = sys.argv[3]

    """
        1. Create a list E of characters sorted by the relative frequency of the
           characters in the encrypted file (descending order).
    """
    enc_dict = {}
    with open(encfile) as inputFile:
        for line in inputFile:
            for currentChar in line:
                if currentChar.isalpha():
                    if currentChar not in enc_dict:
                        enc_dict[currentChar] = 0
                    enc_dict[currentChar] += 1

    # List in descending order
    encList = sorted(enc_dict, key=enc_dict.get, reverse=True)

    """
        2. Create a list R of characters sorted by the relative frequency of the
           characters in the English reference file (descending order).
    """
    ref_dict = {}
    with open(reffile) as inputFile:
        for line in inputFile:
            for currentChar in line:
                if currentChar.isalpha():
                    if currentChar not in ref_dict:
                        ref_dict[currentChar] = 0
                    ref_dict[currentChar] += 1

    # List in descending order
    refList = sorted(ref_dict, key=ref_dict.get, reverse=True)

    # {'y': 'h', 'g': 'r', 'z': 'l', 'u': 'g', 'p': 'w', 'w': 'u', 'f': 'i', 'n': 'a', 'r': 'p', 'd': 'm', 's': 'b', 'b': 'j', 'h': 'e', 'x': 'y', 'e': 'o', 't': 't', 'c': 'n', 'a': 'x', 'm': 'd', 'o': 'z', 'v': 's', 'j': 'v', 'l': 'q', 'k': 'c', 'i': 'k', 'q': 'f'}
    replaceDict = dict(zip(encList, refList))

    """
        3. Replace each character x in the encrypted file as follows: if x is the nth
           character in E, replace x by the nth character in R.
    """
    toWrite = ""
    with open(encfile) as inputFile:
        for line in inputFile:
            for currentChar in line:
                if currentChar.isalpha():
                    toWrite += replaceDict[currentChar]
                else:
                    toWrite += currentChar

    """
        4. Write the decoded text into a new file.
    """
    with open(outfile, 'w') as outFile:
        outFile.write(toWrite)

if __name__ == '__main__':
    main()
