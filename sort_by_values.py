#!/usr/bin/env python3
"""Sort numbers by absolute value."""

def main():
    """Run from command line."""
    print(sort_abs_value([-20, 1, 0, 37, -252, 1001]))

def sort_abs_value(numbers):
    """Sort numbers using the absolute value as a key."""
    return sorted(numbers, key=abs)

if __name__ == '__main__':
    main()
