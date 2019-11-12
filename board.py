from board_objects import Board_objects
import coordinates as coords

class Board:
    def __init__(self):
        self.black = Board_objects(coords.black)
        self.white = Board_objects(coords.white)

    def make_board(self):
        board = [["   " for _ in range(9)], ["   " for _ in range(9)],
                ["   " for _ in range(9)], ["   " for _ in range(9)], 
                ["   " for _ in range(9)], ["   " for _ in range(9)], 
                ["   " for _ in range(9)], ["   " for _ in range(9)], 
                ["   " for _ in range(9)]]
        board = self.black.add_to_board(board)
        board = self.white.add_to_board(board)
        return board
