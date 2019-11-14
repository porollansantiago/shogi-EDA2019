

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
        return None

    def get_coords(self, piece, x=0, y=0, replace_x=False, replace_y=False):
        new_coords = [0, 0]
        new_coords[0] = x if replace_x else self.coords[piece][0] + x
        new_coords[1] = y if replace_y else self.coords[piece][1] + y
        return new_coords
    
    def compare_coords(self, new_coords):
        return new_coords in self.coords.values()

    def move(self, piece_to_move, x, y):
        self.coords[piece_to_move] = [x, y]
