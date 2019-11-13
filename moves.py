

class Moves():
    def __init__(self):
        pass

    def validate(self, turn, piece_to_move, new_coords, black, white):
        if turn == "black":
            if self.validate_player(turn, piece_to_move, new_coords, black):
                return False
        elif turn == "white":
            if self.validate_player(turn, piece_to_move, new_coords, white):
                return False
        return True

    def validate_player(self, turn, piece_to_move, new_coords, player):
        if self.__overlapping(new_coords, player):
            return True
        if new_coords not in self.get_move_array(turn, piece_to_move, new_coords, player):
            return True
        return False

    def __overlapping(self, new_coords, player):
        for piece in player.coords.keys():
            if new_coords == player.coords[piece]:
                return True
        return False

    def get_move_array(self, turn, piece_to_move, new_coords, player):
        move_array = []
        if turn == "black" and "P" in piece_to_move:
            move_array.append([player.coords[piece_to_move][0], player.coords[piece_to_move][1] - 1])
        elif turn == "white" and "P" in piece_to_move:
            move_array.append([player.coords[piece_to_move][0], player.coords[piece_to_move][1] + 1])

        return move_array
