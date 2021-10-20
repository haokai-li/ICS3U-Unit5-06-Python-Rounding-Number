#!/usr/bin/env python3

# Created by: Haokai Li
# Created on: Oct 2021
# This Program is about rounding number


def round_number(number, decimal):
    # This function is about rounding number

    # process
    number_float = number * 10 ** decimal + 0.5
    number_float_final = int(number_float)
    number_output = number_float_final / 10 ** decimal

    return number_output


def main():
    # This function just call other functions

    # input
    user_number_string = input("Enter the number you want to round: ")
    user_decimal_string = input("Enter how many decimal places you want to round by: ")
    print("")

    try:
        user_number_number = float(user_number_string)
        user_decimal_number = float(user_decimal_string)

        # call functions
        rounding_number = round_number(
            number=user_number_number, decimal=user_decimal_number
        )

        # output
        print("The rounded number is {}".format(rounding_number))

    except Exception:
        # output
        print("You didn't enter an integer.")

    print("\nDone.")


if __name__ == "__main__":
    main()
