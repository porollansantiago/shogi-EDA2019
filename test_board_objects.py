import unittest
import coordinates as coords
from parameterized import parameterized
from board_objects import Board_objects

class Test_board_objects(unittest.TestCase):
    
    def setUp(self):
        self.board = [["   " for _ in range(9)], ["   " for _ in range(9)],
                      ["   " for _ in range(9)], ["   " for _ in range(9)],
                      ["   " for _ in range(9)], ["   " for _ in range(9)],
                      ["   " for _ in range(9)], ["   " for _ in range(9)],
                      ["   " for _ in range(9)]]

    @parameterized.expand([
        (coords.black, [['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '], 
                        ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '], 
                        ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '], 
                        ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '], 
                        ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '], 
                        ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '], 
                        ['P1 ', 'P2 ', 'P3 ', 'P4 ', 'P5 ', 'P6 ', 'P7 ', 'P8 ', 'P9 '], 
                        ['   ', ' B ', '   ', '   ', '   ', '   ', '   ', ' R ', '   '], 
                        ['L1 ', 'KN1', 'SG1', 'GG1', ' K ', 'GG2', 'SG2', 'KN2', 'L2 ']]),

        (coords.white, [['L2 ', 'KN2', 'SG2', 'GG2', ' K ', 'GG1', 'SG1', 'KN1', 'L1 '], 
                        ['   ', ' R ', '   ', '   ', '   ', '   ', '   ', ' B ', '   '], 
                        ['P9 ', 'P8 ', 'P7 ', 'P6 ', 'P5 ', 'P4 ', 'P3 ', 'P2 ', 'P1 '], 
                        ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '], 
                        ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '], 
                        ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '], 
                        ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '], 
                        ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '], 
                        ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ']])
    ])
    def test_add_to_board(self, coords, new_board):
        board_objects = Board_objects(coords)
        self.assertEqual(board_objects.add_to_board(self.board), new_board)

    @parameterized.expand([
        (coords.black, 'P1 ', [0, 5], [['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '], 
                                       ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '], 
                                       ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '], 
                                       ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '], 
                                       ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '], 
                                       ['P1 ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '], 
                                       ['   ', 'P2 ', 'P3 ', 'P4 ', 'P5 ', 'P6 ', 'P7 ', 'P8 ', 'P9 '], 
                                       ['   ', ' B ', '   ', '   ', '   ', '   ', '   ', ' R ', '   '], 
                                       ['L1 ', 'KN1', 'SG1', 'GG1', ' K ', 'GG2', 'SG2', 'KN2', 'L2 ']]),

        (coords.white, 'P1 ', [8, 3], [['L2 ', 'KN2', 'SG2', 'GG2', ' K ', 'GG1', 'SG1', 'KN1', 'L1 '], 
                                       ['   ', ' R ', '   ', '   ', '   ', '   ', '   ', ' B ', '   '], 
                                       ['P9 ', 'P8 ', 'P7 ', 'P6 ', 'P5 ', 'P4 ', 'P3 ', 'P2 ', '   '], 
                                       ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', 'P1 '], 
                                       ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '], 
                                       ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '], 
                                       ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '], 
                                       ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '], 
                                       ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ']])
    ])
    def test_move(self, coords, piece_to_move, new_coords, new_board):
        board_objects = Board_objects(coords)
        board_objects.move(piece_to_move, new_coords[0], new_coords[1])
        self.assertEqual(board_objects.add_to_board(self.board), new_board)

    @parameterized.expand([
        (coords.black, [0, 6], "P1 "),
        (coords.black, [4, 8], " K "),
        (coords.black, [1, 7], " B "),
        (coords.black, [5, 5], None),
        (coords.black, [0, 8], "L1 "),
        (coords.white, [0, 2], "P9 "),
        (coords.white, [5, 5], None),
        (coords.white, [4, 0], " K "),
        (coords.white, [1, 1], " R "),
        (coords.white, [7, 1], " B "),
    ])
    def test_get_piece(self, board, coord, piece):
        self.board_objects = Board_objects(board)
        self.assertEqual(self.board_objects.get_piece(coord), piece)

    @parameterized.expand([
        (coords.black, "P1 ", 0, 0, False, False, [0, 6]),
        (coords.black, "P1 ", 1, 0, False, False, [1, 6]),
        (coords.black, "P1 ", 0, 1, False, False, [0, 7]),
        (coords.black, "P1 ", 5, 0, True, False, [5, 6]),
        (coords.black, "P1 ", 0, 1, False, True, [0, 1]),
        (coords.black, "P1 ", 5, 5, True, True, [5, 5]),
        (coords.black, "P1 ", 0, -1, False, False, [0, 5])
    ])
    def test_get_coords(self, board, piece, x, y, replace_x, replace_y, expected):
        board_objects = Board_objects(board)
        self.assertEqual(board_objects.get_coords(piece, x, y, replace_x, replace_y), expected)


if __name__ == "__main__":
    unittest.main()