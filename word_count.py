#! usr/bin/env python3
"""word_count.py - Counts the number of characters, words, unique words, and total lines in the file."""

from sys import argv


def main():
    file = argv[1]
    word_count(file)


def word_count(file_name):
    """Parses file to return counts of characters, words,and total lines"""
    counts = {'chars': 0,
              'words': 0,
              'lines': 0}
    unique_words = set()

    with open('file_name', 'r') as file:
        for line in file:
            counts['chars'] += len(line)
            counts['words'] += len(line.split())
            counts['lines'] += 1
            unique_words.update(line.split())

    counts['unique_words'] = len(unique_words)

    for key, value in counts.items():
        print(f'{key}: {value}')


if __name__ == '__main__':
    main()