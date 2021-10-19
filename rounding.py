# !/user/bin/env python3

# Created by Trent Hodgins
# Created on 10/19/2021
# This is the Canada Post program
# This program lets the user to input a numbers and rounds it

import math


def round_decimal(user_number, user_places):
    # process
    user_number[0] = (user_number[0] * (10 ** user_places)) + 0.5
    user_number[0] = int(user_number[0])
    user_number[0] = float(user_number[0])
    user_number[0] = user_number[0] / (10 ** user_places)


def main():
    # calling functions and inputs
    user_number = []

    user_number_string = input("Enter the number you want to round: ")
    places_user_string = input("Enter the decimal places you want to round by: ")

    try:
        user_number_int = float(user_number_string)
        places_user_int = int(places_user_string)

        user_number.append(user_number_int)

        round_decimal(user_number, places_user_int)

        print("")
        print("The decimal rounded {0}".format(user_number[0]))
        print("\nDone.")

    except Exception:
        print("")
        print("Invalid input.")


if __name__ == "__main__":
    main()
