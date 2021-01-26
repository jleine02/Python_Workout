#! usr/bin/env python3
""" A guessing game that uses user input """

import random

def main():
    """Function to run the program."""
    guessing_game()

def guessing_game():
    """Guessing game where user tries to guess random int between 0 and 100"""
    number_to_guess = random.randint(0,100)
    user_guess = int(input("Guess a number between 0 and 100 inclusive: "))
    while True:
        if user_guess < number_to_guess:
            print("Too low!")
        elif user_guess > number_to_guess:
            print("Too high!")
        else:
            print(f"Just right! The answer is {number_to_guess}. You win!")
            break
        user_guess = int(input("Guess a number between 0 and 100 inclusive: "))


if __name__ == "__main__":
    print("Main has been run.")
    main()
