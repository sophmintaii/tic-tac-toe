"""
Contains implementation of class Board for tic tac toe game.
"""
import copy
import random

from btree import LinkedBinaryTree


class Board:
    """
    Board representation.
    """

    def __init__(self):
        """
        Create a new Board object.
        """
        self.positions = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.last_move = None

    def possible(self):
        """
        Returns list of possible moves in the board.
        """
        possible_positions = []
        for i, row in enumerate(self.positions):
            for j in range(len(row)):
                if self.is_empty(i, j):
                    possible_positions.append((i, j))
        return possible_positions

    def person_move(self):
        """
        Receives player's input.
        Checks whether move is correct and if it is so, adds it
        to the positions list.
        """
        print("Possible moves now are: ", str(self.possible()))
        user_input = input("Enter your move (row and col separated with "
                           "space: ")
        move = self.check_input(user_input)
        while not move:
            user_input = input("Incorrect input, try again: ")
            move = self.check_input(user_input)
        self.last_move = 7
        self.positions[move[0]][move[1]] = 7

    def computer_move(self):
        """
        Makes a computer's decision, adds its move to the positions
        list.
        """
        self.positions = self.gen_tree().positions
        print("I made a move.")
        print(self)
        print("Now, it's your turn!")

    def gen_tree(self):
        """
        Finds a better move on the board.
        :return: move to do.
        """
        tree = LinkedBinaryTree(self.positions)

        def recursion(board, tree):
            """Recursive function"""
            possible_moves = board.possible()
            if len(possible_moves) < 2:
                new_board = copy.deepcopy(board)
                if board.last_move == 5:
                    board.last_move = 7
                    new_board.positions[possible_moves[0][0]][
                        possible_moves[0][1]] = 7
                if board.last_move == 7:
                    board.last_move = 5
                    new_board.positions[possible_moves[0][0]][
                        possible_moves[0][1]] = 5
                tree.insert_left(new_board)
            else:
                move = board.last_move
                new_move1 = random.choice(possible_moves)
                possible_moves.remove(new_move1)
                new_move2 = random.choice(possible_moves)
                board1 = copy.deepcopy(board)
                board2 = copy.deepcopy(board)
                next_move = 5 if move == 7 else 7
                board.last_move = copy.deepcopy(next_move)
                board1.positions[new_move1[0]][new_move1[1]] = next_move
                board2.positions[new_move2[0]][new_move2[1]] = next_move
                tree.insert_left(board1)
                tree.insert_right(board2)
                recursion(board1, tree.get_left_child())
                recursion(board2, tree.get_right_child())

        recursion(self, tree)

        left_tree_points = self.win_combinations(tree.left_child.leaves_list())
        right_tree_points = self.win_combinations(
            tree.right_child.leaves_list())
        return tree.left_child.key if left_tree_points > right_tree_points \
            else tree.right_child.key

    @staticmethod
    def win_combinations(boards):
        """
        list(Board) -> int
        Returns number of winning combination in the list of Boards.
        """
        combs = 0
        for board in boards:
            if board.win():
                combs += 1 if board.win() == 5 else -1
        return combs

    def win(self):
        """
        Returns who is winning on the board.
        """
        for row in self.positions:
            if row == [5, 5, 5]:
                return 5
            if row == [7, 7, 7]:
                return 7

        if self.positions[0][0] == self.positions[1][0] == \
                self.positions[2][0] and self.positions[0][0] != 0:
            return self.positions[0][0]
        if self.positions[0][1] == self.positions[1][1] == \
                self.positions[2][1] and self.positions[0][1] != 0:
            return self.positions[1][1]
        if self.positions[0][2] == self.positions[1][2] == \
                self.positions[2][2] and self.positions[0][2] != 0:
            return self.positions[2][2]

        if self.positions[0][0] == self.positions[1][1] == \
                self.positions[2][2] and self.positions[0][0] != 0:
            return self.positions[0][0]

        if self.positions[0][2] == self.positions[1][1] == \
                self.positions[2][0] and self.positions[0][2] != 0:
            return self.positions[0][2]

        if not len(self.possible()):
            return 0

    def is_empty(self, i, j):
        """
        Checks whether cell is empty.
        :param i: row.
        :param j: col.
        :return: True if cell is empty, False otherwise.
        """
        return self.positions[i][j] == 0

    def check_input(self, value):
        """
        Checks whether value is correct input for person's move.
        :return: position if input is correct, False otherwise.
        """
        try:
            value = value.split(" ")
            row = int(value[0])
            col = int(value[1])
            assert (row, col) in self.possible()
            return row, col
        except (AssertionError, ValueError):
            return False

    def check_winner(self):
        """
        Returns string with information about the winner of the game.
        """
        win = self.win()
        if win is not None:
            if win == 7:
                return "You win!"
            if win == 5:
                return "Computer wins!"
            return "Draw!"

    def __str__(self):
        """
        Return string representation of the board.
        Empty cell is represented by space,
        X - person's move, O - computer's move.
        """
        values = {0: " ", 5: "O", 7: "X"}
        res = "-------\n"
        for row in self.positions:
            for cell in row:
                res += "|" + values[cell]
            res += "|\n-------\n"
        return res
