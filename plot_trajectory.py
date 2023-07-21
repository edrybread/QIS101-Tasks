#!usr/bin/env python3
"""plot_trajectory.py"""

from __future__ import annotations

import typing

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

if typing.TYPE_CHECKING:
    from matplotlib.axes import Axes
    from numpy.typing import NDArray

"""Dr. Biersach's solution"""

"""This program plots the trajectory of secondary particles created by cosmic rays 
in the upper atmosphere. It reads in a csv file and then does a linear fit of that 
data and also draws a scatter plot of the data to compare the line to. It also prints the slope,
velocity, and height the secondary particle was created."""
def fit_linear(x: NDArray[np.float_], y: NDArray[np.float_]) -> tuple[float, float]:
    n: int = len(x)
    m: float = float(n * np.sum(x * y) - np.sum(x) * np.sum(y))
    m /= float(n * np.sum(x ** 2) - np.sum(x) ** 2)
    b: float = float(np.sum(y) - m * np.sum(x))
    b /= n
    return m, b

def plot(ax: Axes) -> None:
    data_file: Path = Path(__file__).parent.joinpath("ray.csv")
    data = np.genfromtxt(data_file, delimiter = ",")

    x = data[:, 0] # time in nanoseconds
    y = data[:, 1] # height in centimeters

    m: float
    b: float
    m, b = fit_linear(x, y)
    h = (np.abs(m) * 1e9 / 100) * (0.1743 / 1e3) / 1000
    c = 29.98 # speed of light in cm/ns

    print(f"Slope = {abs(m):.4f} cm/ns")
    print(f"Velocity = {np.abs(m) / c:,.2f}")
    print(f"Origination Height = {h:,.2f}")

    ax.scatter(x, y)
    ax.plot(x, m * x + b, color = "red", linewidth = 2)

    ax.set_title("Secondary Cosmic Ray Trajectory")
    ax.set_xlabel("time (ns)")
    ax.set_ylabel("height (cm)")
    ax.grid()

    plt.show()

def main() -> None:
    plt.figure(__file__)
    plot(plt.axes())
    plt.show()

if __name__ == '__main__':
    main()