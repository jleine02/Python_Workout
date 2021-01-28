#! usr/bin/env python3
"""Converts a string from input to pig latin and prints to console."""

def main():
    """Runs program from command line."""
    user_text = list(input("Please enter a word or phrase to conver to pig latin:\n").split())
    pig_latin_text = ''
    for word in user_text:
        pig_latin_text += pig_latin(word) + ' '

    print(pig_latin_text)

def pig_latin(word):
    if word[0] in 'aeiou':
        return f'{word}way'
    else:
        return f'{word[1:]}{word[0]}ay'

if __name__ == '__main__':
    main()
