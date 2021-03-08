#! usr/bin/env python3
"""dictdiff.py - Compares to dictionaries and prints the differences to stdout."""

from sys import argv


def main():
    dict_one, dict_two = argv[2], argv[3]
    dictdiff(dict_one, dict_two)


def dictdiff(dict_one, dict_two):
    """Compares dictionaries and stores differences in new dictionary."""
    output = {}
    all_keys = dict_one.keys() | dict_two.keys()

    for key in all_keys:
        if dict_one.get(key) != dict_two.get(key):
            output[key] = [dict_one.get(key), dict_two.get(key)]

    return output


if __name__ == "__main__":
    main()
