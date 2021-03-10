#! usr/bin/env python3
# get_final_line - Returns the final line in a file.

from sys import argv


def main():
    file_to_open = argv[1]
    final_line = get_final_line(file_to_open)
    print(f'The final line of the file is:\n\n{final_line}')


def get_final_line(file):
    """Returns the final line of the file passed in as a parameter."""
    with open(file, 'r') as f:
        final_line = ''
        for current_line in f:
            final_line = current_line
    return final_line


if __name__ == '__main__':
    main()
