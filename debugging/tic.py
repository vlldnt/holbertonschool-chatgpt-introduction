#!/usr/bin/python3

def print_board(board):
    """
    Prints the current state of the board.
    """
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    """
    Checks if there is a winner on the board.

    Returns:
        str: "X" or "O" if a player wins, otherwise None.
    """
    # Check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return row[0]

    # Check columns
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]

    return None

def is_full(board):
    """
    Checks if the board is full (i.e., no empty spaces).

    Returns:
        bool: True if the board is full, False otherwise.
    """
    for row in board:
        if " " in row:
            return False
    return True

def tic_tac_toe():
    """
    Main function to play the Tic Tac Toe game. Handles alternating turns, checking for a winner or tie, 
    and displaying the game board.
    """
    board = [[" "]*3 for _ in range(3)]
    player = "X"

    while True:
        print_board(board)

        # Input validation for row and column
        while True:
            try:
                row = int(input(f"Enter row (0, 1, or 2) for player {player}: ").strip())
                col = int(input(f"Enter column (0, 1, or 2) for player {player}: ").strip())

                if row not in [0, 1, 2] or col not in [0, 1, 2]:
                    print("Invalid input! Row and column must be 0, 1, or 2.")
                elif board[row][col] != " ":
                    print("That spot is already taken! Try again.")
                else:
                    break
            except ValueError:
                print("Invalid input! Please enter numbers only.")
            except IndexError:
                print("Invalid input! Row and column must be 0, 1, or 2.")

        # Make the move
        board[row][col] = player

        # Check for a winner
        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"Player {winner} wins!")
            break

        # Check for a tie
        if is_full(board):
            print_board(board)
            print("It's a tie!")
            break

        # Switch player
        player = "O" if player == "X" else "X"


# Run the game
if __name__ == "__main__":
    tic_tac_toe()