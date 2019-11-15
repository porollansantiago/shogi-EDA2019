import copy

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
    
    def compare_coords(self, new_coords):
        for piece in self.coords.keys():
            for coord in self.coords[piece]:
                if new_coords == coord:
                    return True

    def move(self, piece_to_move, piece_index, x, y):
        compact = self.coords[piece_to_move][piece_index][0] >= 10
        self.coords[piece_to_move][piece_index] = [x, y]
        if compact:
            self.captured_pieces.remove([piece_to_move, piece_index])
            self.__compact_captured(piece_to_move, piece_index)
    
    def __compact_captured(self, piece, piece_index):
        prev_coords = 9
        print(self.captured_pieces)
        for cpiece in self.captured_pieces:
            for coor in self.coords[cpiece[0]]:
                print(coor)
                if coor[0] - prev_coords != 1:
                    self.coords[cpiece[0]][cpiece[1]] = [coor[0] - 1, coor[1]]
                prev_coords = coor[0]
        self.captured_x_top -= 1
            

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
                        return piece

    def add_piece(self, piece, piece_index, side=None):
        self.y = 0 if side == "white" else self.y
        if not piece:
            return
        try:
            self.coords[piece].append([self.captured_x_top, self.y])
        except KeyError:
            self.coords[piece] = [[self.captured_x_top, self.y]]
        self.captured_x_top += 1
        self.captured_pieces.append([piece, piece_index])
        return self.coords
