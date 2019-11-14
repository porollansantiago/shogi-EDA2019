

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
                move_array.append([player.coords[piece_to_move][0], player.coords[piece_to_move][1] - 1])
            elif "L" in piece_to_move:
                end, step = -1, -1
                move_array = self.get_lance_moves(piece_to_move, move_array, end, step, player, other_player)
            elif "KN" in piece_to_move:
                move_array.append([player.coords[piece_to_move][0] - 1, player.coords[piece_to_move][1] - 2])
                move_array.append([player.coords[piece_to_move][0] + 1, player.coords[piece_to_move][1] - 2])
        elif turn == "white":
            if "P" in piece_to_move:
                move_array.append([player.coords[piece_to_move][0], player.coords[piece_to_move][1] + 1])
            elif "L" in piece_to_move:
                end, step = 9, 1
                move_array = self.get_lance_moves(piece_to_move, move_array, end, step, player, other_player)
            elif "KN" in piece_to_move:
                move_array.append([player.coords[piece_to_move][0] - 1, player.coords[piece_to_move][1] + 2])
                move_array.append([player.coords[piece_to_move][0] + 1, player.coords[piece_to_move][1] + 2])

        return move_array


    def get_lance_moves(self, piece, move_array, end, step, player, other_player):
        for val in range(player.coords[piece][1], end, step):
            if [player.coords[piece][0], player.coords[piece][1] + val] not in other_player.coords.items():
                move_array.append([player.coords[piece][0], val])
        print(move_array)
        return move_array
