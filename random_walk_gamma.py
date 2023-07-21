#!/usr/bin/env python3
"""random_walk_gamma.py"""

from __future__ import annotations

import typing

import matplotlib.pyplot as plt
import numpy as np
from scipy.special import gamma  # type: ignore

if typing.TYPE_CHECKING:
    from matplotlib.axes import Axes
    from numpy.typing import NDArray

""""""


def plot(ax: Axes) -> None:
    n: int = 20_000
    x: NDArray[np.float_] = np.linspace(1, 25, 100, dtype=np.float_)

    y: NDArray[np.float_] = np.sqrt(2 * n / x) * np.power(
        gamma((x + 1.0) / 2) / gamma(x / 2), 2  # type: ignore
    )

    ax.plot(x, y, linewidth=2)

    ax.set_title("Mean Final Distance of a\n Uniform Random Walk on a Unit Lattice")
    ax.set_xlabel("Dimensions")
    ax.set_ylabel("Mean Final Distance")


def main() -> None:
    plt.figure(__file__)
    plot(plt.axes())
    plt.show()


if __name__ == "__main__":
    main()
