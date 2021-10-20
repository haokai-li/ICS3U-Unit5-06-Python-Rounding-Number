#!/usr/bin/env python3

# Created by: Haokai Li
# Created on: Oct 2021
# This Program is about rounding number


def round_number(someVariable):
    # This function is about rounding number

    # process
    number_float = someVariable[0] * 10 ** someVariable[1] + 0.5
    number_float_final = int(number_float)
    someVariable[0] = number_float_final / 10 ** someVariable[1]


def main():
    # This function just call other functions
    someNumber = []

    # input
    user_number_string = input("Enter the number you want to round: ")
    user_decimal_string = input("Enter how many decimal places you want to round by: ")
    print("")

    try:
        user_number_number = float(user_number_string)
        user_decimal_number = int(user_decimal_string)

        someNumber.append(user_number_number)
        someNumber.append(user_decimal_number)
        # call functions
        round_number(someNumber)
        # output
        print("The rounded number is {}".format(someNumber[0]))

    except Exception:
        # output
        print("You didn't enter an integer.")

    print("\nDone.")


if __name__ == "__main__":
    main()
