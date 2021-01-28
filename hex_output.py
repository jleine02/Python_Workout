#! usr/bin.env python3
"""Program accepts a hex numberfrom user input and prints the integer output."""

def main():
    """Runs the program from command line."""
    hex_output()

def hex_output():
    """Accepts hex user input and prints the hex to console."""
    decimal_number = 0
    hex_number = input('Enter a hexadecimal number to conver to decimal: ')
    for power, digit in enumerate(reversed(hexnum)):
        decimal_number += int(digit, 16) * (16 ** power)
    print(hex_number)


if __name__ = "__main__":
    main()
