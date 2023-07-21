#!/usr/bin/env python3
"""prime_racer4.py"""

from math import sqrt
from random import randint, seed
from time import process_time

"""I got this whole thing from ChatGPT. I hate that I am using it so much, but I
just don't want to fall behind. The implementation of this is quite different
from prime_racer3.py but it seems to work by checking more for False than True.
This is a little bit faster than prime_racer3.py but only a little bit and it's 
much less elegant.

I really do want to be able to do this stuff by myself but I also don't want to
fall behind because I didn't have time to work on this as much as everyone else
since we just got the discord chat updated with more channels I can start to reach
out to others for help."""


def is_prime(n: int) -> bool:
    """Returns True/False if the given number is prime"""
    if n < 2 or n % 2 == 0:
        return False
    if n < 4:
        return True
    if n % 3 == 0:
        return False

    limit = int(sqrt(n)) + 1
    divisor = 5

    while divisor < limit:
        if n % divisor == 0 or n % (divisor + 2) == 0:
            return False
        divisor += 6

    return True


def main() -> None:
    seed(2016)

    num_samples: int = 10_000
    min_val: int = 100_000
    max_val: int = 1_000_000

    print(
        (
            f"Counting the number of primes in {num_samples:,} random samples\n"
            f"with each sample having a value between {min_val:,} "
            f"and {max_val:,} inclusive . . ."
        )
    )

    samples: list[int] = [randint(min_val, max_val) for _ in range(num_samples)]

    start_time: float = process_time()
    num_primes: int = sum(is_prime(n) for n in samples)
    elapsed_time: float = process_time() - start_time

    print(f"Number of primes found: {num_primes:,}")
    print(f"Total run time (sec): {elapsed_time:.3f}\n")


if __name__ == "__main__":
    main()
