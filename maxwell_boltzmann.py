#!/usr/bin/env python3
"""maxwell_boltzmann.py"""

import numpy as np
from scipy.stats import maxwell
import matplotlib.pyplot as plt

import typing


if typing.TYPE_CHECKING:
    from numpy.typing import NDArray


def main() -> None:
    """Generates a plot with three curves on it, Maxwell-Boltzmann Distributions
    that are scaled to the three a values. This shows how the distribution changes
    as it is scaled. The is done using the maxwell function from scipy"""
    a1: int = 1
    a2: int = 2
    a3: int = 5
    x: NDArray[np.float_] = np.linspace(0, 20, 1000)
    fig, ax = plt.subplots(1, 1)
    ax.plot(x, maxwell.pdf(x, scale=a1), label="a1")
    ax.plot(x, maxwell.pdf(x, scale=a2), label="a2")
    ax.plot(x, maxwell.pdf(x, scale=a3), label="a3")
    ax.set_xlim(0, 20)
    ax.legend(loc="best", frameon=False)
    plt.show()


if __name__ == "__main__":
    main()
