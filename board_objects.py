

class Board_objects:
    def __init__(self, coord_dictionary):
        self.coords = coord_dictionary.copy()

    def add_to_board(self, board):
        for piece in self.coords.keys():
            board[self.coords[piece][1]][self.coords[piece][0]] = piece
        return board

    def get_piece(self, coords):
        for piece in self.coords.keys():
            if self.coords[piece] == coords:
                return piece
        return "   "

    def move(self, piece_to_move, x, y):
        self.coords[piece_to_move] = [x, y]
