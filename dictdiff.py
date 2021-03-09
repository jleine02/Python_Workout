#! usr/bin/env python3
"""dictdiff.py - Compares to dictionaries and prints the differences to stdout."""


def main():
    d1 = {'a': 1, 'b': 2, 'c': 3}
    d2 = {'a': 1, 'b': 2, 'c': 4}
    print(f'''The difference between {d1} and {d2} is:\n{dictdiff(d1, d2)}\n''')

    d3 = {'a': 1, 'b': 2, 'd': 3}
    d4 = {'a': 1, 'b': 2, 'c': 4}
    print(f'''The difference between {d3} and {d4} is:\n{dictdiff(d3, d4)}\n''')

    d5 = {'a': 1, 'b': 2, 'd': 4}
    print(f'''The difference between {d1} and {d5} is:\n{dictdiff(d1, d5)}\n''')

    print(f'd1 and d3 merged is : {dictupdate(d1, d3)}\n')

    print(f'd1, d2, and d3 merged is : {dictupdate(d1, d2, d3)}')


def dictdiff(dict_one, dict_two):
    """Compares dictionaries and stores differences in new dictionary."""
    output = {}
    all_keys = dict_one.keys() | dict_two.keys()

    for key in all_keys:
        if dict_one.get(key) != dict_two.get(key):
            output[key] = [dict_one.get(key), dict_two.get(key)]

    return output

def dictupdate(*args):
    """Merges multiple dictionaries into a single dictionary"""
    output = {}
    for dict in args:
        output.update(dict)
    return output


if __name__ == "__main__":
    main()
