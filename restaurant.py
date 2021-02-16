#! usr/bin/python3
"""Create a menu dictionary to store items and their prices.  Users are then asked to pick items from the menu."""

def main():
    """Run program from the command line."""
    menu = {"sandwich": 10, "tea": 7, "fries": 4, "soda": 2, "burger": 8}
    restaurant(menu)

def restaurant(menu):
    """Asks user what they would like off the menu parameter and keeps track of their total."""
    currentSum = 0
    while(True):
        choice = input("Order: ")
        if choice:
            if choice in menu:
                currentSum += menu[choice]
                print(f"{choice} costs {menu[choice]}, total is {currentSum}")
            else:
                print(f"Sorry, we are fresh out of {choice} today.")
        else:
            print(f"Your total is {currentSum}")
            break

if __name__ == '__main__':
    main()