#! usr/bin/env python3
"""Sort a dictionary data structure by key value alphabetically."""

import operator

def main():
    """Run program from command line."""

    PEOPLE = [{'first': 'Reuven', 'last': 'Lerner',
               'email': 'reuven@lerner.co.il'},
              {'first': 'Donald', 'last': 'Trump',
               'email': 'president@whitehouse.gov'},
              {'first': 'Vladimir', 'last': 'Putin',
               'email': 'president@kremvax.ru'},]

    print(alphabetize_names(PEOPLE))

def alphabetize_names(list_of_dicts):
    """Sorts list based off of last and first name keys."""
    return sorted(list_of_dicts,
        key=operator.itemgetter('last', 'first'))

if __name__ == '__main__':
    main()
