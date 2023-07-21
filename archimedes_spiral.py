#!/usr/bin/env python3
"""archimedes_spiral.py"""

from __future__ import annotations

import typing

import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

if typing.TYPE_CHECKING:
    from numpy.typing import NDArray

"""This is Dr. Biersach's solution. I was able to get the graph to draw the spiral 
by myself, but calculating the arc length was what I had trouble figuring out how
to do without making the code really complicated. 
I had forgotten about scipy integrate"""


def f(theta: float):  # type: ignore
    return np.sqrt(theta**2 + 1)


def plot(ax: Axes) -> None:
    theta: NDArray[np.float_] = np.linspace(0, 8 * np.pi, 1000)
    x = theta * np.cos(theta)
    y = theta * np.sin(theta)

    ax.plot(x, y)

    arc_length: float = integrate.quad(f, 0, 8 * np.pi)[0]  # type: ignore

    ax.set_title(
        r"Archimedes Spiral $(r = \theta, \;0\leq\theta\leq 8\pi)$"
        f"\nArc Length = {arc_length:.4f}"
    )
    ax.set_xlabel("x")
    ax.set_ylabel("y")

    ax.axhline(0, color="black")
    ax.axvline(0, color="black")

    ax.set_aspect("equal")


def main() -> None:
    plot(plt.axes())
    plt.show()


if __name__ == "__main__":
    main()
