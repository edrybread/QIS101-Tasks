#!/usr/bin/env python3
"""connect_four.py"""

"""I did just take Dr. Biersach's code for this solution. I typed it all out
by hand. When I tried this problem I thought maybe there would be a simpler
way to do it without checking every single option like this version does. 
I'm sure there is a more concise way to code this but its good to know that
even Dr. Biersach had to write something this repetitive."""


def check_ray(board: list[list[int]], row: int, col: int) -> bool:
    # Check all three "upwards pointing" rays
    if row > 2:
        # Check "upward to the right" ray
        if col < 4 and (
            board[row][col] == board[row - 1][col + 1]
            and board[row][col] == board[row - 2][col + 2]
            and board[row][col] == board[row - 3][col + 3]
        ):
            return True

        # Check "upward to the left" ray
        if col < 2 and (
            board[row][col] == board[row - 1][col - 1]
            and board[row][col] == board[row - 2][col - 2]
            and board[row][col] == board[row - 3][col - 3]
        ):
            return True

        # Check "straight upwards" ray
        if (
            board[row][col] == board[row - 1][col]
            and board[row][col] == board[row - 2][col]
            and board[row][col] == board[row - 3][col]
        ):
            return True

    # Check all three "downwards pointing rays"
    if row < 3:
        # Check "downward to the right" ray
        if col < 4 and (
            board[row][col] == board[row + 1][col + 1]
            and board[row][col] == board[row + 2][col + 2]
            and board[row][col] == board[row + 3][col + 3]
        ):
            return True
        # Check "downward to the left" ray
        if col < 4 and (
            board[row][col] == board[row + 1][col - 1]
            and board[row][col] == board[row + 2][col - 2]
            and board[row][col] == board[row + 3][col - 3]
        ):
            return True
        # Check "straight downwards" ray
        if col < 4 and (
            board[row][col] == board[row + 1][col]
            and board[row][col] == board[row + 2][col]
            and board[row][col] == board[row + 3][col]
        ):
            return True

    # Check "horizontal to the right" ray
    if col < 4 and (
        board[row][col] == board[row][col + 1]
        and board[row][col] == board[row][col + 2]
        and board[row][col] == board[row][col + 3]
    ):
        return True
    # Check "horizontal to the right" ray
    if col > 2 and (
        board[row][col] == board[row][col - 1]
        and board[row][col] == board[row][col - 2]
        and board[row][col] == board[row][col - 3]
    ):
        return True
    return False


def check_winner(player: int, board: list[list[int]]) -> bool:
    for row in range(6):
        for col in range(7):
            if board[row][col] == player and check_ray(board, row, col):
                return True
    return False


def print_winner(board: list[list[int]]) -> None:
    print(*board, sep="\n")
    if check_winner(1, board):
        print("Player 1 wins!")
    else:
        if check_winner(2, board):
            print("Player 2 wins!")
        else:
            print("No winner yet")
    print()


def main() -> None:
    board1: list[list[int]] = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0],
        [0, 2, 2, 1, 1, 0, 0],
        [0, 2, 1, 2, 2, 0, 1],
        [2, 1, 1, 1, 2, 0, 2],
    ]
    print_winner(board1)

    board2: list[list[int]] = [
        [0, 0, 2, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0],
        [0, 2, 2, 2, 2, 1, 0],
        [0, 1, 1, 2, 2, 2, 0],
        [2, 2, 1, 1, 1, 2, 0],
    ]
    print_winner(board2)

    board3: list[list[int]] = [
        [0, 0, 0, 2, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0],
        [0, 0, 1, 1, 2, 2, 0],
        [0, 1, 2, 1, 2, 2, 0],
        [0, 2, 2, 2, 1, 1, 0],
        [0, 1, 1, 2, 1, 2, 0],
    ]
    print_winner(board3)


if __name__ == "__main__":
    main()
