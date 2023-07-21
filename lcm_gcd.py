#!/usr/bin/env python3
"""lcm_gcd.py"""

from math import gcd


def lcm(int1: int, int2: int) -> float:
    return (int1 * int2) / gcd(int1, int2)


def main() -> None:
    a: int = 447618
    b: int = 2011835
    print(f"The LCM of {a} and {b} = {lcm(a, b)}")


if __name__ == "__main__":
    main()
