#! usr/bin/env python3
""" rainfall.py - program uses dictionary to keep track of user supplied
rainfall amounts for different cities."""

from collections import OrderedDict


def main():
    get_rainfall()


def get_rainfall():
    rain_fall = OrderedDict()

    while True:
        city_name = input("Enter city name: ")
        if city_name:
            rain_amount = input("Enter rain amount in mm: ")
            rain_fall[city_name] = rain_fall.get(city_name, 0) + int(rain_amount)
        else:
            break

    for city_name, rain_amount in rain_fall.items():
        print(f'{city_name}: {rain_amount}')


if __name__ == "__main__":
    main()
