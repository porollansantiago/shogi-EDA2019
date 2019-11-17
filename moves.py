

class Moves():
    def validate(self, turn, piece_to_move, piece_index, x, y, black, white, move_array=None):
        if [x, y] == [10, 4] or [x, y] == [12, 4]:
            return False
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
        try:
            return [x, y] not in move_array
        except TypeError:
            return True

    def get_move_array(self, turn, piece, piece_index, x, y, player, other_player):
        move_array = []
        all_player_coords = player.get_all_coords()
        if x > 9:
            return self.get_empty_spaces(player, other_player, piece)
        if turn == "black":
            move_array = self.black_side_moves(turn, piece, piece_index, player, other_player, move_array, all_player_coords)
        elif turn == "white":
            move_array = self.white_side_moves(turn, piece, piece_index, player, other_player, move_array, all_player_coords)
        return move_array

    def black_side_moves(self, turn, piece, piece_index, player, other_player, move_array, all_player_coords):
        if " P " == piece:
            new_coords = player.get_coords(piece, piece_index, 0, -1)
            if self.__inside_the_board(new_coords) and new_coords not in all_player_coords:
                return [new_coords]
        elif " L " == piece:
            end, step = -1, -1
            return self.get_lance_moves(piece, piece_index, move_array, end, step, player, other_player, all_player_coords)
        elif "KN " == piece:
            return self.get_knight_moves(player, piece, piece_index, move_array, -2, all_player_coords)
        elif "SG " == piece:
            return self.get_SG_moves(player, piece, piece_index, move_array, -1, all_player_coords)
        elif piece in ["GG ", "PP ", "PKN", "PSG", "PL "]:
            return self.get_GG_moves(player, piece, piece_index, move_array, -1, 1, all_player_coords)
        elif "R" in piece:
            return self.get_rook_moves(player, other_player, piece, piece_index, move_array, all_player_coords)
        elif "B" in piece:
            return self.get_bishop_moves(player, other_player, piece, piece_index, move_array, all_player_coords)
        elif " K " == piece:
            return self.get_king_moves(player, piece, piece_index, move_array, all_player_coords)

    def white_side_moves(self, turn, piece, piece_index, player, other_player, move_array, all_player_coords):
        if " P " == piece:
            new_coords = player.get_coords(piece, piece_index, 0, 1)
            if self.__inside_the_board(new_coords) and new_coords not in all_player_coords:
                return [new_coords]
        elif " L " == piece:
            end, step = 9, 1
            return self.get_lance_moves(piece, piece_index, move_array, end, step, player, other_player, all_player_coords)
        elif "KN " == piece:
            return self.get_knight_moves(player, piece, piece_index, move_array, 2, all_player_coords)
        elif "SG " == piece:
            return self.get_SG_moves(player, piece, piece_index, move_array, 1, all_player_coords)
        elif piece in ["GG ", "PP ", "PKN", "PSG", "PL "]:
            return self.get_GG_moves(player, piece, piece_index, move_array, 1, -1, all_player_coords)
        elif "R" in piece:
            return self.get_rook_moves(player, other_player, piece, piece_index, move_array, all_player_coords)
        elif "B" in piece:
            return self.get_bishop_moves(player, other_player, piece, piece_index, move_array, all_player_coords)
        elif " K " == piece:
            return self.get_king_moves(player, piece, piece_index, move_array, all_player_coords)

    def get_lance_moves(self, piece, piece_index, move_array, end, step, player, other_player, all_player_coords):
        for val in range(player.coords[piece][piece_index][1] + step, end, step):
            new_coords = player.get_coords(piece, piece_index, 0, val, False, True)
            if self.__inside_the_board(new_coords):
                if new_coords not in all_player_coords:
                    move_array.append(player.get_coords(piece, piece_index, 0, val, False, True))
            if player.compare_coords(new_coords) or other_player.compare_coords(new_coords):
                break
        return move_array

    def get_knight_moves(self, player, piece, piece_index, move_array, y, all_player_coords):
        for x in range(-1, 2, 2):
            new_coords = player.get_coords(piece, piece_index, x, y)
            if self.__inside_the_board(new_coords) and new_coords not in all_player_coords:
                if new_coords not in all_player_coords:
                    move_array.append(new_coords)
        return move_array

    def get_SG_moves(self, player, piece, piece_index, move_array, val, all_player_coords):
        self.__get_front_moves(move_array, player, piece, piece_index, val, all_player_coords)
        self.__get_side_moves(move_array, player, piece, piece_index, val, all_player_coords)
        return move_array

    def get_GG_moves(self, player, piece, piece_index, move_array, front_val, back_val, all_player_coords):
        self.__get_front_moves(move_array, player, piece, piece_index, front_val, all_player_coords)
        self.__get_side_moves(move_array, player, piece, piece_index, 0, all_player_coords)
        new_coord = player.get_coords(piece, piece_index, 0, back_val)
        if self.__inside_the_board(new_coord) and new_coord not in all_player_coords:
            move_array.append(new_coord)
        return move_array

    def get_king_moves(self, player, piece, piece_index, move_array, all_player_coords):
        self.__get_front_moves(move_array, player, piece, piece_index, 1, all_player_coords)
        self.__get_front_moves(move_array, player, piece, piece_index, -1, all_player_coords)
        self.__get_side_moves(move_array, player, piece, piece_index, 0, all_player_coords)
        return move_array

    def get_rook_moves(self, player, other_player, piece, piece_index, move_array, all_player_coords):
        coords = player.get_coords(piece, piece_index)
        self.__get_rook_col(coords, player, piece, piece_index, move_array, other_player, all_player_coords)
        self.__get_rook_row(coords, player, piece, piece_index, move_array, other_player, all_player_coords)
        if "PR " == piece:
            for val in [-1, 1]:
                new_coords1 = player.get_coords(piece, piece_index, val, val)
                new_coords2 = player.get_coords(piece, piece_index, -val, val)
                if self.__inside_the_board(new_coords1) and new_coords1 not in all_player_coords:
                    move_array.append(new_coords1)
                if self.__inside_the_board(new_coords2) and new_coords2 not in all_player_coords:
                    move_array.append(new_coords2)
        return move_array

    def get_bishop_moves(self, player, other_player, piece, piece_index, move_array, all_player_coords):
        coords = player.get_coords(piece, piece_index)
        start1 = coords[0] if coords[0] > coords[1] else coords[1]
        for val in range(1, 9 - start1):
            new_coords = player.get_coords(piece, piece_index, val, val)
            if new_coords not in all_player_coords:
                move_array.append(new_coords)
            if player.compare_coords(new_coords) or other_player.compare_coords(new_coords):
                break
        start2 = coords[0] if coords[0] < coords[1] else coords[1]
        for val in range(start2, -1, -1):
            new_coords = player.get_coords(piece, piece_index, -val, -val)
            if new_coords not in all_player_coords:
                move_array.append(new_coords)
            if player.compare_coords(new_coords) or other_player.compare_coords(new_coords):
                break
        start3 = 8 - coords[0] if 8 - coords[0] < coords[1] else coords[1]
        for val in range(1, start3 + 1):
            new_coords = player.get_coords(piece, piece_index, val, -val)
            if new_coords not in all_player_coords:
                move_array.append(new_coords)
            if player.compare_coords(new_coords) or other_player.compare_coords(new_coords):
                break
        start4 = 8 - coords[1] if 8 - coords[1] < coords[0] else coords[0]
        for val in range(1, start4 + 1):
            new_coords = player.get_coords(piece, piece_index, -val, val)
            if new_coords not in all_player_coords:
                move_array.append(new_coords)
            if player.compare_coords(new_coords) or other_player.compare_coords(new_coords):
                break
        if "PB " == piece:
            for val in [-1, 1]:
                new_coords1 = player.get_coords(piece, piece_index, val)
                new_coords2 = player.get_coords(piece, piece_index, 0, val)
                if self.__inside_the_board(new_coords1) and new_coords1 not in all_player_coords:
                    move_array.append(new_coords1)
                if self.__inside_the_board(new_coords2) and new_coords2 not in all_player_coords:
                    move_array.append(new_coords2)
        return move_array                

    def __get_rook_col(self, coords, player, piece, piece_index, move_array, other_player, all_player_coords):
        for val in range(coords[1] + 1, 9):
            new_coords = player.get_coords(piece, piece_index, 0, val, False, True)
            if new_coords not in all_player_coords:
                move_array.append(new_coords)
            if player.compare_coords(new_coords) or other_player.compare_coords(new_coords):
                break
        for val in range(coords[1] - 1, -1, -1):
            new_coords = player.get_coords(piece, piece_index, 0, val, False, True)
            if new_coords not in all_player_coords:
                move_array.append(new_coords)
            if player.compare_coords(new_coords) or other_player.compare_coords(new_coords):
                break

    def __get_rook_row(self, coords, player, piece, piece_index, move_array, other_player, all_player_coords):
        for val in range(coords[0] + 1, 9):
            new_coords = player.get_coords(piece, piece_index, val, 0, True)
            if new_coords not in all_player_coords:
                move_array.append(new_coords)
            if player.compare_coords(new_coords) or other_player.compare_coords(new_coords):
                break
        for val in range(coords[0] - 1, -1, -1):
            new_coords = player.get_coords(piece, piece_index, val, 0, True)
            if new_coords not in all_player_coords:
                move_array.append(new_coords)
            if player.compare_coords(new_coords) or other_player.compare_coords(new_coords):
                break

    def __get_side_moves(self, move_array, player, piece, piece_index, val, all_player_coords):
        for x in range(-1, 2, 2):
            new_coords = player.get_coords(piece, piece_index, x, -val)
            if self.__inside_the_board(new_coords) and new_coords:
                if new_coords not in all_player_coords:
                    move_array.append(new_coords)

    def __get_front_moves(self, move_array, player, piece, piece_index, val, all_player_coords):
        for x in range(-1, 2):
            new_coords = player.get_coords(piece, piece_index, x, val)
            if self.__inside_the_board(new_coords) and new_coords:
                if new_coords not in all_player_coords:
                    move_array.append(new_coords)


    def __inside_the_board(self, new_coords):
        return new_coords[0] >= 0 and new_coords[0] <= 8 and new_coords[1] <= 8 and new_coords[1] >= 0

    def get_empty_spaces(self, player, other_player, piece):
        move_array = []
        p = []
        pawn_columns = []
        if piece == " P ":
            for x in player.get_pawn_cols():
                pawn_columns.append(x)
        
        for coord in player.get_all_coords():
            p.append(coord)
        for coord in other_player.get_all_coords():
            p.append(coord)
        for x in range(9):
            for y in range(9):
                if [x, y] not in p:
                    if x not in pawn_columns:
                        move_array.append([x, y])
        return move_array

    def get_all_player_moves(self, turn, player, opponent):
        move_array = []
        for piece in player.coords:
            for idx, coord in enumerate(player.coords[piece]):
                try:
                    for move in self.get_move_array(turn, piece, idx, coord[0], coord[1], player, opponent):
                        move_array.append(move)
                except TypeError:
                    pass
        return move_array
