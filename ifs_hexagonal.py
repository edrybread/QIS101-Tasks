#!/usr/bin/env python3
"""ifs_hexagonal.py"""

from ifs import IteratedFunctionSystem
from pygame import Color
from simple_screen import SimpleScreen

ifs = IteratedFunctionSystem()


def plot_ifs(ss: SimpleScreen) -> None:
    iterations = 200_000
    x: float = 0.0
    y: float = 0.0
    clr: Color

    # Iterate (but don't draw) to let IFS reach its stable orbit
    for _ in range(100):
        x, y, clr = ifs.transform_point(x, y)

    # Now draw each pixel in the stable orbit
    for _ in range(iterations):
        x, y, clr = ifs.transform_point(x, y)
        ss.set_world_pixel(x, y, clr)


def main() -> None:
    """This function has 6 mappings to generate the hexagonal shape. Using a 30x30
    grid, the image will not touch the sides of the grid. The origin is at 15, 15
    and the far edges on the x-axis are at 5 and 25. The y-axis goes from 6.33 to
    23.66. Because the hexagonal shape is made up of equilateral triangles, the
    height of the triangles was found using the length of a side times the square
    root of 3 divided by 2. By mapping the 6 triangles, this fractal pattern
    emerged."""
    ifs.set_base_frame(0, 0, 30, 30)

    p: float = 1 / 6

    ifs.add_mapping(25, 15, 15, 15, 20, 23.66, Color("blue"), p)  # COD
    ifs.add_mapping(20, 23.66, 15, 15, 10, 23.66, Color("blue"), p)  # DOE
    ifs.add_mapping(10, 23.66, 15, 15, 5, 15, Color("blue"), p)  # EOF
    ifs.add_mapping(5, 15, 15, 15, 10, 6.33, Color("blue"), p)  # FOA
    ifs.add_mapping(10, 6.33, 15, 15, 20, 6.33, Color("blue"), p)  # AOB
    ifs.add_mapping(20, 6.33, 15, 15, 25, 15, Color("blue"), p)  # BOC

    ifs.generate_transforms()

    ss = SimpleScreen(
        world_rect=((0, 0), (30, 30)),
        screen_size=(900, 900),
        draw_function=plot_ifs,
        title="IFS Hexagonal",
    )
    ss.show()


if __name__ == "__main__":
    main()
