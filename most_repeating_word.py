#!/usr/bin/env python3
"""Identifies and returns word in a list with the most repeating letters."""

from collections import Counter
import operator

def main():
    """Run program from command line."""
    WORDS = ['potato', 'leprechaun', 'elementary', 'soup', 'alpha', 'ninny',
            'sassafrass']
    print(most_repeating_word(WORDS))

def most_repeating_word(list_of_words):
    """Uses most_repeating_letter_count function to identify word in list with
    the greatest number of repeating characters."""
    return max(list_of_words, key=most_repeating_letter_count)

def most_repeating_letter_count(word):
    """Returns the count of the letter that appears the most in the word."""
    return Counter(word).most_common(1)[0][1]

if __name__ == '__main__':
    main()
