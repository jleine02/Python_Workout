#! usr/bin/#!/usr/bin/env python3
"""Identifies the longest word in a file-like object."""

from sys import argv

def main():
    """Runs program from command line."""
    word = longestword(argv[1])
    print(word)

def longestword(file):
    """Iterates over file object and returns longest string in all lines."""


if __name__ == '__main__':
    main()
