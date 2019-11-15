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
                        [' P ', ' P ', ' P ', ' P ', ' P ', ' P ', ' P ', ' P ', ' P '], 
                        ['   ', ' B ', '   ', '   ', '   ', '   ', '   ', ' R ', '   '], 
                        [' L ', 'KN ', 'SG ', 'GG ', ' K ', 'GG ', 'SG ', 'KN ', ' L ', '   ']]),

        (coords.white, [[' L ', 'KN ', 'SG ', 'GG ', ' K ', 'GG ', 'SG ', 'KN ', ' L ', '   '], 
                        ['   ', ' R ', '   ', '   ', '   ', '   ', '   ', ' B ', '   '], 
                        [' P ', ' P ', ' P ', ' P ', ' P ', ' P ', ' P ', ' P ', ' P '],
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
        (coords.black, ' P ', [0, 5],
                                      [['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '], 
                                       ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '], 
                                       ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '], 
                                       ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '], 
                                       ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '], 
                                       [' P ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '], 
                                       ['   ', ' P ', ' P ', ' P ', ' P ', ' P ', ' P ', ' P ', ' P '], 
                                       ['   ', ' B ', '   ', '   ', '   ', '   ', '   ', ' R ', '   '], 
                                       [' L ', 'KN ', 'SG ', 'GG ', ' K ', 'GG ', 'SG ', 'KN ', ' L ', '   ']]),

        ({"P1 ": [[10, 8]], "P2 ": [[11, 8]]}, "P1 ", [4, 4],
                                      [['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '], 
                                       ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '], 
                                       ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '], 
                                       ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '], 
                                       ['   ', '   ', '   ', '   ', 'P1 ', '   ', '   ', '   ', '   '], 
                                       ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '], 
                                       ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '], 
                                       ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '], 
                                       ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', 'P2 ']], 12, 11, [["P1 ", 0], ["P2 ", 0]])
    ])
    def test_move(self, coords, piece_to_move, new_coords, new_board, x_top=None, expected_x_top=10, captured_pieces=[[]], piece_index=0):
        board_objects = Board_objects(coords)
        board_objects.captured_x_top = x_top if x_top else 10
        board_objects.captured_pieces = captured_pieces
        board_objects.move(piece_to_move, piece_index, new_coords[0], new_coords[1])
        self.assertEqual(board_objects.add_to_board(self.board), new_board)
        self.assertEqual(board_objects.captured_x_top, expected_x_top)

    @parameterized.expand([
        (coords.black, 0, 6, " P "),
        (coords.black, 4, 8, " K "),
        (coords.black, 1, 7, " B "),
        (coords.black, 5, 5, None),
        (coords.black, 0, 8, " L "),
        (coords.white, 0, 2, " P "),
        (coords.white, 5, 5, None),
        (coords.white, 4, 0, " K "),
        (coords.white, 1, 1, " R "),
        (coords.white, 7, 1, " B "),
    ])
    def test_get_piece(self, board, x, y, piece):
        self.board_objects = Board_objects(board)
        self.assertEqual(self.board_objects.get_piece(x, y), (piece, 0))

    @parameterized.expand([
        (coords.black, " P ", 0, 0, 0, False, False, [0, 6]),
        (coords.black, " P ", 0, 1, 0, False, False, [1, 6]),
        (coords.black, " P ", 0, 0, 1, False, False, [0, 7]),
        (coords.black, " P ", 0, 5, 0, True, False, [5, 6]),
        (coords.black, " P ", 0, 0, 1, False, True, [0, 1]),
        (coords.black, " P ", 0, 5, 5, True, True, [5, 5]),
        (coords.black, " P ", 0, 0, -1, False, False, [0, 5])
    ])
    def test_get_coords(self, board, piece, piece_index, x, y, replace_x, replace_y, expected):
        board_objects = Board_objects(board)
        self.assertEqual(board_objects.get_coords(piece, piece_index, x, y, replace_x, replace_y), expected)

    @parameterized.expand([
        ({" P ": [[5, 2]]}, [5, 2]),
        ({" P ": [[2, 1]]}, [2, 1]),
        ({" P ": [[0, 0]]}, [0, 0]),
        ({" P ": [[8, 8]]}, [8, 8])
    ])
    def test_compare_coords(self, board, new_coords):
        board_objects = Board_objects(board)
        self.assertTrue(board_objects.compare_coords(new_coords))

    @parameterized.expand([
        ({"P1 ": [[5, 2]]}, [4, 2]),
        ({"P1 ": [[2, 1]]}, [1, 1]),
        ({"P1 ": [[0, 0]]}, [2, 0]),
        ({"P1 ": [[8, 8]]}, [8, 1])
    ])
    def test_compare_coords2(self, board, new_coords):
        board_objects = Board_objects(board)
        self.assertFalse(board_objects.compare_coords(new_coords))

    @parameterized.expand([
        ({"P1 ": [[5, 2]]}, [[5, 2]]),
        ({"P2 ": [[3, 5]], "P9 ": [[1, 2]]}, [[3, 5], [1, 2]]),
    ])
    def test_get_all_coords(self, board, all_coords):
        board_objects = Board_objects(board)
        self.assertEqual(board_objects.get_all_coords(), all_coords)

    @parameterized.expand([
        ([4, 4], "P1 ", {"P1 ": [[4, 4]]}, {}),
        ([2, 2], "P1 ", {"P1 ": [[2, 2]], "P2 ": [[3, 3]]}, {"P2 ": [[3, 3]]})
    ])
    def test_pop(self, coord, piece, board, new_board):
        board_objects = Board_objects(board)
        self.assertEqual(board_objects.pop(coord), piece)
        self.assertEqual(board_objects.coords, new_board)

    @parameterized.expand([
        ("black", "P1 ", None, None, {}, {"P1 ": [[10, 8]]}),
        ("black", "P1 ","P2 ", None, {}, {"P1 ": [[10, 8]], "P2 ": [[11, 8]]}),
        ("black", " R ", "KN1", " B ", {}, {" R ": [[10, 8]], "KN1": [[11, 8]], " B ": [[12, 8]]}),
        ("white", "P1 ", None, None, {}, {"P1 ": [[10, 0]]}),
        ("white", "P1 ","P2 ", None, {}, {"P1 ": [[10, 0]], "P2 ": [[11, 0]]}),
        ("white", " R ", "KN1", " B ", {}, {" R ": [[10, 0]], "KN1": [[11, 0]], " B ": [[12, 0]]})
    ])
    def test_add_piece(self, side, piece, piece2, piece3, board, new_board):
        board_objects = Board_objects(board)
        board_objects.add_piece(piece, 0, side)
        board_objects.add_piece(piece2, 0, side)
        board_objects.add_piece(piece3, 0, side)
        self.assertEqual(board_objects.coords, new_board)


if __name__ == "__main__":
    unittest.main()