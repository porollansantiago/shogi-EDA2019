from board import Board


class Api:
    def __init__(self):
        self.board = Board()

    def get_board(self):
        board = self.board.make_board()
        new_board = ""
        for line in board:
            new_board += "".join(line) + "\n"
        return new_board

    def play(self, coords_i):
        if " " in coords_i:
            coords = coords_i.split()
        else:
            coords = coords_i
        try:
            coords = [int(coords[0]), int(coords[1])]
        except ValueError:
            return (self.get_board(), "solo se permiten numeros")
        except IndexError:
            return(self.get_board(), "")
        move_array = self.board.play(coords[0], coords[1])
        move_array = "" if not move_array else move_array
        return (self.get_board(), move_array)
