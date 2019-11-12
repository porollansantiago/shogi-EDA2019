from board_objects import Board_objects
import coordinates as coords

class Board:
    def __init__(self):
        self.black = Board_objects(coords.black)
        self.white = Board_objects(coords.white)
        self.turn = "black"

    def make_board(self):
        board = [["   " for _ in range(9)], ["   " for _ in range(9)],
                ["   " for _ in range(9)], ["   " for _ in range(9)], 
                ["   " for _ in range(9)], ["   " for _ in range(9)], 
                ["   " for _ in range(9)], ["   " for _ in range(9)], 
                ["   " for _ in range(9)]]
        board = self.black.add_to_board(board)
        board = self.white.add_to_board(board)
        return board

    def play(self, piece, new_coords):
        if self.turn == "black":
            self.__make_move(piece, new_coords, self.black)
        elif self.turn == "white":
            self.__make_move(piece, new_coords, self.white)
        return self.make_board()

    def __make_move(self, piece, new_coords, player):
        player.move(piece, new_coords[0], new_coords[1])
        self.turn = "white" if self.turn == "black" else "black"
    

