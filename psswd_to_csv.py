#! usr/bin/env python3
"""psswd_to_csv.py - takes passwd-style file as input and creates csv output of username and user id."""

import csv


def main():


def passwd_to_csv(infile_name, outfile_name):
    """Writes user_name and user_id from infile to a csv using tabs as delimiter."""
    with open(infile_name, 'r') as passwd, open(outfile_name, 'w') as output:
        infile = csv.reader(passwd, delimiter=':')
        outfile = csv.writer(output, delimiter='\t')
        for record in infile:
            if len(record) > 1:
                outfile.writerow((record[0], record[2]))

if __name__ == '__main__':
    main()