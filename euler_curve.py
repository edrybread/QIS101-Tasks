#!usr/bin/env python3
"""euler_curve.py"""

from __future__ import annotations

import typing

from scipy.integrate import quad
import matplotlib.pyplot as plt
import numpy as np

if typing.TYPE_CHECKING:
    from matplotlib.axes import Axes
    from numpy.typing import NDArray

"""Dr. Biersach's solution"""

"""This program draws an Euler curve. This is done by taking the integral of two
functions from 0 to t where t is between 0 and 12.34. This curve spirals in on
itself."""

def x(t: float) -> float:
    # integral of cos(u^2) 
    return quad(lambda u: np.cos(u ** 2), 0, t)[0] # type: ignore

def y(t: float) -> float:
    # integral of sin(u^2) 
    return quad(lambda u: np.sin(u ** 2), 0, t)[0] # type: ignore

def ds(t: float) -> float:
    return float(np.sqrt(np.cos(t ** 2) ** 2 + np.sin(t ** 2) ** 2))

def plot(ax: Axes) -> None:
    tf: float = 12.34
    t: NDArray[np.float_] = np.linspace(0, tf, 1000)

    # vectorize creates a vector from an array so they have the same dimension
    # can be plotted.
    vx = np.vectorize(x) 
    vy = np.vectorize(y)
    ax.plot(vx(t), vy(t))

    arc_length: float = quad(ds, 0, tf)[0] # type: ignore

    ax.set_title(rf"Euler's Curve $(0\leq t<{tf:.2f})$ arc length = {arc_length:.2f}")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_aspect("equal")

    # Circle center is at the limit of integral of cos(x**2) as x goes to infinity
    c: float = np.sqrt(np.pi / 2) / 2
    ax.scatter(c, c, color = "red")

def main() -> None:
    plt.figure(__file__)
    plot(plt.axes())
    plt.show()

if __name__ == "__main__":
    main()