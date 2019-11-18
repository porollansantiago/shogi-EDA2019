import copy
from piece import Piece


class Board_objects:
    def __init__(self, coord_dictionary, side=8):
        self.coords = copy.deepcopy(coord_dictionary)
        self.captured_x_top = 10
        self.captured_pieces = []
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
                except:
                    pass
        return board

    def get_piece(self, x, y):
        for piece in self.coords.keys():
            if [x, y] in self.coords[piece]:
                for idx, val in enumerate(self.coords[piece]):
                    if [x, y] == val:
                        return piece, idx
        return None, 0

    def get_coords(self, piece, piece_index, x=0, y=0, replace_x=False, replace_y=False):
        new_coords = [0, 0]
        new_coords[0] = x if replace_x else self.coords[piece][piece_index][0] + x
        new_coords[1] = y if replace_y else self.coords[piece][piece_index][1] + y
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
        compact = self.coords[piece_to_move][piece_index][0] >= 10
        self.coords[piece_to_move][piece_index] = [x, y]
        if compact:
            try:
                self.captured_pieces.remove([piece_to_move, self.coords[piece_to_move][piece_index]])
            except ValueError:
                pass
            self.__compact_captured(piece_to_move, piece_index)
    
    def __compact_captured(self, piece, piece_index):
        prev_coords = 9
        self.__sort(self.captured_pieces)
        for cpiece in self.captured_pieces:
                for idx, coord in enumerate(self.coords[cpiece[0]]):
                    if coord == cpiece[1]:
                        if coord[0] - prev_coords != 1:
                            self.coords[cpiece[0]][idx] = [coord[0] - (-1 + coord[0] - prev_coords), coord[1]]
                            prev_coords = coord[0] - (-1 + coord[0] - prev_coords)
                        else:
                            self.coords[cpiece[0]][idx] = [coord[0], coord[1]]
                            prev_coords = coord[0]
        self.captured_x_top -= 1

    def __sort(self, captured_pieces):
        for idx in range(1, len(captured_pieces)):
            val = captured_pieces[idx]
            idx2 = idx - 1
            while idx2 >= 0 and val[1][0] < captured_pieces[idx2][1][0]:
                captured_pieces[idx2 + 1] = captured_pieces[idx2]
                idx2 -= 1
            captured_pieces[idx2 + 1] = val

    #    stop = 0
    #    while stop != 20:
    #        for idx in range(0, len(captured_pieces) - 1):
    #            if captured_pieces[idx][1] > captured_pieces[idx + 1][1]:
    #                popped = captured_pieces.pop(idx + 1)
    #                captured_pieces.insert(idx, popped)
    #        stop += 1

    def get_all_coords(self):
        all_coords = []
        for val in self.coords.values():
            for coord in val:
                all_coords.append(coord)
        return all_coords

    def pop(self, coord):
        for piece in self.coords.keys():
            if coord in self.coords[piece]:
                for val in self.coords[piece]:
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
        self.captured_pieces.append([piece, [self.captured_x_top, self.y]])
        self.captured_x_top += 1
        return self.coords

    def promote(self, coords):
        piece, val = self.pop(coords)
        promoted_piece = self.__promote(piece)
        try:
            self.coords[promoted_piece].append([val])
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
        elif piece == "PKN ":
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
