#!/usr/bin/env python3
"""benfords_law.py"""

from __future__ import annotations

import typing

import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import numpy as np
import random

if typing.TYPE_CHECKING:
    from matplotlib.axes import Axes
    from numpy.typing import NDArray

"""I used Dr. Biersach's solution. I mostly did this because I didn't get to
this task before he showed us the solution and I don't want to fall behind"""


def p_MSD() -> NDArray[np.float_]:
    """A function that creates an array filled with the first digit from 100,000
    random numbers. These random numbers are generated from between 1 and 1 million
    and then they are raised to the 100th power. This creates very large numbers
    and this program helps to show the weird distribution of first digits for very
    large numbers."""
    p: NDArray[np.float_] = np.zeros(10, dtype=np.float_)
    for _ in range(100_000):
        n: int = random.randint(1, 1_000_000) ** 100
        # below the first digit of a random number is converted into a string,
        # then the first object in that string is pulled out, converted back into
        # and integer, and then added to the array p
        p[int(str(n)[0])] += 1
    p = p[1:]  # the first element of p is removed using array slicing to remove the 0
    p /= 100_000
    return p


def plot(ax: Axes) -> None:
    plt.bar(range(1, 10), p_MSD(), zorder=2.5)
    plt.grid()

    ax.set_title("Benford's Law")
    ax.set_xlabel("Most Significant Digit (MSD)")
    ax.set_ylabel("Probability of MSD")

    ax.xaxis.set_major_locator(MultipleLocator(1))


def main() -> None:
    plt.figure(__file__)
    plot(plt.axes())
    plt.show()


if __name__ == "__main__":
    main()
