#! usr/bin/env python3
"""Accepts a user name from input and then prints the letters in a triangle."""

def main():
    """Runs program from command line."""
    print_name_triangle()

def print_name_triangle():
    """Accepts a name from input and then prints letters in a triangle shape."""
    name = input('Please enter a name: ')
    for idx in range(len(name)):
        print(name[:idx + 1])

if __name__ == '__main__':
    main()
