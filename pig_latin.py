#! usr/bin/env python3
"""Converts a string from input to pig latin and prints to console."""

def main():
    """Runs program from command line."""
    user_text = list(input("Please enter a word or phrase to conver to pig latin:\n").split())
    pig_latin_text = convert_to_piglatin(user_text)
    print(pig_latin_text)

def convert_to_piglatin(user_text):
    """Converts list of strings to pig latin."""
    pig_latin_text = ''
    for word in user_text:
        pig_latin_text += pig_latin(word) + ' '

    return pig_latin_text

def pig_latin(word):
    """Transforms word to pig latin covering all edge cases."""
    # Check for punctuation (multiple punctuation e.g. '!!!')
    punctuation = ''
    while word[-1] in ',.!?:;':
        punctuation += word[-1]
        word = word[:-1]
    # Check for capitalization
    word_capitalized = word[0] == word[0].upper()
    # Transform
    if word[0] in 'aeiou':
        if word_capitalized:
            return (word + 'way' + punctuation).title()
        else:
            return f'{word}way{punctuation}'
    else:
        if word_capitalized:
            return (word[1:] + word[0] + 'ay' + punctuation).title()
        return f'{word[1:]}{word[0]}ay{punctuation}'

if __name__ == '__main__':
    main()
