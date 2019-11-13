

class Moves():
    def __init__(self):
        pass

    def validate(self, turn, piece_to_move, new_coords, black, white):
        if turn == "black" and self.__overlapping(new_coords, black):
            return False
        elif turn == "white" and self.__overlapping(new_coords, white):
            return False
        return True

    def __overlapping(self, new_coords, player):
        for piece in player.coords.keys():
            if new_coords == player.coords[piece]:
                return True
        return False
