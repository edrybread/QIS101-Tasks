#!/usr/bin/env python3
"""celsius_to_fahrenheit.py"""


def main() -> None:
    for celsius in range(-44, 107, 4):
        # Formula for converting fahrenheit to celsius
        fahrenheit: float = celsius * (9 / 5) + 32
        print(f"{celsius:>6.2f} C = {fahrenheit:>6.2f} F")
    print(f"{106:>6.2f} C = {106 * (9 / 5) + 32:>6.2f} F")


if __name__ == "__main__":
    main()
