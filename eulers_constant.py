#!/usr/bin/env python3
"""eulers_constant.py"""

from __future__ import annotations

import typing

import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt

if typing.TYPE_CHECKING:
    from numpy.typing import NDArray
    from matplotlib.axes import Axes

"""Dr. Biersach's solution. The ln ln part was hard to picture it in code"""

h: NDArray[np.float_] = np.zeros(50)
h[2] = 1
for i in range(3, 50):
    h[i] = h[i - 1] + 1 / (i - 1)


def f(x: float) -> float:
    return float(np.log(np.log(1 / x)))  # type: ignore


def plot(ax: Axes) -> None:
    euler_constant: float = -integrate.quad(f, 0, 1)[0]  # type: ignore

    ax.step(np.arange(50), h, label=r"$\sum_{k = 1}^{\lfloor x\rfloor}\frac{1}{k}$")

    # Cannot use first element since log(0) is undefined
    x: NDArray[np.float_] = np.linspace(0, 50, 500)[1:]
    logf: NDArray[np.float_] = euler_constant + np.log(x)  # type: ignore

    ax.plot(x, logf, label=r"$\gamma + \ln x$")
    ax.legend()


def main() -> None:
    plot(plt.axes())
    plt.show()


if __name__ == "__main__":
    main()
