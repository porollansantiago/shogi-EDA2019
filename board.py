from board_objects import Board_objects
import coordinates as coords
from moves import Moves
import copy

class Board:  
    def __init__(self, white=coords.white, black=coords.black):
        self.black = Board_objects(black)
        self.white = Board_objects(white)
        self.turn = "black"
        self.moves = Moves()
        self.check = False
        self.checkmate = False
        self.__init_move()

    def __init_move(self):
        self.promotion = None
        self.piece = None
        self.piece_index = 0
        self.move_array = []

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
            return self.eval_promotion(x, y)
        if not self.piece:
            return self.get_piece(x, y)
        if self.moves.validate(self.turn, self.piece, self.piece_index, x, y,
                                self.black, self.white, self.move_array):
            return self.eval_move(x, y)
        else:
            self.__init_move()

    def get_piece(self, x, y):
        if self.turn == "black":
            return self.__get_piece(x, y, self.black, self.white)
        if self.turn == "white":
            return self.__get_piece(x, y, self.white, self.black)

    def __get_piece(self, x, y, player, opponent):
        self.piece, self.piece_index = player.get_piece(x, y)
        try:
            move_array = self.moves.get_move_array(self.turn, self.piece, self.piece_index, x, y, player, opponent)
        except TypeError:
            return
        else:
            self.move_array = move_array
            return move_array

    def eval_promotion(self, x, y):
        if [x, y] == [10, 4]:
            if self.turn == "black":
                self.black.promote(self.promotion)
            elif self.turn == "white":
                self.white.promote(self.promotion)
        player = self.black if self.turn == "black" else self.white
        opponent = self.black if self.turn == "white" else self.white
        self.game_is_over(self.turn, player, opponent)
        self.turn = "white" if self.turn == "black" else "black"
        self.__init_move()
        return self.check

    def eval_move(self, x, y):
        if self.turn == "black":
            self.make_move(self.piece, self.piece_index, x, y, self.black, self.white)
            if self.promotion:
                return "promotion"
            return self.check
        elif self.turn == "white":
            self.make_move(self.piece, self.piece_index, x, y, self.white, self.black)
            if self.promotion:
                return "promotion"
            return self.check

    def make_move(self, piece, piece_index, x, y, player, opponent):
        p_y = player.get_coords(piece, piece_index)[1]
        player.move(piece, piece_index, x, y)
        self.capture(player, opponent, self.turn)
        self.game_is_over(self.turn, player, opponent)
        if not self.__promotion(p_y, y, x):
            self.turn = "white" if self.turn == "black" else "black"
            self.__init_move()
        else:
            self.promotion = [x, y]

    def __promotion(self, p_y, y, x):
        return ((self.turn == "white" and (y > 5 or p_y >5)) or (self.turn == "black" and (y < 3 or p_y < 3))) and x < 9
    
    def capture(self, player, opponent, side):
        player_coords = player.get_all_coords()
        for coord in opponent.get_all_coords():
            if coord in player_coords:
                piece, idx = opponent.pop(coord)
                player.add_piece(piece, idx, side)

    def game_is_over(self, turn, player, opponent):
        all_player_moves = self.moves.get_all_player_moves(turn, player, opponent)
        opponent_turn = "white" if turn == "black" else "black"
        king_coords = self.get_check(turn, player, opponent, all_player_moves)
        if not king_coords:
            return
        self.checkmate = ((self.__k_cant_move(turn, opponent_turn, player,  opponent,
                                               king_coords, all_player_moves,)) 
                            and self.__k_cant_be_saved(turn, opponent_turn,
                                                       player, opponent, king_coords))

    def get_check(self, turn, player, opponent, all_player_moves=None):
        if not all_player_moves:
            all_player_moves = self.moves.get_all_player_moves(turn, player, opponent)
        try:
            king_coords = opponent.get_coords(" K ", 0)
        except KeyError:
            return
        else:
            self.check = king_coords in all_player_moves
            return king_coords

    def __k_cant_move(self, turn, opponent_turn, player, opponent, king_coords, all_player_moves):
        for coord in self.moves.get_move_array(opponent_turn, " K ", 0, king_coords[0], king_coords[1], opponent, player):
            try:
                if type(coord[0]) is int:
                    if coord not in all_player_moves:
                        return False
            except:
                pass
        return True

    def __k_cant_be_saved(self, turn, opponent_turn, player, opponent, king_coords):
        for pieces in opponent.coords.keys():
            for idx, piece in enumerate(opponent.coords[pieces]):
                if piece[0] < 9:
                    for move in self.moves.get_move_array(opponent_turn, pieces, idx, 0, 0, opponent, player):
                        possible_board = self.__get_possible_board(turn, player, opponent, pieces, idx, move)
                        pb_player = possible_board.black if turn == "black" else possible_board.white
                        pb_opponent = possible_board.white if turn == "black" else possible_board.black
                        possible_board.capture(pb_opponent, pb_player, opponent_turn)
                        possible_board.get_check(turn, pb_player, pb_opponent)
                        if not possible_board.check:
                            return False
        return True

    def __get_possible_board(self, turn, player, opponent, pieces, idx, move):
        white, black = self.__get_possible_board_coords(turn, player, opponent, pieces, idx, move)
        possible_board = Board(white, black)
        possible_board.white.captured_x_top = opponent.captured_x_top if turn == "black" else player.captured_x_top
        possible_board.white.captured_pieces = opponent.captured_pieces if turn == "black" else player.captured_pieces
        possible_board.black.captured_x_top = opponent.captured_x_top if turn == "white" else player.captured_x_top
        possible_board.black.captured_pieces = opponent.captured_pieces if turn == "white" else player.captured_pieces
        possible_board.turn = turn
        return possible_board

    def __get_possible_board_coords(self, turn, player, opponent, pieces, idx, move):
        possible_opponent_coords = copy.deepcopy(opponent.coords)
        possible_player_coords = player.coords
        possible_opponent_coords[pieces][idx] = move
        white = possible_opponent_coords if turn == "black" else possible_player_coords
        black = possible_player_coords if turn == "black" else possible_opponent_coords
        return white, black
