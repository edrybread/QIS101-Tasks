#!/usr/bin/env python3
"""hamming_weight.py"""

"""I tried this quite a few times but couldn't figure out how to iterate over
    a number. I used ChatGPT to finish out this function. This works, I've tested
    it on quite a few other numbers and it does what I think we are supposed to
    have it do. This is not how I would have thought to do it, but it definitely
    works."""


def ham(num: int) -> int:
    """This function takes a number and returns the amount of digits in that number
    that aren't zero."""
    weight: int = 0
    while num > 0:
        digit: int = num % 10  # get the remainder of our number divided by 10
        print(digit)
        if digit > 0:
            weight += 1  # increments the counter if the remainder is greater than 0
        num //= 10  # changes the value of num to the floor division of num by 10
    return weight


def main() -> None:
    sample: int = 95_601
    ham_weight: int = ham(sample)
    print(f"The Hamming weight of {sample} is {ham_weight}")


if __name__ == "__main__":
    main()
