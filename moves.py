

class Moves():
    def validate(self, turn, piece_to_move, piece_index, x, y, black, white,
                 move_array=None, check=False, safe_moves={}):
        if [x, y] == [10, 4] or [x, y] == [12, 4]:
            return False
        if turn == "black":
            if self.validate_player(turn, piece_to_move, piece_index, x, y,
                                    black, white, move_array,
                                    check, safe_moves):
                return False
        elif turn == "white":
            if self.validate_player(turn, piece_to_move, piece_index, x, y,
                                    white, black, move_array,
                                    check, safe_moves):
                return False
        return True

    def validate_player(self, turn, piece_to_move, piece_index, x, y, player,
                        other_player, move_array, check, safe_moves):
        if not move_array:
            move_array = self.get_move_array(turn, piece_to_move, piece_index,
                                             x, y, player, other_player,
                                             check, safe_moves)
        try:
            return [x, y] not in move_array
        except TypeError:
            return True

    def get_move_array(self, turn, piece, piece_index, x, y,
                       player, other_player, check=False, safe_moves={},
                       possible_check=False, check_moves={}):
        move_array = []
        all_player_coords = player.get_all_coords()
        if not piece:
            return []
        if turn == "black":
            move_array = self.black_side_moves(turn, piece, piece_index,
                                               player, other_player,
                                               move_array, all_player_coords,
                                               check, safe_moves,
                                               possible_check, check_moves,
                                               x, y)
        elif turn == "white":
            move_array = self.white_side_moves(turn, piece, piece_index,
                                               player, other_player,
                                               move_array, all_player_coords,
                                               check, safe_moves,
                                               possible_check, check_moves,
                                               x, y)
        return move_array

    def black_side_moves(self, turn, piece, piece_index, player, other_player,
                         move_array, all_player_coords, check, safe_moves,
                         possible_check, check_moves, x, y):
        current_coords = player.get_coords(piece, piece_index)
        if current_coords[0] > 9 and current_coords[1] == 8:
            return self.get_empty_spaces(turn, player, other_player, piece,
                                         piece_index, check, safe_moves,
                                         possible_check, check_moves)
        if " P " == piece:
            new_coords = player.get_coords(piece, piece_index, 0, -1)
            if self.__inside_the_board(new_coords):
                if new_coords not in all_player_coords and ((not check) or (
                        new_coords in safe_moves[(piece, piece_index)])) and(
                            (not possible_check) or (
                                new_coords not in
                                check_moves[(piece, piece_index)])):
                    return [new_coords]
        elif " L " == piece:
            end, step = -1, -1
            return self.get_lance_moves(piece, piece_index, move_array, end,
                                        step, player, other_player,
                                        all_player_coords, check, safe_moves,
                                        possible_check, check_moves)
        elif "KN " == piece:
            return self.get_knight_moves(player, piece, piece_index,
                                         move_array, -2, all_player_coords,
                                         check, safe_moves, possible_check,
                                         check_moves)
        elif "SG " == piece:
            return self.get_SG_moves(player, piece, piece_index, move_array,
                                     -1, all_player_coords, check, safe_moves,
                                     possible_check, check_moves)
        elif piece in ["GG ", "PP ", "PKN", "PSG", "PL "]:
            return self.get_GG_moves(player, piece, piece_index, move_array,
                                     -1, 1, all_player_coords, check,
                                     safe_moves, possible_check, check_moves)
        elif "R" in piece:
            return self.get_rook_moves(player, other_player, piece,
                                       piece_index, move_array,
                                       all_player_coords, check, safe_moves,
                                       possible_check, check_moves)
        elif "B" in piece:
            return self.get_bishop_moves(player, other_player, piece,
                                         piece_index, move_array,
                                         all_player_coords, check, safe_moves,
                                         possible_check, check_moves)
        elif " K " == piece:
            return self.get_king_moves(player, piece, piece_index, move_array,
                                       all_player_coords, check, safe_moves,
                                       possible_check, check_moves)

    def white_side_moves(self, turn, piece, piece_index, player, other_player,
                         move_array, all_player_coords, check, safe_moves,
                         possible_check, check_moves, x, y):
        current_coords = player.get_coords(piece, piece_index)
        if current_coords[0] > 9 and current_coords[1] == 0:
            return self.get_empty_spaces(turn, player, other_player, piece,
                                         piece_index, check, safe_moves,
                                         possible_check, check_moves)
        if " P " == piece:
            new_coords = player.get_coords(piece, piece_index, 0, 1)
            if self.__inside_the_board(new_coords):
                if new_coords not in all_player_coords and ((not check) or (
                        new_coords in safe_moves[(piece, piece_index)])) and(
                            (not possible_check) or (
                                new_coords not in
                                check_moves[(piece, piece_index)])):
                    return [new_coords]
        elif " L " == piece:
            end, step = 9, 1
            return self.get_lance_moves(piece, piece_index, move_array, end,
                                        step, player, other_player,
                                        all_player_coords, check, safe_moves,
                                        possible_check, check_moves)
        elif "KN " == piece:
            return self.get_knight_moves(player, piece, piece_index,
                                         move_array, 2, all_player_coords,
                                         check, safe_moves, possible_check,
                                         check_moves)
        elif "SG " == piece:
            return self.get_SG_moves(player, piece, piece_index, move_array, 1,
                                     all_player_coords, check, safe_moves,
                                     possible_check, check_moves)
        elif piece in ["GG ", "PP ", "PKN", "PSG", "PL "]:
            return self.get_GG_moves(player, piece, piece_index, move_array, 1,
                                     -1, all_player_coords, check, safe_moves,
                                     possible_check, check_moves)
        elif "R" in piece:
            return self.get_rook_moves(player, other_player, piece,
                                       piece_index, move_array,
                                       all_player_coords, check, safe_moves,
                                       possible_check, check_moves)
        elif "B" in piece:
            return self.get_bishop_moves(player, other_player, piece,
                                         piece_index, move_array,
                                         all_player_coords, check, safe_moves,
                                         possible_check, check_moves)
        elif " K " == piece:
            return self.get_king_moves(player, piece, piece_index, move_array,
                                       all_player_coords, check, safe_moves,
                                       possible_check, check_moves)

    def get_lance_moves(self, piece, piece_index, move_array, end, step,
                        player, other_player, all_player_coords, check,
                        safe_moves, possible_check, check_moves):
        for val in range(player.coords[piece][piece_index][1] + step,
                         end, step):
            new_coords = player.get_coords(
                piece, piece_index, 0, val, False, True)
            if self.__inside_the_board(new_coords):
                if new_coords not in all_player_coords and ((not check) or (
                        new_coords in safe_moves[(piece, piece_index)])) and(
                            (not possible_check) or (
                                new_coords not in
                                check_moves[(piece, piece_index)])):
                    move_array.append(new_coords)
            if player.compare_coords(new_coords) or (
               other_player.compare_coords(new_coords)):
                break
        return move_array

    def get_knight_moves(self, player, piece, piece_index, move_array, y,
                         all_player_coords, check, safe_moves,
                         possible_check, check_moves):
        for x in range(-1, 2, 2):
            new_coords = player.get_coords(piece, piece_index, x, y)
            if self.__inside_the_board(new_coords):
                if new_coords not in all_player_coords and ((not check) or (
                        new_coords in safe_moves[(piece, piece_index)])) and(
                            (not possible_check) or (
                                new_coords not in
                                check_moves[(piece, piece_index)])):
                    move_array.append(new_coords)
        return move_array

    def get_SG_moves(self, player, piece, piece_index, move_array, val,
                     all_player_coords, check, safe_moves,
                     possible_check, check_moves):
        self.__get_front_moves(move_array, player, piece, piece_index, val,
                               all_player_coords, check, safe_moves,
                               possible_check, check_moves)
        self.__get_side_moves(move_array, player, piece, piece_index, val,
                              all_player_coords, check, safe_moves,
                              possible_check, check_moves)
        return move_array

    def get_GG_moves(self, player, piece, piece_index, move_array, front_val,
                     back_val, all_player_coords, check, safe_moves,
                     possible_check, check_moves):
        self.__get_front_moves(move_array, player, piece, piece_index,
                               front_val, all_player_coords, check, safe_moves,
                               possible_check, check_moves)
        self.__get_side_moves(move_array, player, piece, piece_index, 0,
                              all_player_coords, check, safe_moves,
                              possible_check, check_moves)
        new_coords = player.get_coords(piece, piece_index, 0, back_val)
        if self.__inside_the_board(new_coords):
            if new_coords not in all_player_coords and ((not check) or (
                    new_coords in safe_moves[(piece, piece_index)])) and(
                        (not possible_check) or (
                            new_coords not in
                            check_moves[(piece, piece_index)])):
                move_array.append(new_coords)
        return move_array

    def get_king_moves(self, player, piece, piece_index, move_array,
                       all_player_coords, check, safe_moves,
                       possible_check, check_moves):
        self.__get_front_moves(move_array, player, piece, piece_index, 1,
                               all_player_coords, check, safe_moves,
                               possible_check, check_moves)
        self.__get_front_moves(move_array, player, piece, piece_index, -1,
                               all_player_coords, check, safe_moves,
                               possible_check, check_moves)
        self.__get_side_moves(move_array, player, piece, piece_index, 0,
                              all_player_coords, check, safe_moves,
                              possible_check, check_moves)
        return move_array

    def get_rook_moves(self, player, other_player, piece, piece_index,
                       move_array, all_player_coords, check, safe_moves,
                       possible_check, check_moves):
        coords = player.get_coords(piece, piece_index)
        self.__get_rook_col(coords, player, piece, piece_index, move_array,
                            other_player, all_player_coords, check, safe_moves,
                            possible_check, check_moves)
        self.__get_rook_row(coords, player, other_player, piece, piece_index,
                            move_array, all_player_coords, check, safe_moves,
                            possible_check, check_moves)

        if "PR " == piece:
            for val in [-1, 1]:
                new_coords1 = player.get_coords(piece, piece_index, val, val)
                new_coords2 = player.get_coords(piece, piece_index, -val, val)
                if self.__inside_the_board(new_coords1):
                    if new_coords1 not in all_player_coords and ((not check)or(
                          new_coords1 in safe_moves[(piece, piece_index)]))and(
                                (not possible_check) or (
                                    new_coords1 not in
                                    check_moves[(piece, piece_index)])):
                        move_array.append(new_coords1)
                if self.__inside_the_board(new_coords1):
                    if new_coords2 not in all_player_coords and ((not check)or(
                          new_coords2 in safe_moves[(piece, piece_index)]))and(
                                (not possible_check) or (
                                    new_coords2 not in
                                    check_moves[(piece, piece_index)])):
                        move_array.append(new_coords2)
        return move_array

    def get_bishop_moves(self, player, other_player, piece, piece_index,
                         move_array, all_player_coords, check, safe_moves,
                         possible_check, check_moves):
        coords = player.get_coords(piece, piece_index)
        start1 = coords[0] if coords[0] > coords[1] else coords[1]
        for val in range(1, 9 - start1):
            new_coords = player.get_coords(piece, piece_index, val, val)
            if new_coords not in all_player_coords and ((not check) or (
                    new_coords in safe_moves[(piece, piece_index)])) and(
                        (not possible_check) or (
                            new_coords not in
                            check_moves[(piece, piece_index)])):
                move_array.append(new_coords)
            if player.compare_coords(new_coords) or (
               other_player.compare_coords(new_coords)):
                break
        start2 = coords[0] if coords[0] < coords[1] else coords[1]
        for val in range(1, start2 + 1):
            new_coords = player.get_coords(piece, piece_index, -val, -val)
            if new_coords not in all_player_coords and ((not check) or (
                    new_coords in safe_moves[(piece, piece_index)])) and(
                        (not possible_check) or (
                            new_coords not in
                            check_moves[(piece, piece_index)])):
                move_array.append(new_coords)
            if player.compare_coords(new_coords) or (
               other_player.compare_coords(new_coords)):
                break
        start3 = 8 - coords[0] if 8 - coords[0] < coords[1] else coords[1]
        for val in range(1, start3 + 1):
            new_coords = player.get_coords(piece, piece_index, val, -val)
            if new_coords not in all_player_coords and ((not check) or (
                    new_coords in safe_moves[(piece, piece_index)])) and(
                        (not possible_check) or (
                            new_coords not in
                            check_moves[(piece, piece_index)])):
                move_array.append(new_coords)
            if player.compare_coords(new_coords) or (
               other_player.compare_coords(new_coords)):
                break
        start4 = 8 - coords[1] if 8 - coords[1] < coords[0] else coords[0]
        for val in range(1, start4 + 1):
            new_coords = player.get_coords(piece, piece_index, -val, val)
            if new_coords not in all_player_coords and ((not check) or (
                    new_coords in safe_moves[(piece, piece_index)])) and(
                        (not possible_check) or (
                            new_coords not in
                            check_moves[(piece, piece_index)])):
                move_array.append(new_coords)
            if player.compare_coords(new_coords) or (
               other_player.compare_coords(new_coords)):
                break
        if "PB " == piece:
            for val in [-1, 1]:
                new_coords1 = player.get_coords(piece, piece_index, val)
                new_coords2 = player.get_coords(piece, piece_index, 0, val)
                if self.__inside_the_board(new_coords1):
                    if new_coords1 not in all_player_coords and ((not check)or(
                          new_coords1 in safe_moves[(piece, piece_index)]))and(
                                (not possible_check) or (
                                    new_coords1 not in
                                    check_moves[(piece, piece_index)])):
                        move_array.append(new_coords1)
                if self.__inside_the_board(new_coords2):
                    if new_coords2 not in all_player_coords and ((not check)or(
                          new_coords2 in safe_moves[(piece, piece_index)]))and(
                                (not possible_check) or (
                                    new_coords2 not in
                                    check_moves[(piece, piece_index)])):
                        move_array.append(new_coords2)
        return move_array

    def __get_rook_col(self, coords, player, piece, piece_index, move_array,
                       opponent, all_player_coords, check, safe_moves,
                       possible_check, check_moves):
        for val in range(coords[1] + 1, 9):
            new_coords = player.get_coords(
                piece, piece_index, 0, val, False, True)
            if new_coords not in all_player_coords and ((not check) or (
                    new_coords in safe_moves[(piece, piece_index)])) and(
                        (not possible_check) or (
                            new_coords not in
                            check_moves[(piece, piece_index)])):
                move_array.append(new_coords)
            if player.compare_coords(new_coords) or (
               opponent.compare_coords(new_coords)):
                break
        for val in range(coords[1] - 1, -1, -1):
            new_coords = player.get_coords(
                piece, piece_index, 0, val, False, True)
            if new_coords not in all_player_coords and ((not check) or (
                    new_coords in safe_moves[(piece, piece_index)])) and(
                        (not possible_check) or (
                            new_coords not in
                            check_moves[(piece, piece_index)])):
                move_array.append(new_coords)
            if player.compare_coords(new_coords) or (
               opponent.compare_coords(new_coords)):
                break

    def __get_rook_row(self, coords, player, opponent, piece, piece_index,
                       move_array, all_player_coords, check, safe_moves,
                       possible_check, check_moves):
        self.__rook_row_right(coords, player, opponent, piece, piece_index,
                              all_player_coords, check, safe_moves,
                              possible_check, check_moves, move_array)
        self.__rook_row_left(coords, player, opponent, piece, piece_index,
                             all_player_coords, check, safe_moves,
                             possible_check, check_moves, move_array)

    def __rook_row_right(self, coords, player, opponent, piece, piece_index,
                         all_player_coords, check, safe_moves,
                         possible_check, check_moves, move_array):
        for val in range(coords[0] + 1, 9):
            new_coords = player.get_coords(piece, piece_index, val, 0, True)
            if new_coords not in all_player_coords and ((not check) or (
                    new_coords in safe_moves[(piece, piece_index)])) and(
                        (not possible_check) or (
                            new_coords not in
                            check_moves[(piece, piece_index)])):
                move_array.append(new_coords)
            if player.compare_coords(new_coords) or (
               opponent.compare_coords(new_coords)):
                break

    def __rook_row_left(self, coords, player, opponent, piece, piece_index,
                        all_player_coords, check, safe_moves,
                        possible_check, check_moves, move_array):
        for val in range(coords[0] - 1, -1, -1):
            new_coords = player.get_coords(piece, piece_index, val, 0, True)
            if new_coords not in all_player_coords:
                if ((not check) or (new_coords in
                                    safe_moves[(piece, piece_index)])):
                    if ((not possible_check) or (new_coords not in
                                                 check_moves[(piece,
                                                              piece_index)])):
                        move_array.append(new_coords)
            if player.compare_coords(new_coords) or (
                    opponent.compare_coords(new_coords)):
                break

    def __get_side_moves(self, move_array, player, piece, piece_index, val,
                         all_player_coords, check, safe_moves, possible_check,
                         check_moves):
        for x in range(-1, 2, 2):
            new_coords = player.get_coords(piece, piece_index, x, -val)
            if self.__inside_the_board(new_coords) and new_coords:
                if new_coords not in all_player_coords and ((not check) or (
                        new_coords in safe_moves[(piece, piece_index)])) and(
                            (not possible_check) or (
                                new_coords not in
                                check_moves[(piece, piece_index)])):
                    move_array.append(new_coords)

    def __get_front_moves(self, move_array, player, piece, piece_index, val,
                          all_player_coords, check, safe_moves,
                          possible_check, check_moves):
        for x in range(-1, 2):
            new_coords = player.get_coords(piece, piece_index, x, val)
            if self.__inside_the_board(new_coords) and new_coords:
                if new_coords not in all_player_coords and ((not check) or (
                        new_coords in safe_moves[(piece, piece_index)])) and(
                            (not possible_check) or (
                                new_coords not in
                                check_moves[(piece, piece_index)])):
                    move_array.append(new_coords)

    def __inside_the_board(self, new_coords):
        return new_coords[0] >= 0 and (
                new_coords[0] <= 8) and (
                new_coords[1] <= 8 and new_coords[1] >= 0)

    def get_empty_spaces(self, turn, player, opponent, piece, piece_index,
                         check, safe_moves, possible_check, check_moves):
        occupied = []
        pawn_columns = []
        if piece == " P ":
            self.__pawn_columns(turn, player, opponent, pawn_columns, occupied)
        if piece in [" P ", " L "]:
            self.__pawn_lance_opposite_line(turn, occupied)
        elif piece == "KN ":
            self.__knight_opposite_lines(turn, occupied)
        self.__empty_spaces(player, opponent, occupied)
        return self.__get_moves(occupied, pawn_columns, piece, piece_index,
                                check, safe_moves, possible_check, check_moves)

    def __pawn_columns(self, turn, player, opponent, pawn_columns, occupied):
        try:
            king_coords = opponent.get_coords(" K ", 0)
        except KeyError:
            pass
        else:
            if turn == "white":
                king_coords[1] -= 1
            elif turn == "black":
                king_coords[1] += 1
            occupied.append(king_coords)
        for x in player.get_pawn_cols():
            pawn_columns.append(x)

    def __pawn_lance_opposite_line(self, turn, occupied):
        op_side = 0 if turn == "black" else 8
        for x in range(9):
            occupied.append([x, op_side])

    def __knight_opposite_lines(self, turn, occupied):
        start = 0 if turn == "black" else 7
        for y in range(start, start + 2):
            for x in range(9):
                occupied.append([x, y])

    def __empty_spaces(self, player, opponent, occupied):
        for coord in player.get_all_coords():
            occupied.append(coord)
        for coord in opponent.get_all_coords():
            occupied.append(coord)

    def __get_moves(self, occupied, pawn_columns, piece, piece_index, check,
                    safe_moves, possible_check, check_moves):
        move_array = []
        for x in range(9):
            for y in range(9):
                if [x, y] not in occupied and (
                  ((not check) or ([x, y] in safe_moves[(piece, piece_index)]))
                  and
                  ((not possible_check) or (
                   ([x, y] not in check_moves[(piece, piece_index)]))) and (
                        x not in pawn_columns)):
                    move_array.append([x, y])
        return move_array

    def get_all_player_moves(self, turn, player, opponent):
        move_array = []
        for piece in player.coords.keys():
            for idx, coord in enumerate(player.coords[piece]):
                try:
                    for move in self.get_move_array(turn, piece, idx,
                                                    coord[0], coord[1],
                                                    player, opponent):
                        move_array.append(move)
                except TypeError:
                    pass
        return move_array
