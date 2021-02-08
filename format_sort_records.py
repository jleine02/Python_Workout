#! usr/bin/env python3
"""Read and print a list of tuples in a formatted manner."""

import operator

def main():
    """Run program from command line."""
    PEOPLE = [('Donald', 'Trump', 7.85),
              ('Valdimir', 'Putin', 3.626),
              ('Jinping', 'Xi', 10.603)]

    print('\n'.join(format_sort_records(PEOPLE)))

def format_sort_records(records):
    """Place holder."""
    output = []
    template = '{1:10} {0:10} {2:5.2f}'
    for record in sorted(records, key=operator.itemgetter(1,0)):
        output.append(template.format(*record))
    return output

if __name__ == '__main__':
    main()
