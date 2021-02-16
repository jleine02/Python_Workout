# usr/bin/env python3
"""Simulate a simple login system using a dictionary."""


def main():
    """Run program from the command line."""
    login_to_system()


def login_to_system():
    """User prompted for username and password and denied access if either is incorrect."""
    login_info = {"jake": "s3cret", "rachel": "karl", "frank": "sebastian", "armando": "12345"}

    while True:
        user_name = input("username: ").strip()
        password = input("password: ").strip()

        if user_name in login_info.keys():
            if password == login_info[user_name]:
                print("Logged in successfully!")
                break
            else:
                print("Invalid user_name or password")
        else:
            print("Invalid user_name or password")


if __name__ == "__main__":
    main()
