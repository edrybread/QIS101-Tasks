#!/usr/bin/env python3
"""plot3d_cylinder.py"""

from __future__ import annotations

import typing

import matplotlib.pyplot as plt
import numpy as np

if typing.TYPE_CHECKING:
    from matplotlib.axes import Axes

    from numpy.typing import NDArray


def plot(ax: Axes) -> None:
    u: NDArray[np.float_] = np.linspace(0, 2 * np.pi, 30)  # poloidal angle
    v: NDArray[np.float_] = np.linspace(-1, 1, 30)
    u, v = np.meshgrid(u, v)
    # fmt: off
    x: NDArray[np.float_] = np.cos(u)
    y: NDArray[np.float_] = np.sin(u)
    z: NDArray[np.float_] = v
    # fmt: on

    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")  # type: ignore

    ax.plot_wireframe(x, y, z)  # type: ignore
    ax.set_aspect("equal")


def main() -> None:
    plt.figure(__file__, constrained_layout=True)
    plot(plt.axes(projection="3d"))
    plt.show()


if __name__ == "__main__":
    main()
