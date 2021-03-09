#! usr/bin/env python3
"""Returns the number of unique elements in a list."""


def main():
    list_one = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    list_two = [1, 2, 3, 4, 5, 6, 6, 9, 9, 0]

    print(f'{list_one} has {how_many_unique_numbers(list_one)} unique elements.\n')
    print(f'{list_two} has {how_many_unique_numbers(list_two)} unique elements.')


def how_many_unique_numbers(numbers):
    """Returns number of unique elements in a list of numbers."""
    return len(set(numbers))


if __name__ == '__main__':
    main()
