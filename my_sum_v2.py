#! usr/bin/env python3
"""Refactoring my_sum to sum an unlimitted number of elements."""

from sys import argv

def main():
        """Run program from command line."""
        elements = argv[1]
        print(my_sum(elements))

def my_sum(*elements):
    """Sum a variable amount of elements regardless of type."""


if __name__ == '__main__':
    main()
