from board_objects import Board_objects
import coordinates as coords
from moves import Moves


class Board:  
    def __init__(self):
        self.black = Board_objects(coords.black)
        self.white = Board_objects(coords.white)
        self.turn = "black"
        self.piece = ""
        self.piece_index = 0
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
                self.piece, self.piece_index = self.black.get_piece(new_coords)
                return
        if self.turn == "white":
            if not self.piece:
                self.piece, self.piece_index = self.white.get_piece(new_coords)
                return

        if self.moves.validate(self.turn, self.piece, self.piece_index, new_coords, self.black, self.white):
            if self.turn == "black":
                self.make_move(self.piece, self.piece_index, new_coords, self.black, self.white)
            elif self.turn == "white":
                self.make_move(self.piece, self.piece_index, new_coords, self.white, self.black)
        else:
            self.piece = None
            self.piece_index = 0
        return self.make_board()

    def make_move(self, piece, piece_index, new_coords, player, opponent):
        player.move(piece, piece_index, new_coords[0], new_coords[1])
        self.__capture(player, opponent, self.turn)
        self.turn = "white" if self.turn == "black" else "black"
        self.piece = None
        self.piece_index = 0
    
    def __capture(self, player, opponent, side):
        player_coords = player.get_all_coords()
        for coord in opponent.get_all_coords():
            if coord in player_coords:
                player.add_piece(opponent.pop(coord), side)


