#!/usr/bin/env python3
"""plot3d_complex_sine.py"""

from __future__ import annotations

import typing

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.ticker import LinearLocator

if typing.TYPE_CHECKING:
    from typing import Any
    from matplotlib.axes import Axes

    from numpy.typing import NDArray


def f(z: NDArray[np.float_]) -> NDArray[np.float_]:
    return np.array(np.abs(np.sin(z)))


def plot(ax: Axes) -> None:
    z: NDArray[np.float_] = np.linspace(-2.5, 2.5, 100)
    y: NDArray[np.complex_] = np.linspace(-1j, 1j, 100)

    z, y = np.meshgrid(z, y)
    zy: NDArray[np.complex_] = z + y
    fz: NDArray[np.float_] = f(zy)  # type: ignore

    ax.zaxis.set_major_locator(LinearLocator(10))  # type: ignore
    ax.zaxis.set_major_formatter("{x:.02f}")  # type: ignore
    ax.plot_surface(z, y.imag, fz, cmap="coolwarm")


def main() -> None:
    plt.figure(__file__, constrained_layout=True)
    plot(plt.axes(projection="3d"))
    plt.show()


if __name__ == "__main__":
    main()
