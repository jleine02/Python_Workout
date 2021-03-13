#! usr/bin/env python3
"""word_count.py - Counts the number of characters, words, unique words, and total lines in the file."""

from sys import argv

def main():
    file = argv[1]
    word_count(file)


def word_count(file_name):
    """Parses file to return counts of characters, words,and total lines"""


if __name__ == '__main__':
    main()