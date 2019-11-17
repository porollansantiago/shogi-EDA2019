from board_objects import Board_objects
import coordinates as coords
from moves import Moves


class Board:  
    def __init__(self, white=coords.white, black=coords.black):
        self.black = Board_objects(black)
        self.white = Board_objects(white)
        self.turn = "black"
        self.piece = ""
        self.piece_index = 0
        self.moves = Moves()
        self.promotion = None
        self.check = False
        self.check_mate = False

    def make_board(self):
        board = [["   " for _ in range(self.white.captured_x_top)], ["   " for _ in range(9)],
                ["   " for _ in range(9)], ["   " for _ in range(9)],
                ["   " for _ in range(9)], ["   " for _ in range(9)],
                ["   " for _ in range(9)], ["   " for _ in range(9)],
                ["   " for _ in range(self.black.captured_x_top)]]
        self.black.add_to_board(board)
        self.white.add_to_board(board)
        return board

    def play(self, x, y):
        if self.promotion:
            if [x, y] == [10, 4]:
                if self.turn == "black":
                    self.black.promote(self.promotion)
                elif self.turn == "white":
                    self.white.promote(self.promotion)
            self.turn = "white" if self.turn == "black" else "black"
            self.piece = None
            self.piece_index = 0
            self.move_array = []
            self.promotion = None
            return
            
        if self.turn == "black":
            if not self.piece:
                self.piece, self.piece_index = self.black.get_piece(x, y)
                try:
                    move_array = self.moves.get_move_array(self.turn, self.piece, self.piece_index, x, y, self.black, self.white)
                except TypeError:
                    return
                else:
                    self.move_array = move_array
                    return move_array
        if self.turn == "white":
            if not self.piece:
                self.piece, self.piece_index = self.white.get_piece(x, y)
                try:
                    move_array = self.moves.get_move_array(self.turn, self.piece, self.piece_index, x, y, self.white, self.black)
                except TypeError:
                    return
                else:
                    self.move_array = move_array
                    return move_array

        if self.moves.validate(self.turn, self.piece, self.piece_index, x, y, self.black, self.white, self.move_array):
            if self.turn == "black":
                self.make_move(self.piece, self.piece_index, x, y, self.black, self.white)
            elif self.turn == "white":
                self.make_move(self.piece, self.piece_index, x, y, self.white, self.black)
        else:
            self.promotion = None
            self.piece = None
            self.piece_index = 0
            self.move_array = []

    def make_move(self, piece, piece_index, x, y, player, opponent):
        p_y = player.get_coords(piece, piece_index)[1]
        player.move(piece, piece_index, x, y)
        self.__capture(player, opponent, self.turn)
        self.__check(self.turn, piece, piece_index, x, y, player, opponent)
        if not self.__promotion(p_y, y, x):
            self.turn = "white" if self.turn == "black" else "black"
            self.piece = None
            self.piece_index = 0
            self.move_array = []
            self.promotion = None
        else:
            self.promotion = [x, y]
    
    def __capture(self, player, opponent, side):
        player_coords = player.get_all_coords()
        for coord in opponent.get_all_coords():
            if coord in player_coords:
                piece, idx = opponent.pop(coord)
                player.add_piece(piece, idx, side)

    def __promotion(self, p_y, y, x):
        return ((self.turn == "white" and (y > 5 or p_y >5)) or (self.turn == "black" and (y < 3 or p_y < 3))) and x < 9

    def __check(self, turn, piece, piece_index, x, y, player, opponent):
        all_player_moves = self.moves.get_all_player_moves(turn, player, opponent)
        try:
            king_coords = opponent.get_coords(" K ", 0)
        except KeyError:
            return
        else:
            self.check = king_coords in all_player_moves
        self.__check_mate(turn, player, opponent, king_coords, all_player_moves)
    
    def __check_mate(self, turn, player, opponent, king_coords, all_player_moves):
        opponent_turn = "white" if turn == "black" else "black"
        for coord in self.moves.get_move_array(opponent_turn, " K ", 0, king_coords[0], king_coords[1], opponent, player):
            if coord not in all_player_moves:
                return
        self.check_mate = True
        