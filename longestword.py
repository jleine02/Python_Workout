#! usr/bin/#!/usr/bin/env python3
"""Identifies the longest word in a file-like object."""

from sys import argv

def main():
    """Runs program from command line."""
    word = longestword(argv[1])
    print(word)

def longestword(file):
    """Iterates over file object and returns longest string in all lines."""
    with open(file, 'r') as in_file:
        words = in_file.read().split() # opportunity to use a generator here?
    max_len = len(max(words, key=len))
    return [word for word in words if len(word) == max_len]

if __name__ == '__main__':
    main()
