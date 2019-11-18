import unittest
from parameterized import parameterized
from board import Board


class Test_board(unittest.TestCase):
    
    def setUp(self):
        self.board = Board()

    def test_make_board_original(self):
        new_board = [[' L ', 'KN ', 'SG ', 'GG ', ' K ', 'GG ', 'SG ', 'KN ', ' L ', '   '], 
                     ['   ', ' R ', '   ', '   ', '   ', '   ', '   ', ' B ', '   '], 
                     [' P ', ' P ', ' P ', ' P ', ' P ', ' P ', ' P ', ' P ', ' P '], 
                     ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '], 
                     ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '], 
                     ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '], 
                     [' P ', ' P ', ' P ', ' P ', ' P ', ' P ', ' P ', ' P ', ' P '], 
                     ['   ', ' B ', '   ', '   ', '   ', '   ', '   ', ' R ', '   '], 
                     [' L ', 'KN ', 'SG ', 'GG ', ' K ', 'GG ', 'SG ', 'KN ', ' L ', '   ']]
        self.assertEqual(self.board.make_board(), new_board)

    @parameterized.expand([
        ({" P ": [[1, 1], [2, 1]]}, {},
                    [['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '], 
                     ['   ', ' P ', ' P ', '   ', '   ', '   ', '   ', '   ', '   '], 
                     ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '], 
                     ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '], 
                     ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '], 
                     ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '], 
                     ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '], 
                     ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '], 
                     ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ']] ),
        ({" P ": [[1, 0], [2, 0]]}, {" P ": [[3, 0]]},
                    [['   ', ' P ', ' P ', ' P ', '   ', '   ', '   ', '   ', '   ', '   '], 
                     ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '], 
                     ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '], 
                     ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '], 
                     ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '], 
                     ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '], 
                     ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '], 
                     ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '], 
                     ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ']] ),
        ({" P ": [[1, 8], [2, 8]]}, {},
                    [['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '], 
                     ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '], 
                     ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '], 
                     ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '], 
                     ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '], 
                     ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '], 
                     ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '], 
                     ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '], 
                     ['   ', ' P ', ' P ', '   ', '   ', '   ', '   ', '   ', '   ', '   ']] ),
        ({" P ": [[1, 8], [2, 8]]}, {" P ": [[3, 8]]},
                    [['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '], 
                     ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '], 
                     ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '], 
                     ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '], 
                     ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '], 
                     ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '], 
                     ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '], 
                     ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '], 
                     ['   ', ' P ', ' P ', ' P ', '   ', '   ', '   ', '   ', '   ', '   ']] ),
        ({" P ": [[1, 0]]}, {" P ": [[2, 0], [3, 0]]},
                    [['   ', ' P ', ' P ', ' P ', '   ', '   ', '   ', '   ', '   ', '   '], 
                     ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '], 
                     ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '], 
                     ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '], 
                     ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '], 
                     ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '], 
                     ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '], 
                     ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '], 
                     ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ']] ),
        ({" P ": [[1, 8]]}, {" P ": [[2, 8], [3, 8]]},
                    [['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '], 
                     ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '], 
                     ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '], 
                     ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '], 
                     ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '], 
                     ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '], 
                     ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '], 
                     ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '], 
                     ['   ', ' P ', ' P ', ' P ', '   ', '   ', '   ', '   ', '   ', '   ']] ),
    ])
    def test_make_board(self, white, black, new_board):
        board = Board(white, black)
        self.assertEqual(board.make_board(), new_board)

    @parameterized.expand([
        ([0, 6], [0, 5],[[' L ', 'KN ', 'SG ', 'GG ', ' K ', 'GG ', 'SG ', 'KN ', ' L ', '   '], 
                         ['   ', ' R ', '   ', '   ', '   ', '   ', '   ', ' B ', '   '], 
                         [' P ', ' P ', ' P ', ' P ', ' P ', ' P ', ' P ', ' P ', ' P '], 
                         ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '], 
                         ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '], 
                         [' P ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '], 
                         ['   ', ' P ', ' P ', ' P ', ' P ', ' P ', ' P ', ' P ', ' P '], 
                         ['   ', ' B ', '   ', '   ', '   ', '   ', '   ', ' R ', '   '], 
                         [' L ', 'KN ', 'SG ', 'GG ', ' K ', 'GG ', 'SG ', 'KN ', ' L ', '   ']]),
        ([8, 6], [8, 5],[[' L ', 'KN ', 'SG ', 'GG ', ' K ', 'GG ', 'SG ', 'KN ', ' L ', '   '], 
                         ['   ', ' R ', '   ', '   ', '   ', '   ', '   ', ' B ', '   '], 
                         [' P ', ' P ', ' P ', ' P ', ' P ', ' P ', ' P ', ' P ', ' P '], 
                         ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '], 
                         ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '], 
                         ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', ' P '], 
                         [' P ', ' P ', ' P ', ' P ', ' P ', ' P ', ' P ', ' P ', '   '], 
                         ['   ', ' B ', '   ', '   ', '   ', '   ', '   ', ' R ', '   '], 
                         [' L ', 'KN ', 'SG ', 'GG ', ' K ', 'GG ', 'SG ', 'KN ', ' L ', '   ']])
    ])
    def test_play(self, piece_coords, new_coords, new_board):
        self.board.play(piece_coords[0], piece_coords[1])
        self.board.play(new_coords[0], new_coords[1])
        self.assertEqual(self.board.make_board(), new_board)

    @parameterized.expand([
        ("black", [3, 5], [3, 4], 10, 10, [], [], " P ", 
        {" P ": [[0, 5],[1, 5],[2, 5], [3, 5]]}, {" P ": [[0, 4], [1, 4], [2, 4], [3, 4]]},
                        ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', ' P ']),
        ("black", [4, 8], [3, 6], 12, 10, [[" R ", [11, 8]], [" B ", [10, 8]]], [], "KN ", 
        {"KN ": [[4, 8]], " R ": [[11, 8]], " B ": [[10, 8]]}, {" P ": [[3, 6]]},
                        ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', ' B ', ' R ', ' P ']),
        ("black", [4, 8], [3, 6], 12, 10, [[" R ", [11, 8]], [" B ", [10, 8]]], [], "KN ", 
        {"KN ": [[4, 8]], " R ": [[11, 8]], " B ": [[10, 8]]}, {"PP ": [[3, 6]]},
                        ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', ' B ', ' R ', ' P ']),
        ("black", [4, 8], [3, 6], 12, 10, [[" R ", [11, 8]], [" B ", [10, 8]]], [], "KN ", 
        {"KN ": [[4, 8]], " R ": [[11, 8]], " B ": [[10, 8]]}, {"PSG": [[3, 6]]},
                        ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', ' B ', ' R ', 'SG ']),
        ("black", [4, 8], [3, 6], 12, 10, [[" R ", [11, 8]], [" B ", [10, 8]]], [], "KN ", 
        {"KN ": [[4, 8]], " R ": [[11, 8]], " B ": [[10, 8]]}, {"PR ": [[3, 6]]},
                        ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', ' B ', ' R ', ' R ']),
        ("white", [4, 0], [3, 2], 10, 14, [], [[" B ", [13, 0]], [" B ", [11, 0]], [" P ", [10, 0]], [" L ", [12, 0]]], "KN ",
        {" R ": [[3, 2]]}, {"KN ": [[4, 0]], " B ": [[13, 0], [11, 0]], " P ": [[10, 0]], " L ": [[12, 0]]},
                        ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', ' P ', ' B ', ' L ', ' B ', ' R ']),
        ("white", [4, 0], [3, 2], 10, 14, [], [[" B ", [13, 0]], [" B ", [11, 0]], [" P ", [10, 0]], [" L ", [12, 0]]], "KN ",
        {"PR ": [[3, 2]]}, {"KN ": [[4, 0]], " B ": [[13, 0], [11, 0]], " P ": [[10, 0]], " L ": [[12, 0]]},
                        ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', ' P ', ' B ', ' L ', ' B ', ' R ']),

    ])
    def test_capture(self, turn, coords, new_coords, bcaptopx, 
                    wcaptopx, bcap, wcap, expected_piece, black, 
                    white, expected_row):
        board = Board(white, black)
        board.turn = turn
        s = 0 if turn == "white" else 8
        board.white.captured_x_top, board.black.captured_x_top = wcaptopx, bcaptopx
        board.white.captured_pieces, board.black.captured_pieces = wcap, bcap
        board.play(coords[0], coords[1])
        board.play(new_coords[0], new_coords[1])
        b = board.make_board()
        self.assertEqual(b[coords[1]][coords[0]], '   ')
        self.assertEqual(b[new_coords[1]][new_coords[0]], expected_piece)
        self.assertEqual(b[s], expected_row)

    @parameterized.expand([
        ("black", {" P ": [[10, 8], [11, 8], [12, 8]]}, {},
            [11, 8], [0, 5], " P ", 13, 10, [[" P ", [11, 8]], [" P ", [10, 8]],[" P ", [12, 8]]], [],
            ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', ' P ', ' P ']),
        ("black", {" P ": [[10, 8], [11, 8], [13, 8]], " B ": [[12, 8]]}, {},
            [11, 8], [0, 5], " P ", 14, 10, [[" P ", [13, 8]], [" P ", [11, 8]], [" B ", [12, 8]], [" P ", [10, 8]]], [],
            ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', ' P ', ' B ', ' P ']),
        ("white", {}, {" P ": [[10, 0], [11, 0], [12, 0]]},
            [11, 0], [0, 5], " P ", 10, 13, [], [[" P ", [11, 0]], [" P ", [10, 0]],[" P ", [12, 0]]],
            ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', ' P ', ' P ']),
        ("white", {}, {" P ": [[10, 0], [11, 0], [13, 0]], " B ": [[12, 0]]},
            [11, 0], [0, 5], " P ", 10, 14, [], [[" P ", [11, 0]], [" P ", [10, 0]], [" P ", [13, 0]], [" B ", [12, 0]]],
            ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', ' P ', ' B ', ' P ']),

        ("black", {" P ": [[10, 8], [11, 8], [12, 8]]}, {" B ": [[0, 5]]},
            [11, 8], [0, 5], " B ", 13, 10, [[" P ", [11, 8]], [" P ", [10, 8]],[" P ", [12, 8]]], [],
            ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', ' P ', ' P ', ' P ']),
        ("black", {" P ": [[10, 8], [11, 8], [13, 8]], " B ": [[0, 5], [12, 8]]}, {},
            [11, 8], [0, 5], " B ", 14, 10, [[" P ", [13, 8]], [" P ", [11, 8]], [" B ", [12, 8]], [" P ", [10, 8]]], [],
            ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', ' P ', ' P ', ' B ', ' P ']),
        ("white", {" R ": [[0, 5]]}, {" P ": [[10, 0], [11, 0], [12, 0]]},
            [11, 0], [0, 5], " R ", 10, 13, [], [[" P ", [11, 0]], [" P ", [10, 0]],[" P ", [12, 0]]],
            ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', ' P ', ' P ', ' P ']),
        ("white", {}, {" P ": [[10, 0], [11, 0], [13, 0], [0, 5]], " B ": [[12, 0]]},
            [11, 0], [0, 5], " P ", 10, 14, [], [[" P ", [11, 0]], [" P ", [10, 0]], [" P ", [13, 0]], [" B ", [12, 0]]],
            ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', ' P ', ' P ', ' B ', ' P ']),

        ("black", {" P ": [[10, 8], [11, 8], [12, 8], [0, 6]]}, {" P ": [[0, 2]]},
            [11, 8], [0, 5], "   ", 13, 10, [[" P ", [11, 8]], [" P ", [10, 8]],[" P ", [12, 8]]], [],
            ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', ' P ', ' P ', ' P ']),
        ("white", {" P ": [[0, 4]]}, {" P ": [[10, 0], [11, 0], [12, 0], [0, 2]]},
            [11, 0], [0, 5], "   ", 10, 13, [], [[" P ", [11, 0]], [" P ", [10, 0]],[" P ", [12, 0]]],
            ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', ' P ', ' P ', ' P ']),
    ])
    def test_play_reintroduce(self, turn, black, white, coords, 
                                new_coords, expected_piece, b_xtop, w_xtop, 
                                b_capt, w_capt, expected_row):
        board = Board(white, black)
        board.turn = turn
        board.white.captured_x_top = w_xtop
        board.black.captured_x_top = b_xtop
        board.white.captured_pieces = w_capt
        board.black.captured_pieces = b_capt
        board.play(coords[0], coords[1])
        board.play(new_coords[0], new_coords[1])
        b = board.make_board()
        self.assertEqual(b[new_coords[1]][new_coords[0]], expected_piece)
        self.assertEqual(b[coords[1]], expected_row)

    @parameterized.expand([
        ({" P ": [[1, 3]]}, {}, [1, 3], [1, 2], [10, 4], 'PP ', "black"),
        ({" P ": [[1, 2]]}, {}, [1, 2], [1, 1], [10, 4], 'PP ', "black"),
        ({" P ": [[1, 3]]}, {}, [1, 3], [1, 2], [12, 4], ' P ', "black"),
        ({}, {" P ": [[1, 5]]}, [1, 5], [1, 6], [10, 4], 'PP ', "white"),
        ({}, {" P ": [[1, 6]]}, [1, 6], [1, 7], [10, 4], 'PP ', "white"),
        ({}, {" P ": [[1, 5]]}, [1, 5], [1, 6], [12, 4], ' P ', "white"),
        ({"SG ": [[1, 3]]}, {}, [1, 3], [1, 2], [10, 4], "PSG", "black"),
        ({"SG ": [[1, 3]]}, {}, [1, 3], [1, 2], [12, 4], "SG ", "black"),
        ({"SG ": [[1, 2]]}, {}, [1, 2], [1, 1], [10, 4], "PSG", "black"),
        ({"SG ": [[1, 2]]}, {}, [1, 2], [1, 1], [12, 4], "SG ", "black"),
        ({"SG ": [[1, 2]]}, {}, [1, 2], [0, 3], [10, 4], "PSG", "black"),
        ({"SG ": [[1, 2]]}, {}, [1, 2], [0, 3], [12, 4], "SG ", "black"),
        ({}, {"SG ": [[1, 5]]}, [1, 5], [1, 6], [10, 4], "PSG", "white"),
        ({}, {"SG ": [[1, 5]]}, [1, 5], [1, 6], [12, 4], "SG ", "white"),
        ({}, {"SG ": [[1, 6]]}, [1, 6], [1, 7], [10, 4], "PSG", "white"),
        ({}, {"SG ": [[1, 6]]}, [1, 6], [1, 7], [12, 4], "SG ", "white"),
        ({}, {"SG ": [[1, 6]]}, [1, 6], [2, 5], [10, 4], "PSG", "white"),
        ({}, {"SG ": [[1, 6]]}, [1, 6], [2, 5], [12, 4], "SG ", "white"),
        ({"KN ": [[3, 3]]}, {}, [3, 3], [4, 1], [10, 4], "PKN", "black"),
        ({"KN ": [[3, 3]]}, {}, [3, 3], [4, 1], [12, 4], "KN ", "black"),
        ({"KN ": [[3, 2]]}, {}, [3, 2], [4, 0], [10, 4], "PKN", "black"),
        ({"KN ": [[3, 2]]}, {}, [3, 2], [4, 0], [12, 4], "KN ", "black"),
        ({}, {"KN ": [[3, 4]]}, [3, 4], [2, 6], [10, 4], "PKN", "white"),
        ({}, {"KN ": [[3, 4]]}, [3, 4], [2, 6], [12, 4], "KN ", "white"),
        ({}, {"KN ": [[3, 6]]}, [3, 6], [2, 8], [10, 4], "PKN", "white"),
        ({}, {"KN ": [[3, 6]]}, [3, 6], [2, 8], [12, 4], "KN ", "white"),
        ({" L ": [[0, 6]]}, {}, [0, 6], [0, 2], [10, 4], "PL ", "black"),
        ({" L ": [[0, 6]]}, {}, [0, 6], [0, 2], [12, 4], " L ", "black"),
        ({" L ": [[0, 2]]}, {}, [0, 2], [0, 1], [10, 4], "PL ", "black"),
        ({" L ": [[0, 2]]}, {}, [0, 2], [0, 1], [12, 4], " L ", "black"),
        ({}, {" L ": [[8, 3]]}, [8, 3], [8, 6], [10, 4], "PL ", "white"),
        ({}, {" L ": [[8, 3]]}, [8, 3], [8, 6], [12, 4], " L ", "white"),
        ({}, {" L ": [[8, 6]]}, [8, 6], [8, 8], [10, 4], "PL ", "white"),
        ({}, {" L ": [[8, 6]]}, [8, 6], [8, 8], [12, 4], " L ", "white"),
        ({" B ": [[1, 4]]}, {}, [1, 4], [4, 1], [10, 4], "PB ", "black"),
        ({" B ": [[1, 4]]}, {}, [1, 4], [4, 1], [12, 4], " B ", "black"),
        ({" B ": [[6, 2]]}, {}, [6, 2], [7, 1], [10, 4], "PB ", "black"),
        ({" B ": [[6, 2]]}, {}, [6, 2], [7, 1], [12, 4], " B ", "black"),
        ({" B ": [[8, 2]]}, {}, [8, 2], [6, 4], [10, 4], "PB ", "black"),
        ({" B ": [[8, 2]]}, {}, [8, 2], [6, 4], [12, 4], " B ", "black"),
        ({}, {" B ": [[5, 4]]}, [5, 4], [2, 7], [10, 4], "PB ", "white"),
        ({}, {" B ": [[5, 4]]}, [5, 4], [2, 7], [12, 4], " B ", "white"),
        ({}, {" B ": [[3, 7]]}, [3, 7], [1, 5], [10, 4], "PB ", "white"),
        ({}, {" B ": [[3, 7]]}, [3, 7], [1, 5], [12, 4], " B ", "white"),
        ({}, {" B ": [[2, 7]]}, [2, 7], [1, 6], [10, 4], "PB ", "white"),
        ({}, {" B ": [[2, 7]]}, [2, 7], [1, 6], [12, 4], " B ", "white"),
        ({" R ": [[2, 5]]}, {}, [2, 5], [2, 0], [10, 4], "PR ", "black"),
        ({" R ": [[2, 5]]}, {}, [2, 5], [2, 0], [12, 4], " R ", "black"),
        ({" R ": [[2, 0]]}, {}, [2, 0], [2, 1], [10, 4], "PR ", "black"),
        ({" R ": [[2, 0]]}, {}, [2, 0], [2, 1], [12, 4], " R ", "black"),
        ({" R ": [[2, 2]]}, {}, [2, 2], [2, 7], [10, 4], "PR ", "black"),
        ({" R ": [[2, 2]]}, {}, [2, 2], [2, 7], [12, 4], " R ", "black"),
        ({}, {" R ": [[4, 3]]}, [4, 3], [4, 7], [10, 4], "PR ", "white"),
        ({}, {" R ": [[4, 3]]}, [4, 3], [4, 7], [12, 4], " R ", "white"),
        ({}, {" R ": [[4, 7]]}, [4, 7], [4, 5], [10, 4], "PR ", "white"),
        ({}, {" R ": [[4, 7]]}, [4, 7], [4, 5], [12, 4], " R ", "white"),
        ({}, {" R ": [[4, 7]]}, [4, 7], [4, 8], [10, 4], "PR ", "white"),
        ({}, {" R ": [[4, 7]]}, [4, 7], [4, 8], [12, 4], " R ", "white"),
    ])
    def test_play_promote(self, black, white, piece_coords, new_coords, promote, expected, turn):
        board = Board(white, black)
        board.turn = turn
        board.play(piece_coords[0], piece_coords[1])
        board.play(new_coords[0], new_coords[1])
        self.assertEqual(board.turn, turn)
        board.play(promote[0], promote[1])
        self.assertNotEqual(board.turn, turn)
        self.assertEqual(board.make_board()[new_coords[1]][new_coords[0]], expected)

    @parameterized.expand([
        ("black", {" R ": [[8, 8]]}, {" K ": [[4, 0]]}, [8, 8], [4, 8]),
        ("white", {" K ": [[4, 8]]}, {" R ": [[8, 0]]}, [8, 0], [4, 0]),
    ])
    def test_play_check(self, turn, black, white, piece_coords, new_coords):
        board = Board(white, black)
        board.turn = turn
        board.play(piece_coords[0], piece_coords[1])
        self.assertFalse(board.check)
        self.assertFalse(board.checkmate)
        board.play(new_coords[0], new_coords[1])
        self.assertTrue(board.check)
        self.assertFalse(board.checkmate)

    @parameterized.expand([
        ("black", {" R ": [[2, 3]], "GG ": [[2, 1], [6, 1]] }, {" K ": [[4, 0]]}, [2, 3], [4, 3]),
        ("white", {" K ": [[4, 8]]},{" R ": [[2, 3]], "GG ": [[2, 7], [6, 7]] }, [2, 3], [4, 3]),
        ("black", {"PR ": [[6, 1]], " B ": [[0, 3]], "KN ": [[4, 4]]}, {" K ": [[4, 0]]}, [4, 4], [3, 2]),
        ("white", {" K ": [[4, 8]]}, {"PR ": [[6, 7]], " B ": [[0, 5]], "KN ": [[4, 4]]}, [4, 4], [3, 6]),
    ])
    def test_play_checkmate(self, turn, black, white, piece_coords, new_coords):
        board = Board(white, black)
        board.turn = turn
        board.play(piece_coords[0], piece_coords[1])
        self.assertFalse(board.check)
        self.assertFalse(board.checkmate)
        board.play(new_coords[0], new_coords[1])
        self.assertTrue(board.check)
        self.assertTrue(board.checkmate)

    @parameterized.expand([
        ("black", {" R ": [[2, 3]], "GG ": [[3, 1], [6, 1]]}, { " K ": [[4, 0]]}, [2, 3], [4, 3]),
        ("white", {" K ": [[4, 8]]}, {" R ": [[2, 3]], "GG ": [[3, 7], [6, 7]] }, [2, 3], [4, 3]),
        ("black", {" R ": [[2, 3]], "GG ": [[6, 1]], " P ": [[3, 1]]}, { " K ": [[4, 0]]}, [2, 3], [4, 3]),
        ("white", {" K ": [[4, 8]]}, {" R ": [[2, 3]], "GG ": [[6, 7]], " P ": [[3, 7]]}, [2, 3], [4, 3]),
        ("black", {" R ": [[2, 3]], "GG ": [[6, 1], [2, 1]]}, { " K ": [[4, 0]], " B ": [[6, 0]]}, [2, 3], [4, 3]),
        ("white", {" K ": [[4, 8]], " B ": [[7, 4]]}, {" R ": [[2, 3]], "GG ": [[6, 7], [2, 7]]}, [2, 3], [4, 3]),
        ("black", {"PR ": [[6, 1]], "KN ": [[4, 4]]}, {" K ": [[4, 0]]}, [4, 4], [3, 2]),
        ("white", {" K ": [[4, 8]]}, {"PR ": [[6, 7]], "KN ": [[4, 4]]}, [4, 4], [3, 6]),    
    ])
    def test_play_checkmate_false(self, turn, black, white, piece_coords, new_coords):
        board = Board(white, black)
        board.turn = turn
        board.play(piece_coords[0], piece_coords[1])
        self.assertFalse(board.check)
        self.assertFalse(board.checkmate)
        board.play(new_coords[0], new_coords[1])
        self.assertTrue(board.check)
        self.assertFalse(board.checkmate)

    @parameterized.expand([
        ("black", {" R ": [[8, 8]]}, {" K ": [[4, 0]]}, [8, 8], [4, 8], [4, 0], [5, 0]),
        ("white", {" K ": [[4, 8]]}, {" R ": [[8, 0]]}, [8, 0], [4, 0], [4, 8], [5, 8]),
    ])
    def test_play_check_move(self, turn, black, white, piece_coords, new_coords, piece2_coords, new_coords2):
        board = Board(white, black)
        board.turn = turn
        board.play(piece_coords[0], piece_coords[1])
        board.play(new_coords[0], new_coords[1])
        self.assertTrue(board.check)
        self.assertFalse(board.checkmate)
        board.play(piece2_coords[0], piece2_coords[1])
        board.play(new_coords2[0], new_coords2[1])
        self.assertFalse(board.check)
        self.assertFalse(board.checkmate)

    @parameterized.expand([
        ("black", {" R ": [[8, 8]]}, {" K ": [[4, 0]]}, [8, 8], [4, 8], [4, 0], [4, 1]),
        ("white", {" K ": [[4, 8]]}, {" R ": [[8, 0]]}, [8, 0], [4, 0], [4, 8], [4, 7]),
        ("black", {" R ": [[8, 8]]}, {" K ": [[4, 0]], " P ": [[0, 2]]}, [8, 8], [4, 8], [0, 2], [0, 3]),
        ("white", {" K ": [[4, 8]], " P ": [[0, 6]]}, {" R ": [[8, 0]]}, [8, 0], [4, 0], [0, 6], [0, 5]),
    ])
    def test_play_check_move_false(self, turn, black, white, piece_coords, new_coords, piece2_coords, new_coords2):
        board = Board(white, black)
        board.turn = turn
        turn = "black" if turn == "white" else "white"
        board.play(piece_coords[0], piece_coords[1])
        board.play(new_coords[0], new_coords[1])
        self.assertEqual(turn, board.turn)
        self.assertTrue(board.check)
        board.play(piece2_coords[0], piece2_coords[1])
        board.play(new_coords2[0], new_coords2[1])
        self.assertEqual(turn, board.turn)
        self.assertTrue(board.check)

if __name__ == "__main__":
    unittest.main(verbosity=2)