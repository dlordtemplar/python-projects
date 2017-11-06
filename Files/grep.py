''' Grep (2 Points)

Write a program grep.py that searches a given input file for lines containing
a word, and returns a list with all matching lines. For instance, 

    python3 grep.py wsj00.txt programming

should create a list of all lines in wsj00.txt that contain the string "programming".
'''

import sys

def grep(filename, word):
    # a list containing all the lines with the word.
    linesWithWord = []
    
    with open(filename) as file:
        for line in file:
            words = line.split()
            if word in words:
                linesWithWord.append(line)

    return linesWithWord

def main():
    if len(sys.argv) != 3:
        print('Usage: python grep.py <input file> <word>', file=sys.stderr)
        sys.exit(1)
    
    filename = sys.argv[1]
    searchfor = sys.argv[2]
    
    for lineWithWord in grep(filename, searchfor):
        print(lineWithWord)

if __name__ == '__main__':
    main()
