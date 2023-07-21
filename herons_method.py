#!/usr/bin/env python3
"""herons_method.py"""

from random import randint
from math import sqrt

def heron(s: int, x: float) -> float:
    """Implements Heron's method to find the square root of a 
    number by iterating over a guess until the error is less
    than 1e-8"""
    current: float = s
    guess: float = x
    # this while loop takes the current guess and squares it and then
    # divides by two to find the next guess until the value is found
    while abs(guess ** 2 - current) > 1e-8:
        guess = (guess + current / guess) / 2
    return guess


def main() -> None:
    s = randint(1e6, 2e6) # type: ignore 
    # creates a random number to find the square root of
    x: float = s / 2
    z: float = heron(s, x)
    r: float = z
    print(f"The approximate square root of {s} is {r:0.8f}")
    print(F"The actual square root of {s} is {sqrt(s)}")

if __name__ == "__main__":
    main()
