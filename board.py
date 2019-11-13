from board_objects import Board_objects
import coordinates as coords
from moves import Moves


class Board:  
    def __init__(self):
        self.black = Board_objects(coords.black)
        self.white = Board_objects(coords.white)
        self.turn = "black"
        self.piece = ""
        self.moves = Moves()

    def make_board(self):
        board = [["   " for _ in range(9)], ["   " for _ in range(9)],
                ["   " for _ in range(9)], ["   " for _ in range(9)], 
                ["   " for _ in range(9)], ["   " for _ in range(9)], 
                ["   " for _ in range(9)], ["   " for _ in range(9)], 
                ["   " for _ in range(9)]]
        board = self.black.add_to_board(board)
        board = self.white.add_to_board(board)
        return board

    def play(self, new_coords):
        if self.turn == "black":
            if not self.piece:
                self.piece = self.black.get_piece(new_coords)
                return
        if self.turn == "white":
            if not self.piece:
                self.piece = self.white.get_piece(new_coords)
                return
        if self.moves.validate(self.turn, self.piece, new_coords, self.black, self.white):
            if self.turn == "black":
                self.__make_move(self.piece, new_coords, self.black)
            elif self.turn == "white":
                self.__make_move(self.piece, new_coords, self.white)
        else:
            self.piece = None
        return self.make_board()

    def __make_move(self, piece, new_coords, player):
        player.move(piece, new_coords[0], new_coords[1])
        self.turn = "white" if self.turn == "black" else "black"
        self.piece = None
    

