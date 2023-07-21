#!\usr\bin\env python3
"""ladder_problem.py"""

from __future__ import annotations

import typing

import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize  # type: ignore
from matplotlib.ticker import AutoMinorLocator

if typing.TYPE_CHECKING:
    from matplotlib.axes import Axes
    from scipy.optimize import OptimizeResult  # type: ignore
    from numpy.typing import NDArray

"""I used Dr. Biersach's solution for this problem. It was really hard. I knew I
had seem something like this before but never this exact thing and couldn't quite
figure it out in time."""


def length(theta: NDArray[np.float_]) -> NDArray[np.float_]:
    return 2 / np.sin(theta) + 1 / np.cos(theta)


def plot(ax: Axes) -> None:
    # Don't include the start or end points as they cause division by zero
    # in either the first or second term of the sum for length
    theta: NDArray[np.float_] = np.linspace(0, np.pi / 2, 100, dtype=np.float_)[1:-2]
    ladder: NDArray[np.float_] = length(theta)

    ax.plot(theta, ladder)

    # Find point where ladder length is consistent
    # This means the first derivative of length() is zero at an extrema point
    # In this case that extrema is a global minimum of length()
    res: OptimizeResult = scipy.optimize.minimize(length, np.pi / 4)  # type: ignore

    # The result.x is an array, and we only want the first element
    c_theta: float = res.x[0]  # type: ignore
    c_length: float = float(length(np.array(c_theta)))  # type: ignore

    ax.set_title(f"Max Length = {c_length:.4f} m")

    ax.plot(c_theta, c_length, color="green", marker="o")
    ax.axhline(c_length, color="gray", linestyle="--")
    ax.vlines(x=c_theta, ymin=0, ymax=c_length, color="red")

    ax.set_xlabel(r"$\theta$ (radians)")
    ax.set_ylabel("Length (m)")

    ax.xaxis.set_minor_locator(AutoMinorLocator())
    ax.yaxis.set_minor_locator(AutoMinorLocator())

    ax.set_ylim(0, 25)
    plt.show()


def main() -> None:
    plot(plt.axes())
    plt.show()


if __name__ == "__main__":
    main()
