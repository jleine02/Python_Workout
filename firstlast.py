#! usr/bin.env python3
"""Retrieves the first and last element of the sequence."""

from sys import argv

def main():
    """Runs program from command line."""
    elements = firstlast(argv[1])
    print(elements)

def firstlast(sequence):
    """Identifies type of sequence and returns first and last elements of that
    sequence in the same type of sequence."""
    return sequence[:1] + sequence[-1:]

if __name__ == '__main__':
    main()
