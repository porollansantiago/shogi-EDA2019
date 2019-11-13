import unittest
from parameterized import parameterized
from board import Board


class Test_board(unittest.TestCase):
    
    def setUp(self):
        self.board = Board()

    def test_make_board_original(self):
        new_board = [['L2 ', 'KN2', 'SG2', 'GG2', ' K ', 'GG1', 'SG1', 'KN1', 'L1 '], 
                     ['   ', ' R ', '   ', '   ', '   ', '   ', '   ', ' B ', '   '], 
                     ['P9 ', 'P8 ', 'P7 ', 'P6 ', 'P5 ', 'P4 ', 'P3 ', 'P2 ', 'P1 '], 
                     ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '], 
                     ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '], 
                     ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '], 
                     ['P1 ', 'P2 ', 'P3 ', 'P4 ', 'P5 ', 'P6 ', 'P7 ', 'P8 ', 'P9 '], 
                     ['   ', ' B ', '   ', '   ', '   ', '   ', '   ', ' R ', '   '], 
                     ['L1 ', 'KN1', 'SG1', 'GG1', ' K ', 'GG2', 'SG2', 'KN2', 'L2 ']]
        self.assertEqual(self.board.make_board(), new_board)

    @parameterized.expand([
        ([0, 6], [0, 5], [['L2 ', 'KN2', 'SG2', 'GG2', ' K ', 'GG1', 'SG1', 'KN1', 'L1 '], 
                         ['   ', ' R ', '   ', '   ', '   ', '   ', '   ', ' B ', '   '], 
                         ['P9 ', 'P8 ', 'P7 ', 'P6 ', 'P5 ', 'P4 ', 'P3 ', 'P2 ', 'P1 '], 
                         ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '], 
                         ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '], 
                         ['P1 ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '], 
                         ['   ', 'P2 ', 'P3 ', 'P4 ', 'P5 ', 'P6 ', 'P7 ', 'P8 ', 'P9 '], 
                         ['   ', ' B ', '   ', '   ', '   ', '   ', '   ', ' R ', '   '], 
                         ['L1 ', 'KN1', 'SG1', 'GG1', ' K ', 'GG2', 'SG2', 'KN2', 'L2 ']]),

        ([8, 6], [8, 5], [['L2 ', 'KN2', 'SG2', 'GG2', ' K ', 'GG1', 'SG1', 'KN1', 'L1 '], 
                         ['   ', ' R ', '   ', '   ', '   ', '   ', '   ', ' B ', '   '], 
                         ['P9 ', 'P8 ', 'P7 ', 'P6 ', 'P5 ', 'P4 ', 'P3 ', 'P2 ', 'P1 '], 
                         ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '], 
                         ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '], 
                         ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', 'P9 '], 
                         ['P1 ', 'P2 ', 'P3 ', 'P4 ', 'P5 ', 'P6 ', 'P7 ', 'P8 ', '   '], 
                         ['   ', ' B ', '   ', '   ', '   ', '   ', '   ', ' R ', '   '], 
                         ['L1 ', 'KN1', 'SG1', 'GG1', ' K ', 'GG2', 'SG2', 'KN2', 'L2 ']])
    ])
    def test_play(self, piece_coords, new_coords, new_board):
        self.board.play(piece_coords)
        self.assertEqual(self.board.play(new_coords), new_board)

if __name__ == "__main__":
    unittest.main()