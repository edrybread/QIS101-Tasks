#!/usr/bin/env python3
"""board_encoding.py"""


def decode(num: int) -> list[str]:
    """This function decodes the board number into base 3 and using that to
    determine which mark should go in which space"""
    board: list[str] = []
    while num > 0:
        if num % 3 == 2:  # if the remainder is a two, we print an O
            board.append("O")
        elif num % 3 == 1:  # if the remainder is a one, we print an X
            board.append("X")
        elif num % 3 == 0:  # if the remainder is a zero, we print a blank space
            board.append(" ")
        num //= 3  # floor divide the number now and then repeat
    while len(board) < 10:  # this fills out any remaining spaces for shorter numbers
        board.append(" ")
    return board


def draw_board(board: list[str]) -> str:
    """Drawing the board in an ascii format to be readable as a tic tac toe board
    using indexing from the decode output to place the marks in the correct place"""
    print()
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    return ""


def main() -> None:
    board_nums: list[int] = [2271, 1638, 12065]
    for num in board_nums:  # decode each board number included in board_nums
        print(f"Board: {num}", end="")
        print(f"{draw_board(decode(num))}")


if __name__ == "__main__":
    main()
