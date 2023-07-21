#!/usr/bin/env python3
"""sum_multiples.py"""


def multiples(number: int) -> float:
    """Calculates sum of values between 1 and 1900 divisible by both 7 and 11"""
    val = 0  # initial value
    for number in range(1, 1901):  # set range between 1 and 1900
        if (number % 7 == 0) and (number % 11 == 0):  # checks for divisibility
            val += number  # increment initial value by each number divisible number
    return val


def main() -> None:
    num = 0  # initialize value for function to call
    print(f"{multiples(num):<,.0f}")


if __name__ == "__main__":
    main()
