

class Moves():
    def validate(self, turn, piece_to_move, piece_index, x, y, black, white, move_array=None):
        if turn == "black":
            if self.validate_player(turn, piece_to_move, piece_index, x, y, black, white, move_array):
                return False
        elif turn == "white":
            if self.validate_player(turn, piece_to_move, piece_index, x, y, white, black, move_array):
                return False
        return True

    def validate_player(self, turn, piece_to_move, piece_index, x, y, player, other_player, move_array):
        if not move_array:
            move_array = self.get_move_array(turn ,piece_to_move, piece_index, x, y,player, other_player)
        if self.__overlapping(x, y, player):
            return True
        if [x, y] not in move_array:
            return True
        return False

    def __overlapping(self, x, y, player):
        for piece in player.coords.keys():
            if [x, y] in player.coords[piece]:
                return True
        return False

    def get_move_array(self, turn, piece_to_move, piece_index, x, y, player, other_player):
        move_array = []
        if turn == "black":
            if " P " == piece_to_move:
                new_coords = player.get_coords(piece_to_move, piece_index, 0, -1)
                if self.__inside_the_board(new_coords):
                    move_array.append(new_coords)
            elif " L " == piece_to_move:
                end, step = -1, -1
                move_array = self.get_lance_moves(piece_to_move, piece_index, move_array, end, step, player, other_player)
            elif "KN " == piece_to_move:
                move_array = self.get_knight_moves(player, piece_to_move, piece_index, move_array, -2)
            elif "SG " == piece_to_move:
                move_array = self.get_SG_moves(player, piece_to_move, piece_index, move_array, -1)
            elif "GG " == piece_to_move:
                move_array = self.get_GG_moves(player, piece_to_move, piece_index, move_array, -1, 1)
            elif " R " == piece_to_move:
                move_array = self.get_rook_moves(player, other_player, piece_to_move, piece_index, move_array)
            elif " B " == piece_to_move:
                move_array = self.get_bishop_moves(player, other_player, piece_to_move, piece_index, move_array)
            elif " K " == piece_to_move:
                move_array = self.get_king_moves(player, piece_to_move, piece_index, move_array)
            
        elif turn == "white":
            if " P " == piece_to_move:
                move_array.append(player.get_coords(piece_to_move, piece_index, 0, 1))
            elif " L " == piece_to_move:
                end, step = 9, 1
                move_array = self.get_lance_moves(piece_to_move, piece_index, move_array, end, step, player, other_player)
            elif "KN " == piece_to_move:
                move_array = self.get_knight_moves(player, piece_to_move, piece_index, move_array, 2)
            elif "SG " == piece_to_move:
                move_array = self.get_SG_moves(player, piece_to_move, piece_index, move_array, 1)
            elif "GG " == piece_to_move:
                move_array = self.get_GG_moves(player, piece_to_move, piece_index, move_array, 1, -1)
            elif " R " == piece_to_move:
                move_array = self.get_rook_moves(player, other_player, piece_to_move, piece_index, move_array)
            elif " B " in piece_to_move:
                move_array = self.get_bishop_moves(player, other_player, piece_to_move, piece_index, move_array)
            elif " K " == piece_to_move:
                move_array = self.get_king_moves(player, piece_to_move, piece_index, move_array)
        print(move_array)
        return move_array


    def get_lance_moves(self, piece, piece_index, move_array, end, step, player, other_player):
        for val in range(player.coords[piece][piece_index][1] + step, end, step):
            new_coords = player.get_coords(piece, piece_index, 0, val, False, True)
            if self.__inside_the_board(new_coords):
                move_array.append(player.get_coords(piece, piece_index, 0, val, False, True))
            if player.compare_coords(new_coords) or other_player.compare_coords(new_coords):
                break
        return move_array

    def get_knight_moves(self, player, piece, piece_index, move_array, y):
        for x in range(-1, 2, 2):
            new_coords = player.get_coords(piece, piece_index, x, y)
            if self.__inside_the_board(new_coords):
                move_array.append(new_coords)
        return move_array

    def get_SG_moves(self, player, piece, piece_index, move_array, val):
        move_array.append(self.__get_front_moves(move_array, player, piece, piece_index, val))
        move_array.append(self.__get_side_moves(move_array, player, piece, piece_index, val))
        return move_array

    def get_GG_moves(self, player, piece, piece_index, move_array, front_val, back_val):
        move_array.append(self.__get_front_moves(move_array, player, piece, piece_index, front_val))
        move_array.append(self.__get_side_moves(move_array, player, piece, piece_index, 0))
        new_coord = player.get_coords(piece, piece_index, 0, back_val)
        if self.__inside_the_board(new_coord):
            move_array.append(new_coord)
        return move_array

    def get_king_moves(self, player, piece, piece_index, move_array):
        move_array.append(self.__get_front_moves(move_array, player, piece, piece_index, 1))
        move_array.append(self.__get_front_moves(move_array, player, piece, piece_index, -1))
        move_array.append(self.__get_side_moves(move_array, player, piece, piece_index, 0))
        return move_array

    def get_rook_moves(self, player, other_player, piece, piece_index, move_array):
        coords = player.get_coords(piece, piece_index)
        move_array.append(self.__get_rook_col(coords, player, piece, piece_index, move_array, other_player))
        move_array.append(self.__get_rook_row(coords, player, piece, piece_index, move_array, other_player))
        return move_array

    def get_bishop_moves(self, player, other_player, piece, piece_index, move_array):
        coords = player.get_coords(piece, piece_index)
        start1 = coords[0] if coords[0] > coords[1] else coords[1]
        for val in range(1, 9 - start1):
            new_coords = player.get_coords(piece, piece_index, val, val)
            move_array.append(new_coords)
            if player.compare_coords(new_coords) or other_player.compare_coords(new_coords):
                break
        start2 = coords[0] if coords[0] < coords[1] else coords[1]
        for val in range(start2, -1, -1):
            new_coords = player.get_coords(piece, piece_index, -val, -val)
            move_array.append(new_coords)
            if player.compare_coords(new_coords) or other_player.compare_coords(new_coords):
                break
        start3 = 8 - coords[0] if 8 - coords[0] < coords[1] else coords[1]
        for val in range(1, start3 + 1):
            new_coords = player.get_coords(piece, piece_index, val, -val)
            move_array.append(new_coords)
            if player.compare_coords(new_coords) or other_player.compare_coords(new_coords):
                break
        start4 = 8 - coords[1] if 8 - coords[1] < coords[0] else coords[0]
        for val in range(1, start4 + 1):
            new_coords = player.get_coords(piece, piece_index, -val, val)
            move_array.append(new_coords)
            if player.compare_coords(new_coords) or other_player.compare_coords(new_coords):
                break
        return move_array


    def __get_rook_col(self, coords, player, piece, piece_index, move_array, other_player):
        for val in range(coords[1] + 1, 9):
            new_coords = player.get_coords(piece, piece_index, 0, val, False, True)
            move_array.append(new_coords)
            if player.compare_coords(new_coords) or other_player.compare_coords(new_coords):
                break
        for val in range(coords[1] - 1, -1, -1):
            new_coords = player.get_coords(piece, piece_index, 0, val, False, True)
            move_array.append(new_coords)
            if player.compare_coords(new_coords) or other_player.compare_coords(new_coords):
                break
        return move_array

    def __get_rook_row(self, coords, player, piece, piece_index, move_array, other_player):
        for val in range(coords[0] + 1, 9):
            new_coords = player.get_coords(piece, piece_index, val, 0, True)
            move_array.append(new_coords)
            if player.compare_coords(new_coords) or other_player.compare_coords(new_coords):
                break
        for val in range(coords[0] - 1, -1, -1):
            new_coords = player.get_coords(piece, piece_index, val, 0, True)
            move_array.append(new_coords)
            if player.compare_coords(new_coords) or other_player.compare_coords(new_coords):
                break
        return move_array

    def __get_side_moves(self, move_array, player, piece, piece_index, val):
        for x in range(-1, 2, 2):
            new_coords = player.get_coords(piece, piece_index, x, -val)
            if self.__inside_the_board(new_coords):
                move_array.append(new_coords)

    def __get_front_moves(self, move_array, player, piece, piece_index, val):
        for x in range(-1, 2):
            new_coords = player.get_coords(piece, piece_index, x, val)
            if self.__inside_the_board(new_coords):
                move_array.append(new_coords)
        return move_array

    def __inside_the_board(self, new_coords):
        return new_coords[0] >= 0 and new_coords[0] <= 8 and new_coords[1] <= 8 and new_coords[1] >= 0
        