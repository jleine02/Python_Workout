#! usr/bin/env python3
"""Implementing the sum function allowing variable arg lengths"""

def main():
    """Runs program."""
    print(f"mysum([10, 20, 30, 40, 50], 50): {mysum([10, 20, 30, 40, 50], 50)}")

def mysum(*numbers, start=0):
    sum = start
    for number in numbers:
        sum += number
    return sum

if __name__ == '__main__':
    main()
