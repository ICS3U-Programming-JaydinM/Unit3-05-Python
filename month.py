#!/usr/bin/env python3

# Made by Jaydin Madore
# Made on Oct. 14, 2022
# This program gets the number from a user and then finds out what month it i


def main():

    # Gets the user's month with the number they input form.
    use_number = int(input("Enter the number of a month: "))

    # structure for months and their corresponding number.
    match use_number:
        case 1:
            print("1 is January.")
        case 2:
            print("2 is February.")
        case 3:
            print("3 is March.")
        case 4:
            print("4 is April.")
        case 5:
            print("5 is May.")
        case 6:
            print("6 is June.")
        case 7:
            print("7 is July.")
        case 8:
            print("8 is August.")
        case 9:
            print("9 is September.")
        case 10:
            print("10 is October.")
        case 11:
            print("11 is November.")
        case 12:
            print("12 is December.")

        # in case the user inputs an non-month number:
        case _:
            print(" Please enter an number between 1-12.")


if __name__ == "__main__":
    main()
