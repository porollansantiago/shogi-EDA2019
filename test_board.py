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
        self.assertEqual(self.board.play(new_coords[0], new_coords[1]), new_board)

    @parameterized.expand([
        ([3, 5], [3, 4], {" P ": [[0, 5],[1, 5],[2, 5], [3, 5]]}, {" P ": [[0, 4], [1, 4], [2, 4], [3, 4]]},
                        [['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '], 
                         ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '], 
                         ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '], 
                         ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '], 
                         [' P ', ' P ', ' P ', ' P ', '   ', '   ', '   ', '   ', '   '], 
                         [' P ', ' P ', ' P ', '   ', '   ', '   ', '   ', '   ', '   '], 
                         ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '], 
                         ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '], 
                         ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', ' P ']])
    ])
    def test_capture(self, coords, new_coords, black, white, new_board):
        board = Board(white, black)
        board.play(coords[0], coords[1])
        self.assertEqual(board.play(new_coords[0], new_coords[1]), new_board)

if __name__ == "__main__":
    unittest.main()