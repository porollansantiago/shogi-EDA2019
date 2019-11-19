from board_objects import Board_objects
import coordinates as coords
from moves import Moves
from piece import Piece
import copy

class Board:  
    def __init__(self, white=coords.white, black=coords.black):
        self.black = Board_objects(black)
        self.white = Board_objects(white)
        self.turn = "black"
        self.moves = Moves()
        self.check = False
        self.checkmate = False
        self.check_pieces = []
        self.safe_moves = {}
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
                                self.black, self.white, self.move_array, self.check, self.safe_moves):
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
        if self.check and ([self.piece, self.piece_index] not in self.check_pieces):
            self.__init_move()
            return
        try:
            move_array = self.moves.get_move_array(self.turn, self.piece, self.piece_index, x, y, player, opponent, self.check, self.safe_moves)
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
        prev_coords = player.get_coords(piece, piece_index)
        player.move(piece, piece_index, x, y)
        self.capture(player, opponent, self.turn)
        self.game_is_over(self.turn, player, opponent)
        if not self.__promotion(prev_coords, y, x, piece):
            self.turn = "white" if self.turn == "black" else "black"
            self.__init_move()
        else:
            self.move_array = []
            self.promotion = [x, y]

    def __promotion(self, prev_coords, y, x, piece):
        return ((self.turn == "white" and (y > 5 or prev_coords[1] > 5)) or (self.turn == "black" and (y < 3 or prev_coords[1] < 3))) and x < 9 and piece != "GG " and prev_coords[0] < 9
    
    def capture(self, player, opponent, side):
        self.check = False
        self.check_pieces = []
        player_coords = player.get_all_coords()
        for coord in opponent.get_all_coords():
            if coord in player_coords:
                piece, idx = opponent.pop(coord)
                player.add_piece(piece, idx, side)

    def game_is_over(self, turn, player, opponent):
        self.safe_moves = {}
        self.check = False
        all_player_moves = self.moves.get_all_player_moves(turn, player, opponent)
        opponent_turn = "white" if turn == "black" else "black"
        king_coords = self.get_check(turn, player, opponent, all_player_moves)
        if not king_coords:
            return
        if not self.check:
            return
        if (self.__k_cant_be_saved(turn, opponent_turn,
                                                       player, opponent, king_coords)):
            self.checkmate = True

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

    def __k_cant_be_saved(self, turn, opponent_turn, player, opponent, king_coords):
        checkmate = True
        for pieces in opponent.coords.keys():
            for idx, piece in enumerate(opponent.coords[pieces]):
                if piece[0] < 9:
                    try:
                        for move in self.moves.get_move_array(opponent_turn, pieces, idx, 0, 0, opponent, player):
                            possible_board = self.__get_possible_board(turn, player, opponent, pieces, idx, move)
                            pb_player = possible_board.black if turn == "black" else possible_board.white
                            pb_opponent = possible_board.white if turn == "black" else possible_board.black
                            possible_board.capture(pb_opponent, pb_player, opponent_turn)
                            possible_board.get_check(turn, pb_player, pb_opponent)
                            if not possible_board.check:
                                self.check_pieces.append([pieces, idx])
                                try:
                                    self.safe_moves[(pieces, idx)].append(move)
                                except KeyError:
                                    self.safe_moves[(pieces, idx)] = [move]
                                checkmate = False
                    except TypeError:
                        pass
        return checkmate

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

    def get_pygame_objects(self, screen, settings):
        return (self.white.get_pygame_obj(screen, settings, "white"), 
                self.black.get_pygame_obj(screen, settings, "black"), 
                self.prep_board(screen, settings),
                self.prep_move_array(screen, settings),
                self.prep_sign(screen, settings))

    def prep_sign(self, screen, settings):
        winner = "blanco" if self.turn == "black" else "negro"
        if self.checkmate:
            return Piece(screen, settings, "Jaque mate, Gana " + winner, 12, 4, "black")
        if self.promotion:
            return Piece(screen, settings, "PRM", 10, 4, "black")
        elif self.check:
            return Piece(screen, settings, "Jaque", 10, 4, "black")


    def prep_move_array(self, screen, settings):
        move_array = []
        try:
            for move in self.move_array:
                p = Piece(screen, settings, 0, move[0], move[1], "movearray")
                move_array.append(p)
        except TypeError:
            return
        return move_array

    def prep_board(self, screen, settings):
        b = []
        for x in range(self.white.captured_x_top):
            p = Piece(screen, settings, None, x, 0, "board")
            b.append(p)
        for x in range(self.black.captured_x_top):
            p = Piece(screen, settings, None, x, 8, "board")
            b.append(p)
        for x in range(9):
            for y in range(1, 8):
                p = Piece(screen, settings, None, x, y, "board")
                b.append(p)
        return b
