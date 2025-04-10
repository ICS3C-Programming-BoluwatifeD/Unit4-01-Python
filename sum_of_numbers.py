#!/usr/bin/env python3
# Created By: Boluwatife Dada
# created on March 31
# This program asks the user to enter a positive integer


def main():
    # this function uses a while loop
    loop_counter = 0
    total_sum = 0

    # Get user_number
    while True:
        try:
            positive_integer_str = input("ENter a positive integer")
            positive_integer = int(positive_integer_str)
            if positive_integer > 0:
                break
            else:
                print("please enter a non-negative integer.")
        except ValueError:
            print("invalid input. please enter an integer.")
            print("")

    # process
    while loop_counter <= positive_integer:
        total_sum = total_sum + loop_counter
        loop_counter = loop_counter + 1

    print(f"The sum of numbers rom 0 to {positive_integer} is : {total_sum}")


if __name__ == "__main__":
    main()
