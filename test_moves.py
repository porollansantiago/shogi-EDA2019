import unittest
from moves import Moves
from parameterized import parameterized
from board_objects import Board_objects
import coordinates as c

class test_moves(unittest.TestCase):
    def setUp(self):
        self.moves = Moves()
        self.black = Board_objects(c.black)
        self.white = Board_objects(c.white)

    @parameterized.expand([
        ("black", "P1 ", [0, 5]),
        ("black", "P2 ", [1, 5]),
        ("black", "P3 ", [2, 5]),
        ("black", "P4 ", [3, 5]),
        ("black", "P5 ", [4, 5])
    ])
    def test_validate_not_overlapping(self, turn, piece, new_coords):
        self.assertTrue(self.moves.validate(turn, piece, new_coords, self.black, self.white))

    @parameterized.expand([
        ("white", "P1 ", [0, 0]),
        ("white", "P2 ", [1, 0]),
        ("white", "P3 ", [2, 0]),
        ("white", "P4 ", [3, 0]),
        ("white", "P5 ", [4, 0]),
        ("black", "P1 ", [0, 8]),
        ("black", "P2 ", [1, 8]),
        ("black", "P3 ", [2, 8]),
        ("black", "P4 ", [3, 8]),
        ("black", "P5 ", [4, 8])
    ])
    def test_validate_overlapping(self, turn, piece, new_coords):
        self.assertFalse(self.moves.validate(turn, piece, new_coords, self.black, self.white))

    @parameterized.expand([
        ("white", "P1 ", [0, 4]),
        ("white", "P2 ", [1, 4]),
        ("white", "P3 ", [2, 5]),
        ("white", "P4 ", [3, 4]),
        ("white", "P5 ", [4, 4]),
        ("black", "P1 ", [0, 4]),
        ("black", "P2 ", [1, 4]),
        ("black", "P3 ", [2, 3]),
        ("black", "P4 ", [3, 4]),
        ("black", "P5 ", [4, 3])
    ])
    def test_validate_Peon_move(self, turn, piece, new_coords):
        self.assertFalse(self.moves.validate(turn, piece, new_coords, self.black, self.white))

    @parameterized.expand([
        ("black", "L1 ", [0, 7], {"L1 ": [0, 8]}, {}),
        ("black", "L1 ", [0, 6], {"L1 ": [0, 8]}, {}),
        ("black", "L1 ", [0, 5], {"L1 ": [0, 8]}, {}),
        ("black", "L1 ", [0, 4], {"L1 ": [0, 8]}, {}),
        ("black", "L1 ", [0, 3], {"L1 ": [0, 8]}, {}),
        ("black", "L1 ", [0, 2], {"L1 ": [0, 8]}, {}),
        ("black", "L1 ", [0, 1], {"L1 ": [0, 8]}, {}),
        ("black", "L1 ", [0, 0], {"L1 ": [0, 8]}, {}),
    ])
    def test_validate_Lance_move(self, turn, piece, new_coords, example_black_coords, example_white_coords):
        example_black = Board_objects(example_black_coords)
        example_white = Board_objects(example_white_coords)
        self.assertTrue(self.moves.validate(turn, piece, new_coords, example_black, example_white))



if __name__ == "__main__":
    unittest.main()