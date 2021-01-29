#! usr/bin/env python3
"""Converts a string from input to pig latin and prints to console."""

def main():
    """Runs program from command line."""
    user_text = list(input("Please enter a word or phrase to conver to pig latin:\n").split())
    pig_latin_text = convert_to_piglatin(user_text)
    print(pig_latin_text)

def convert_to_piglatin(text):
    """Coverts list of strings to pig latin."""
    pig_latin_text = ''
    for word in text:
        pig_latin_text += pig_latin(word) + ' '

    return pig_latin_text

def pig_latin(word):
    # Need to refactor each use case into separate functions to test
    # TODO: Check for punctuation (multiple punctuation e.g. '!!!')
    # TODO: Check for capitalization
    # TODO: Transform

    if word[0] in 'aeiou':
        return f'{word}way'
    else:
        return f'{word[1:]}{word[0]}ay'

if __name__ == '__main__':
    main()
