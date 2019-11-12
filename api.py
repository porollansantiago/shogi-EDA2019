from board import Board


class Api:
    def __init__(self):
        self.board = Board()

    def get_board(self):
        board = self.board.make_board()
        new_board = ""
        for line in board:
            new_board += "".join(line) + "\n"
        return new_board