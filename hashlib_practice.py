#! usr/bin/env python3
"""Practice using the hashlib library."""

import os
from hashlib import md5


def main():
    print(create_hash_from_filenames('./txt_files'))


def convert_to_hash(filename):
    """Use md5 from hashlib to return string representation of filename's hash."""
    return md5(filename.encode()).hexdigest()


def create_hash_from_filenames(dir_name):
    """Return a dicitonary of filename key's and their hashlib.md5 hashes."""
    return {filename: convert_to_hash(os.path.join(dir_name, filename)) for filename in os.listdir(dir_name) if
            os.path.isfile((os.path.join(dir_name, filename)))}


if __name__ == '__main__':
    main()
