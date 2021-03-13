#! usr/bin/env python3
"""Create a dictionary from a Unix-style password file."""

from sys import argv


def main():
    file_name = argv[1]
    with open(file_name, 'r') as infile:
        password_dict = password_to_dict(infile)

    print(password_dict)


def password_to_dict(file):
    """Creates a dictionary from a unix-style password file at /etc/passwd."""
    temp_dict = {}
    for line in file:
        if line.startswith(('#', '\n')):
            continue
        user_info = line.split(':')
        temp_dict[user_info[0]] = user_info[2]

    return temp_dict


if __name__ == '__main__':
    main()
