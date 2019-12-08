#!/usr/bin/env python3

# Created by: Matsuru Hoshi
# Created on: Nov 2019
# This is program cylinder volume calculator

import random


def main():
    # This is generate 10 random number from 0-10 and figures out averag

    # variables for program
    sum = 0

    # This is a list holding the random numbers
    numbers = []

    # process
    for repeater in range(0, 10):
        number = random.randint(0, 100)
        numbers.append(number)
        # output
        print(numbers[repeater])
        sum = sum + numbers[repeater]

    average = sum / (repeater + 1)

    # output
    print("\n" + str(average))


if __name__ == "__main__":
    main()
