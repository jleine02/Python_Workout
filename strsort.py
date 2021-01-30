#! usr/bin/env python3
"""Sorts a string based on eah characters unicode value."""

from sys import argv

def main():
    """Runs program from command line."""
    word = argv[1]
    sorted_word = strsort(word)
    print(sorted_word)

def strsort(word):
    """Sorts string parameter based on unicode value ascending order."""
    return ''.join(sorted(word))


if __name__ == '__main__':
    main()
