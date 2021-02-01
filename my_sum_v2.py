#! usr/bin/env python3
"""Refactoring my_sum to sum an unlimitted number of elements."""

def main():
        """Run program from command line."""
        print(my_sum([1,2,3,4,5],[6,7,8,9,10]))

def my_sum(*elements):
    """Sum a variable amount of elements regardless of type."""
    if elements is False:
        return elements
    output = elements[0]
    for element in elements[1:]:
        output += element
    return output


if __name__ == '__main__':
    main()
