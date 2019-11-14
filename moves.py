

class Moves():
    def __init__(self):
        pass

    def validate(self, turn, piece_to_move, new_coords, black, white):
        if turn == "black":
            if self.validate_player(turn, piece_to_move, new_coords, black, white):
                return False
        elif turn == "white":
            if self.validate_player(turn, piece_to_move, new_coords, white, black):
                return False
        return True

    def validate_player(self, turn, piece_to_move, new_coords, player, other_player):
        if self.__overlapping(new_coords, player):
            return True
        if new_coords not in self.get_move_array(turn, piece_to_move, new_coords, player, other_player):
            return True
        return False

    def __overlapping(self, new_coords, player):
        for piece in player.coords.keys():
            if new_coords == player.coords[piece]:
                return True
        return False

    def get_move_array(self, turn, piece_to_move, new_coords, player, other_player):
        move_array = []
        if turn == "black":
            if "P" in piece_to_move:
                new_coords = player.get_coords(piece_to_move, 0, -1)
                if self.__inside_the_board(new_coords):
                    move_array.append(new_coords)
            elif "L" in piece_to_move:
                end, step = -1, -1
                move_array = self.get_lance_moves(piece_to_move, move_array, end, step, player, other_player)
            elif "KN" in piece_to_move:
                move_array = self.get_knight_moves(player, piece_to_move, move_array, -2)
            elif "SG" in piece_to_move:
                move_array = self.get_SG_moves(player, piece_to_move, move_array, -1)
            elif "GG" in piece_to_move:
                move_array = self.get_GG_moves(player, piece_to_move, move_array, -1, 1)
            elif "R" in piece_to_move:
                move_array = self.get_rook_moves(player, other_player, piece_to_move, move_array)
            elif " K " in piece_to_move:
                move_array = self.get_king_moves(player, piece_to_move, move_array)
            
        elif turn == "white":
            if "P" in piece_to_move:
                move_array.append(player.get_coords(piece_to_move, 0, 1))
            elif "L" in piece_to_move:
                end, step = 9, 1
                move_array = self.get_lance_moves(piece_to_move, move_array, end, step, player, other_player)
            elif "KN" in piece_to_move:
                move_array = self.get_knight_moves(player, piece_to_move, move_array, 2)
            elif "SG" in piece_to_move:
                move_array = self.get_SG_moves(player, piece_to_move, move_array, 1)
            elif "GG" in piece_to_move:
                move_array = self.get_GG_moves(player, piece_to_move, move_array, 1, -1)
            elif "R" in piece_to_move:
                move_array = self.get_rook_moves(player, other_player, piece_to_move, move_array)
            elif " K " in piece_to_move:
                move_array = self.get_king_moves(player, piece_to_move, move_array)
        print(move_array)
        return move_array


    def get_lance_moves(self, piece, move_array, end, step, player, other_player):
        for val in range(player.coords[piece][1] + step, end, step):
            new_coords = player.get_coords(piece, 0, val, False, True)
            if self.__inside_the_board(new_coords):
                move_array.append(player.get_coords(piece, 0, val, False, True))
            if player.compare_coords(new_coords) or other_player.compare_coords(new_coords):
                break
        return move_array

    def get_knight_moves(self, player, piece, move_array, y):
        for x in range(-1, 2, 2):
            new_coords = player.get_coords(piece, x, y)
            if self.__inside_the_board(new_coords):
                move_array.append(new_coords)
        return move_array

    def get_SG_moves(self, player, piece, move_array, val):
        move_array.append(self.__get_front_moves(move_array, player, piece, val))
        move_array.append(self.__get_side_moves(move_array, player, piece, val))
        return move_array

    def get_GG_moves(self, player, piece, move_array, front_val, back_val):
        move_array.append(self.__get_front_moves(move_array, player, piece, front_val))
        move_array.append(self.__get_side_moves(move_array, player, piece, 0))
        new_coord = player.get_coords(piece, 0, back_val)
        if self.__inside_the_board(new_coord):
            move_array.append(new_coord)
        return move_array

    def get_king_moves(self, player, piece, move_array):
        move_array.append(self.__get_front_moves(move_array, player, piece, 1))
        move_array.append(self.__get_front_moves(move_array, player, piece, -1))
        move_array.append(self.__get_side_moves(move_array, player, piece, 0))
        return move_array

    def get_rook_moves(self, player, other_player, piece, move_array):
        coords = player.get_coords(piece)
        move_array.append(self.__get_rook_col(coords, player, piece, move_array, other_player))
        move_array.append(self.__get_rook_row(coords, player, piece, move_array, other_player))
        return move_array

    def __get_rook_col(self, coords, player, piece, move_array, other_player):
        for val in range(coords[1] + 1, 9):
            new_coords = player.get_coords(piece, 0, val, False, True)
            move_array.append(new_coords)
            if player.compare_coords(new_coords) or other_player.compare_coords(new_coords):
                break
        for val in range(coords[1] - 1, -1, -1):
            new_coords = player.get_coords(piece, 0, val, False, True)
            move_array.append(new_coords)
            if player.compare_coords(new_coords) or other_player.compare_coords(new_coords):
                break
        return move_array

    def __get_rook_row(self, coords, player, piece, move_array, other_player):
        for val in range(coords[0] + 1, 9):
            new_coords = player.get_coords(piece, val, 0, True)
            move_array.append(new_coords)
            if player.compare_coords(new_coords) or other_player.compare_coords(new_coords):
                break
        for val in range(coords[0] - 1, -1, -1):
            new_coords = player.get_coords(piece, val, 0, True)
            move_array.append(new_coords)
            if player.compare_coords(new_coords) or other_player.compare_coords(new_coords):
                break
        return move_array

    def __get_side_moves(self, move_array, player, piece, val):
        for x in range(-1, 2, 2):
            new_coords = player.get_coords(piece, x, -val)
            if self.__inside_the_board(new_coords):
                move_array.append(new_coords)

    def __get_front_moves(self, move_array, player, piece, val):
        for x in range(-1, 2):
            new_coords = player.get_coords(piece, x, val)
            if self.__inside_the_board(new_coords):
                move_array.append(new_coords)
        return move_array

    def __inside_the_board(self, new_coords):
        return new_coords[0] >= 0 and new_coords[0] <= 8 and new_coords[1] <= 8 and new_coords[1] >= 0
        