#!/usr/bin/env python3
"""sum_squares.py"""



def gaussian(num: int) -> float:
    """ Calculates the sum using a Gaussian Summation Formula """
    gauss: float = ((2 * num**3) + (3 * num**2) + num) / 6
    return gauss

def loop(n: int) -> int:
    """ Calculates the sum using a loop to add squares individually"""
    loop_val = 0 # variable to hold the loop sum values as the loop operates
    for square in range(1, n + 1): # for loop with n + 1 to make it inclusive of 1,000
        loop_val += square**2 # adding the previous loop val to the next value
    return loop_val

def main() -> None:
    num_terms: int = 1_000
    gaussian_sum: float = gaussian(num_terms) 
    loop_sum: int = loop(num_terms)
    print(f"Loop: {loop_sum:<,}")
    print(f"Gaussian: {gaussian_sum:<,.0f}")

if __name__ == "__main__":
    main()