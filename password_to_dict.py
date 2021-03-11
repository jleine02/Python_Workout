#! usr/bin/env python3
"""Create a dictionary from a Unix-style password file."""


def main():
    with open('passwd.txt', r) as infile:
        password_dict = password_to_dict(infile)

    print(password_dict)


def password_to_dict(file):
    temp_dict = {}
    for line in file:
        if line.startswith('#'):
            continue
        temp_dict[line[0]] = line[2]

    return temp_dict


if __name__ == '__main__':
    main()
