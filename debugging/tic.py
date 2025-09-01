#!/usr/bin/python3
"""Tic-Tac-Toe game with PEP8-compliant code."""


def print_board(board):
    """Display the current state of the Tic-Tac-Toe board."""
    print("\nCurrent board:")
    for row in board:
        print(" | ".join(row))
        print("-" * 5)


def check_winner(board):
    """Check if there is a winner on the board."""
    # Check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Check columns
    for col in range(len(board[0])):
        if (board[0][col] == board[1][col] == board[2][col]
                and board[0][col] != " "):
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False


def is_full(board):
    """Check if the board is full (tie condition)."""
    for row in board:
        if " " in row:
            return False
    return True


def get_valid_input(prompt):
    """Get a valid integer between 0 and 2 from the user."""
    while True:
        try:
            value = int(input(prompt))
            if value in [0, 1, 2]:
                return value
            print("Invalid input! Please enter 0, 1, or 2.")
        except ValueError:
            print("Invalid input! Please enter a number (0, 1, or 2).")


def tic_tac_toe():
    """Main game loop for Tic-Tac-Toe."""
    board = [[" "]*3 for _ in range(3)]
    player = "X"

    while True:
        print_board(board)
        print(f"Player {player}'s turn:")

        row = get_valid_input(
            "Enter row (0, 1, or 2): "
        )
        col = get_valid_input(
            "Enter column (0, 1, or 2): "
        )

        if board[row][col] != " ":
            print("That spot is already taken! Try again.")
            continue

        board[row][col] = player

        if check_winner(board):
            print_board(board)
            print(
                f"🎉 Player {player} wins!"
            )
            break

        if is_full(board):
            print_board(board)
            print("It's a tie! No more moves possible.")
            break

        # Switch player
        player = "O" if player == "X" else "X"


if __name__ == "__main__":
    tic_tac_toe()
