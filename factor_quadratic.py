#!/usr/bin/env python3
"""factor_quadratic.py"""

from math import gcd


def prime_polynomial(x: int, y: int, z: int) -> int:
    return gcd(x, y, z)


def factor_quadratic(j: int, k: int, l: int) -> None:
    """Displays factors of the quadratic polynomial Jx^2 + Kx + L"""

    print(f"Given the quadratic: {j}x^2 + {k}x + {l}")

    for a in range(1, j + 1):
        if j % a == 0:
            c: int = j // a
            for b in range(1, l + 1):
                if l % b == 0:
                    d: int = l // b
                    if a * d + b * c == k:
                        print(f"The factors are: ({a}x + {b})({c}x + {d})")


def main() -> None:
    x: int = 115425
    y: int = 3254121
    z: int = 379020
    factor_quadratic(x, y, z)
    if prime_polynomial(x, y, z) == 1:
        print("The polynomial is prime, unable to factor")
        print(f"The GCD is: {prime_polynomial(x, y, z)}")


if __name__ == "__main__":
    main()
