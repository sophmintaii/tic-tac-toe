"""
Main module of the game.
"""
from board import Board


def run_game():
    """
    Starts and runs tic-tac-toe game.
    """
    board = Board()
    print("Hello! Here you can play tic-tac-toe game.")
    print("Here's your board by far:")
    print(board)
    while True:
        board.person_move()
        winner = board.check_winner()
        if winner is not None:
            return winner
        board.computer_move()
        winner = board.check_winner()
        if winner is not None:
            return winner


if __name__ == "__main__":
    print(run_game())
