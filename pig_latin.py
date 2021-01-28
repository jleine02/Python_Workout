#! usr/bin/env python3
"""Converts a string from input to pig latin and prints to console."""

def main():
    """Runs program from command line."""
    pig_latin()

def pig_latin():
    user_string = input("Please enter text to convert to pig latin:\n").lower()
    pig_latin_string = ""
    vowels = 'aeiouy'
    for word in user_string:
        if word[0] in vowels:
            pig_latin_string += word + 'way' + ' '
        else:
            pig_latin_string += word[1:] + word[0] + 'ay' + ' '

    print(pig_latin_string)

if __name__ == '__main__':
    main()
