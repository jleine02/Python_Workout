#! usr/bin/env python3
"""longest_word.py - reads files and returns information on the longest words included in each."""
import os


def main():
    print(find_all_longest_words('./txt_files'))


def find_longest_word(file):
    """Returns the longest word found within a file."""
    longest_word = ''
    with open(file, 'r') as f:
        for line in f:
            for word in line.split():
                if len(word) > len(longest_word):
                    longest_word = str(word)
    return longest_word


def find_all_longest_words(directory_name):
    """Return a dictionary that uses the filename as key and the longest word as the value."""
    return {filename: find_longest_word(os.path.join(directory_name, filename)) for filename in
            os.listdir(directory_name) if
            os.path.isfile(os.path.join(directory_name, filename))}


if __name__ == '__main__':
    main()
