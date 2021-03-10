#! usr/bin/env python3
# track_vowels_in_file - opens a file and uses a dictionary to keep track of the count of vowels in a file

from sys import argv
from collections import Counter


def main():
    file_to_open = argv[1]
    print(f'Number of vowels in file: {track_vowels_in_file(file_to_open)}')


def track_vowels_in_file(infile):
    """Updates a Counter object with vowels in each word of each line in a txt file."""
    vowel_freq = Counter()
    for line in read_file(infile):
        for word in line:
            for char in word:
                if char.lower() in 'aeiou':
                    vowel_freq.update(char.lower())
    return vowel_freq


def read_file(file):
    """Lazy read in each line of a file using a generator."""
    with open(file) as f:
        while True:
            line = f.readline()
            if not line:
                break
            yield line


if __name__ == '__main__':
    main()
