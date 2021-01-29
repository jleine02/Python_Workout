#! usr/bin/env python3
"""Prefaces vowels in a word with 'ub'."""

def main():
    """Runs program from command line."""
    user_input = input("Please type a word to convert to Ubbi Dubbi: ")
    translated_word = convert_to_ubbi_dubbi(user_input)
    print(f'Translated word: {translated_word}')

def convert_to_ubbi_dubbi(word):
    """Preface vowels in word with 'ub'."""
    word_list = []
    for char in word:
        if char in 'aeiou':
            word_list.append('ub')
        word_list.append(char)

    return ''.join(word_list)


if __name__ == '__main__':
    main()
