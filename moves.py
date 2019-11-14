

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
                move_array = self.get_SG_moves(move_array, 1)
        elif turn == "white":
            if "P" in piece_to_move:
                move_array.append(player.get_coords(piece_to_move, 0, 1))
            elif "L" in piece_to_move:
                end, step = 9, 1
                move_array = self.get_lance_moves(piece_to_move, move_array, end, step, player, other_player)
            elif "KN" in piece_to_move:
                move_array = self.get_knight_moves(player, piece_to_move, move_array, 2)
        print(move_array)
        return move_array


    def get_lance_moves(self, piece, move_array, end, step, player, other_player):
        for val in range(player.coords[piece][1], end, step):
            new_coords = player.get_coords(piece, 0, val, False, True)
            if new_coords not in other_player.coords.items():
                if self.__inside_the_board(new_coords):
                    move_array.append(player.get_coords(piece, 0, val, False, True))
        return move_array

    def get_knight_moves(self, player, piece, move_array, y):
        for x in range(-1, 2, 2):
            new_coords = player.get_coords(piece, x, y)
            if self.__inside_the_board(new_coords):
                move_array.append(new_coords)
        return move_array

    def get_SG_moves(self, move_array, val):
        return move_array

    def __inside_the_board(self, new_coords):
        return new_coords[0] >= 0 and new_coords[0] <= 8 and new_coords[1] <= 8 and new_coords[1] >= 0
        