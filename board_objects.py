import copy
from piece import Piece


class Board_objects:
    def __init__(self, coord_dictionary, side=8):
        self.coords = copy.deepcopy(coord_dictionary)
        self.captured_x_top = 10
        try:
            self.y = self.coords[" K "][0][1]
        except KeyError:
            self.y = side

    def add_to_board(self, board):
        L = len(board[self.y])
        for _ in range(L, self.captured_x_top):
            board[self.y].append("   ")
        for piece in self.coords.keys():
            for coor in self.coords[piece]:
                try:
                    board[coor[1]][coor[0]] = piece
                except IndexError:
                    pass
        return board

    def get_piece(self, x, y):
        for piece in self.coords.keys():
            if [x, y] in self.coords[piece]:
                for idx, val in enumerate(self.coords[piece]):
                    if [x, y] == val:
                        return piece, idx
        return None, 0

    def get_coords(self, piece, piece_index, x=0, y=0,
                   replace_x=False, replace_y=False):
        new_coords = [0, 0]
        new_coords[0] = x if replace_x else (
            self.coords[piece][piece_index][0] + x)
        new_coords[1] = y if replace_y else (
            self.coords[piece][piece_index][1] + y)
        return new_coords

    def get_pawn_cols(self):
        p_cols = []
        for coord in self.coords[" P "]:
            if coord[0] not in p_cols:
                p_cols.append(coord[0])
        return p_cols

    def compare_coords(self, new_coords):
        for piece in self.coords.keys():
            for coord in self.coords[piece]:
                if new_coords == coord:
                    return True

    def move(self, piece_to_move, piece_index, x, y):
        prev_coords = self.coords[piece_to_move][piece_index]
        compact = self.coords[piece_to_move][piece_index][0] >= 10
        self.coords[piece_to_move][piece_index] = [x, y]
        if compact:
            if prev_coords[0] != self.captured_x_top - 1:
                self.__compact_captured(piece_to_move, piece_index)
            self.captured_x_top -= 1

    def __compact_captured(self, piece, piece_index):
        prev_coords = 9
        captured_pieces = self.get_captured_pieces()
        if len(captured_pieces) > 1:
            self.__sort(captured_pieces)
        cp = copy.deepcopy(captured_pieces)
        coords_copy = copy.deepcopy(self.coords)
        for cpiece in cp:
            if cpiece[2] - prev_coords != 1:
                self.coords[cpiece[0]][cpiece[1]] = [(
                    coords_copy[cpiece[0]][cpiece[1]][0] -
                    (-1 + coords_copy[cpiece[0]][cpiece[1]][0] - prev_coords)),
                    coords_copy[cpiece[0]][cpiece[1]][1]]
                prev_coords = (coords_copy[cpiece[0]][cpiece[1]][0] -
                               (-1 + coords_copy[cpiece[0]][cpiece[1]][0] -
                               prev_coords))
            else:
                self.coords[cpiece[0]][cpiece[1]] = [(
                    coords_copy[cpiece[0]][cpiece[1]][0]), (
                        coords_copy[cpiece[0]][cpiece[1]][1])]
                prev_coords = coords_copy[cpiece[0]][cpiece[1]][0]

    def get_captured_pieces(self):
        captured_pieces = []
        for piece in self.coords.keys():
            for idx, coord in enumerate(self.coords[piece]):
                if coord[0] > 9:
                    captured_pieces.append((piece, idx, coord[0]))
        return captured_pieces

    def __sort(self, captured_pieces):
        stop = 0
        while stop < 5:
            for idx in range(0, len(captured_pieces) - 1):
                if captured_pieces[idx][2] > captured_pieces[idx + 1][2]:
                    popped = captured_pieces.pop(idx + 1)
                    captured_pieces.insert(idx, popped)
                    stop = 0
                else:
                    stop += 1

    def get_all_coords(self):
        all_coords = []
        for val in self.coords.values():
            for coord in val:
                all_coords.append(coord)
        return all_coords

    def pop(self, coord):
        coords_copy = copy.deepcopy(self.coords)
        for piece in coords_copy.keys():
            if coord in coords_copy[piece]:
                for val in coords_copy[piece]:
                    if val == coord:
                        self.coords[piece].remove(val)
                        if self.coords[piece] == []:
                            self.coords.pop(piece)
                        return piece, val

    def add_piece(self, piece, piece_idx, side=None):
        self.y = 0 if side == "white" else self.y
        if not piece:
            return
        piece = self.__demote(piece)
        try:
            self.coords[piece].append([self.captured_x_top, self.y])
        except KeyError:
            self.coords[piece] = [[self.captured_x_top, self.y]]
        self.captured_x_top += 1
        return self.coords

    def promote(self, coords):
        piece, val = self.pop(coords)
        promoted_piece = self.__promote(piece)
        try:
            self.coords[promoted_piece].append(val)
        except KeyError:
            self.coords[promoted_piece] = [val]

    def __promote(self, piece):
        if piece == " P ":
            return "PP "
        elif piece == " L ":
            return "PL "
        elif piece == "KN ":
            return "PKN"
        elif piece == "SG ":
            return "PSG"
        elif piece == " B ":
            return "PB "
        elif piece == " R ":
            return "PR "
        return piece

    def __demote(self, piece):
        if piece == "PP ":
            return " P "
        elif piece == "PL ":
            return " L "
        elif piece == "PKN":
            return "KN "
        elif piece == "PSG":
            return "SG "
        elif piece == "PB ":
            return " B "
        elif piece == "PR ":
            return " R "
        return piece

    def get_pygame_obj(self, screen, settings, color):
        images = []
        for pieces in self.coords.keys():
            for coord in self.coords[pieces]:
                p = Piece(screen, settings, pieces, coord[0], coord[1], color)
                images.append(p)
        return images
