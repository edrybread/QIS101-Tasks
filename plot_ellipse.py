#!/usr/bin/env python3
"""plot_ellipse.py"""
from __future__ import annotations

import typing

import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import numpy as np


"""Again I used Dr. Biersach's solution for this task. A reason I haven't been
these completely on my own is because I am just trying to stay caught up. I lost 
a couple of days last week and so it has been hard to catch up and not fall behind.
I plan to continue working on the tasks on my own starting with the week 2 tasks."""

if typing.TYPE_CHECKING:
    from matplotlib.axes import Axes
    from numpy.typing import NDArray


def plot(ax: Axes) -> None:
    a = 100
    b = 50

    theta: NDArray[np.float_] = np.linspace(0, 2 * np.pi, 1000)
    radius = a * b / np.sqrt((b * np.cos(theta)) ** 2 + (a * np.sin(theta)) ** 2)

    x = radius * np.cos(theta)
    y = radius * np.sin(theta)

    ax.plot(x, y)

    ax.set_title(rf"$\frac{{x^2}}{{{a}^2}} + \frac{{y^2}}{{{b}^2}} = 1$")
    ax.set_xlabel("x")
    ax.set_ylabel("y")

    ax.grid()
    ax.axhline(0, color="black")
    ax.axvline(0, color="black")

    ax.xaxis.set_major_locator(MultipleLocator(20))
    ax.yaxis.set_major_locator(MultipleLocator(10))

    ax.set_aspect("equal")


def main() -> None:
    plt.figure(__file__)
    plot(plt.axes())
    plt.show()


if __name__ == "__main__":
    main()
