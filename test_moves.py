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

# PAWN

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
    def test_validate_Pawn_move(self, turn, piece, new_coords):
        self.assertFalse(self.moves.validate(turn, piece, new_coords, self.black, self.white))

# LANCE

    @parameterized.expand([
        ("black", "L1 ", [0, 7], {"L1 ": [0, 8]}, {}),
        ("black", "L1 ", [0, 6], {"L1 ": [0, 8]}, {}),
        ("black", "L1 ", [0, 5], {"L1 ": [0, 8]}, {}),
        ("black", "L1 ", [0, 4], {"L1 ": [0, 8]}, {}),
        ("black", "L1 ", [0, 3], {"L1 ": [0, 8]}, {}),
        ("black", "L1 ", [0, 2], {"L1 ": [0, 8]}, {}),
        ("black", "L1 ", [0, 1], {"L1 ": [0, 8]}, {}),
        ("black", "L1 ", [0, 0], {"L1 ": [0, 8]}, {}),
        ("white", "L1 ", [8, 8], {}, {"L1 ": [8, 0]}),
        ("white", "L1 ", [8, 1], {}, {"L1 ": [8, 0]}),
        ("white", "L1 ", [8, 2], {}, {"L1 ": [8, 0]}),
        ("white", "L1 ", [8, 3], {}, {"L1 ": [8, 0]}),
        ("white", "L1 ", [8, 4], {}, {"L1 ": [8, 0]}),
        ("white", "L1 ", [8, 5], {}, {"L1 ": [8, 0]}),
        ("white", "L1 ", [8, 6], {}, {"L1 ": [8, 0]}),
        ("white", "L1 ", [8, 7], {}, {"L1 ": [8, 0]}),

    ])
    def test_validate_Lance_move(self, turn, piece, new_coords, example_black_coords, example_white_coords):
        example_black = Board_objects(example_black_coords)
        example_white = Board_objects(example_white_coords)
        self.assertTrue(self.moves.validate(turn, piece, new_coords, example_black, example_white))

    @parameterized.expand([
        ("black", "L1 ", [4, 8], {"L1 ": [4, 5]}, {}),
        ("black", "L1 ", [5, 7], {"L1 ": [5, 5]}, {}),
        ("black", "L1 ", [6, 6], {"L1 ": [6, 5]}, {}),
        ("black", "L1 ", [6, 6], {"L1 ": [5, 5]}, {}),
        ("black", "L1 ", [4, 4], {"L1 ": [5, 5]}, {}),
        ("black", "L1 ", [0, 0], {"L1 ": [5, 5]}, {}),
        ("black", "L1 ", [1, 1], {"L1 ": [5, 5]}, {}),
        ("black", "L1 ", [5, 6], {"L1 ": [5, 5]}, {}),
        ("black", "L1 ", [5, 7], {"L1 ": [5, 5]}, {}),
        ("black", "L1 ", [5, 8], {"L1 ": [5, 5]}, {}),
        ("white", "L1 ", [4, 3], {}, {"L1 ": [5, 5]}),
        ("white", "L1 ", [3, 4], {}, {"L1 ": [5, 5]}),
        ("white", "L1 ", [2, 5], {}, {"L1 ": [5, 5]}),
        ("white", "L1 ", [1, 6], {}, {"L1 ": [5, 5]}),
        ("white", "L1 ", [0, 7], {}, {"L1 ": [5, 5]}),
        ("white", "L1 ", [4, 4], {}, {"L1 ": [5, 5]}),
        ("white", "L1 ", [0, 0], {}, {"L1 ": [5, 5]}),
        ("white", "L1 ", [1, 5], {}, {"L1 ": [5, 5]}),
    ])
    def test_validate_Lance_move2(self, turn, piece, new_coords, example_black_coords, example_white_coords):
        example_black = Board_objects(example_black_coords)
        example_white = Board_objects(example_white_coords)
        self.assertFalse(self.moves.validate(turn, piece, new_coords, example_black, example_white))

# KNIGHT

    @parameterized.expand([
        ("black", "KN1", [3, 3], {"KN1": [4, 5]}, {}),
        ("black", "KN1", [5, 3], {"KN1": [4, 5]}, {}),
        ("white", "KN1", [3, 7], {}, {"KN1": [4, 5]}),
        ("white", "KN1", [5, 7], {}, {"KN1": [4, 5]}),

    ])
    def test_validate_Knight_move(self, turn, piece, new_coords, example_black_coords, example_white_coords):
        example_black = Board_objects(example_black_coords)
        example_white = Board_objects(example_white_coords)
        self.assertTrue(self.moves.validate(turn, piece, new_coords, example_black, example_white))

    @parameterized.expand([
        ("black", "KN1", [2, 3], {"KN1": [4, 5]}, {}),
        ("black", "KN1", [4, 3], {"KN1": [4, 5]}, {}),
        ("black", "KN1", [4, 7], {"KN1": [4, 5]}, {}),
        ("black", "KN1", [3, 7], {"KN1": [4, 5]}, {}),
        ("black", "KN1", [5, 7], {"KN1": [4, 5]}, {}),
        ("black", "KN1", [3, 6], {"KN1": [4, 5]}, {}),
        ("black", "KN1", [7, 8], {"KN1": [4, 5]}, {}),
        ("white", "KN1", [2, 3], {}, {"KN1": [4, 5]}),
        ("white", "KN1", [4, 3], {}, {"KN1": [4, 5]}),
        ("white", "KN1", [4, 7], {}, {"KN1": [4, 5]}),
        ("white", "KN1", [3, 3], {}, {"KN1": [4, 5]}),
        ("white", "KN1", [5, 3], {}, {"KN1": [4, 5]}),
        ("white", "KN1", [0, 0], {}, {"KN1": [4, 5]}),

    ])
    def test_validate_Knight_move2(self, turn, piece, new_coords, example_black_coords, example_white_coords):
        example_black = Board_objects(example_black_coords)
        example_white = Board_objects(example_white_coords)
        self.assertFalse(self.moves.validate(turn, piece, new_coords, example_black, example_white))

# SILVER GENERAL

    @parameterized.expand([
        ("black", "SG1", [3, 3], {"SG1": [4, 4]}, {}),
        ("black", "SG1", [4, 3], {"SG1": [4, 4]}, {}),
        ("black", "SG1", [5, 3], {"SG1": [4, 4]}, {}),
        ("black", "SG1", [3, 5], {"SG1": [4, 4]}, {}),
        ("black", "SG1", [5, 5], {"SG1": [4, 4]}, {}),
        ("white", "SG1", [3, 5], {}, {"SG1": [4, 4]}),
        ("white", "SG1", [4, 5], {}, {"SG1": [4, 4]}),
        ("white", "SG1", [5, 5], {}, {"SG1": [4, 4]}),
        ("white", "SG1", [3, 3], {}, {"SG1": [4, 4]}),
        ("white", "SG1", [5, 3], {}, {"SG1": [4, 4]}),
    ])
    def test_silverGeneral_move(self, turn, piece, new_coords, example_black_coords, example_white_coords):
        example_black = Board_objects(example_black_coords)
        example_white = Board_objects(example_white_coords)
        self.assertTrue(self.moves.validate(turn, piece, new_coords, example_black, example_white))

    @parameterized.expand([
        ("black", "SG1", [0, 0], {"SG1": [4, 4]}, {}),
        ("black", "SG1", [8, 8], {"SG1": [4, 4]}, {}),
        ("black", "SG1", [4, 5], {"SG1": [4, 4]}, {}),
        ("black", "SG1", [3, 4], {"SG1": [4, 4]}, {}),
        ("black", "SG1", [5, 4], {"SG1": [4, 4]}, {}),
        ("white", "SG1", [0, 0], {}, {"SG1": [4, 4]}),
        ("white", "SG1", [8, 8], {}, {"SG1": [4, 4]}),
        ("white", "SG1", [4, 3], {}, {"SG1": [4, 4]}),
        ("white", "SG1", [3, 4], {}, {"SG1": [4, 4]}),
        ("white", "SG1", [5, 4], {}, {"SG1": [4, 4]}),
    ])
    def test_silverGeneral_move2(self, turn, piece, new_coords, example_black_coords, example_white_coords):
        example_black = Board_objects(example_black_coords)
        example_white = Board_objects(example_white_coords)
        self.assertFalse(self.moves.validate(turn, piece, new_coords, example_black, example_white))

# GOLD GENERAL

    @parameterized.expand([
        ("black", "GG1", [3, 3], {"GG1": [4, 4]}, {}),
        ("black", "GG1", [4, 3], {"GG1": [4, 4]}, {}),
        ("black", "GG1", [5, 3], {"GG1": [4, 4]}, {}),
        ("black", "GG1", [3, 4], {"GG1": [4, 4]}, {}),
        ("black", "GG1", [5, 4], {"GG1": [4, 4]}, {}),
        ("black", "GG1", [4, 5], {"GG1": [4, 4]}, {}),
        ("white", "GG1", [3, 5], {}, {"GG1": [4, 4]}),
        ("white", "GG1", [4, 5], {}, {"GG1": [4, 4]}),
        ("white", "GG1", [5, 5], {}, {"GG1": [4, 4]}),
        ("white", "GG1", [3, 4], {}, {"GG1": [4, 4]}),
        ("white", "GG1", [5, 4], {}, {"GG1": [4, 4]}),
        ("white", "GG1", [4, 3], {}, {"GG1": [4, 4]}),
    ])
    def test_goldGeneral_move(self, turn, piece, new_coords, example_black_coords, example_white_coords):
        example_black = Board_objects(example_black_coords)
        example_white = Board_objects(example_white_coords)
        self.assertTrue(self.moves.validate(turn, piece, new_coords, example_black, example_white))

    @parameterized.expand([
        ("black", "GG1", [0, 0], {"GG1": [4, 4]}, {}),
        ("black", "GG1", [8, 8], {"GG1": [4, 4]}, {}),
        ("black", "GG1", [3, 5], {"GG1": [4, 4]}, {}),
        ("black", "GG1", [5, 5], {"GG1": [4, 4]}, {}),
        ("black", "GG1", [4, 2], {"GG1": [4, 4]}, {}),
        ("black", "GG1", [4, 6], {"GG1": [4, 4]}, {}),
        ("white", "GG1", [3, 3], {}, {"GG1": [4, 4]}),
        ("white", "GG1", [5, 3], {}, {"GG1": [4, 4]}),
        ("white", "GG1", [0, 0], {}, {"GG1": [4, 4]}),
        ("white", "GG1", [8, 8], {}, {"GG1": [4, 4]}),
        ("white", "GG1", [4, 2], {}, {"GG1": [4, 4]}),
        ("white", "GG1", [4, 6], {}, {"GG1": [4, 4]}),
    ])
    def test_goldGeneral_move2(self, turn, piece, new_coords, example_black_coords, example_white_coords):
        example_black = Board_objects(example_black_coords)
        example_white = Board_objects(example_white_coords)
        self.assertFalse(self.moves.validate(turn, piece, new_coords, example_black, example_white))

# KING

    @parameterized.expand([
        ("black", " K ", [3, 3], {" K ": [4, 4]}, {}),
        ("black", " K ", [4, 3], {" K ": [4, 4]}, {}),
        ("black", " K ", [5, 3], {" K ": [4, 4]}, {}),
        ("black", " K ", [3, 4], {" K ": [4, 4]}, {}),
        ("black", " K ", [5, 4], {" K ": [4, 4]}, {}),
        ("black", " K ", [3, 5], {" K ": [4, 4]}, {}),
        ("black", " K ", [4, 5], {" K ": [4, 4]}, {}),
        ("black", " K ", [5, 5], {" K ": [4, 4]}, {}),
        ("white", " K ", [3, 3], {}, {" K ": [4, 4]}),
        ("white", " K ", [4, 3], {}, {" K ": [4, 4]}),
        ("white", " K ", [5, 3], {}, {" K ": [4, 4]}),
        ("white", " K ", [3, 4], {}, {" K ": [4, 4]}),
        ("white", " K ", [5, 4], {}, {" K ": [4, 4]}),
        ("white", " K ", [3, 5], {}, {" K ": [4, 4]}),
        ("white", " K ", [4, 5], {}, {" K ": [4, 4]}),
        ("white", " K ", [5, 5], {}, {" K ": [4, 4]}),
    ])
    def test_king_move(self, turn, piece, new_coords, example_black_coords, example_white_coords):
        example_black = Board_objects(example_black_coords)
        example_white = Board_objects(example_white_coords)
        self.assertTrue(self.moves.validate(turn, piece, new_coords, example_black, example_white))

    @parameterized.expand([
        ("black", " K ", [0, 0], {" K ": [4, 4]}, {}),
        ("black", " K ", [8, 8], {" K ": [4, 4]}, {}),
        ("black", " K ", [2, 2], {" K ": [4, 4]}, {}),
        ("black", " K ", [4, 2], {" K ": [4, 4]}, {}),
        ("black", " K ", [4, 6], {" K ": [4, 4]}, {}),
        ("black", " K ", [6, 4], {" K ": [4, 4]}, {}),
        ("black", " K ", [2, 4], {" K ": [4, 4]}, {}),
        ("black", " K ", [6, 6], {" K ": [4, 4]}, {}),
        ("white", " K ", [0, 0], {}, {" K ": [4, 4]}),
        ("white", " K ", [8, 8], {}, {" K ": [4, 4]}),
        ("white", " K ", [2, 2], {}, {" K ": [4, 4]}),
        ("white", " K ", [4, 2], {}, {" K ": [4, 4]}),
        ("white", " K ", [4, 6], {}, {" K ": [4, 4]}),
        ("white", " K ", [6, 4], {}, {" K ": [4, 4]}),
        ("white", " K ", [2, 4], {}, {" K ": [4, 4]}),
        ("white", " K ", [6, 6], {}, {" K ": [4, 4]}),
    ])
    def test_king_move2(self, turn, piece, new_coords, example_black_coords, example_white_coords):
        example_black = Board_objects(example_black_coords)
        example_white = Board_objects(example_white_coords)
        self.assertFalse(self.moves.validate(turn, piece, new_coords, example_black, example_white))

# ROOK

    @parameterized.expand([
        ("black", "R1 ", [4, 0], {"R1 ": [4, 4]}, {}),
        ("black", "R1 ", [4, 1], {"R1 ": [4, 4]}, {}),
        ("black", "R1 ", [4, 2], {"R1 ": [4, 4]}, {}),
        ("black", "R1 ", [4, 3], {"R1 ": [4, 4]}, {}),
        ("black", "R1 ", [4, 5], {"R1 ": [4, 4]}, {}),
        ("black", "R1 ", [4, 6], {"R1 ": [4, 4]}, {}),
        ("black", "R1 ", [4, 7], {"R1 ": [4, 4]}, {}),
        ("black", "R1 ", [4, 8], {"R1 ": [4, 4]}, {}),
        ("black", "R1 ", [0, 4], {"R1 ": [4, 4]}, {}),
        ("black", "R1 ", [1, 4], {"R1 ": [4, 4]}, {}),
        ("black", "R1 ", [2, 4], {"R1 ": [4, 4]}, {}),
        ("black", "R1 ", [3, 4], {"R1 ": [4, 4]}, {}),
        ("black", "R1 ", [5, 4], {"R1 ": [4, 4]}, {}),
        ("black", "R1 ", [6, 4], {"R1 ": [4, 4]}, {}),
        ("black", "R1 ", [7, 4], {"R1 ": [4, 4]}, {}),
        ("black", "R1 ", [8, 4], {"R1 ": [4, 4]}, {}),
        ("white", "R1 ", [4, 0], {}, {"R1 ": [4, 4]}),
        ("white", "R1 ", [4, 1], {}, {"R1 ": [4, 4]}),
        ("white", "R1 ", [4, 2], {}, {"R1 ": [4, 4]}),
        ("white", "R1 ", [4, 3], {}, {"R1 ": [4, 4]}),
        ("white", "R1 ", [4, 5], {}, {"R1 ": [4, 4]}),
        ("white", "R1 ", [4, 6], {}, {"R1 ": [4, 4]}),
        ("white", "R1 ", [4, 7], {}, {"R1 ": [4, 4]}),
        ("white", "R1 ", [4, 8], {}, {"R1 ": [4, 4]}),
        ("white", "R1 ", [0, 4], {}, {"R1 ": [4, 4]}),
        ("white", "R1 ", [1, 4], {}, {"R1 ": [4, 4]}),
        ("white", "R1 ", [2, 4], {}, {"R1 ": [4, 4]}),
        ("white", "R1 ", [3, 4], {}, {"R1 ": [4, 4]}),
        ("white", "R1 ", [5, 4], {}, {"R1 ": [4, 4]}),
        ("white", "R1 ", [6, 4], {}, {"R1 ": [4, 4]}),
        ("white", "R1 ", [7, 4], {}, {"R1 ": [4, 4]}),
        ("white", "R1 ", [8, 4], {}, {"R1 ": [4, 4]}),
    ])
    def test_rook_move(self, turn, piece, new_coords, example_black_coords, example_white_coords):
        example_black = Board_objects(example_black_coords)
        example_white = Board_objects(example_white_coords)
        self.assertTrue(self.moves.validate(turn, piece, new_coords, example_black, example_white))

    @parameterized.expand([
        ("black", "R1 ", [0, 0], {"R1 ": [4, 4]}, {}),
        ("black", "R1 ", [8, 8], {"R1 ": [4, 4]}, {}),
        ("black", "R1 ", [1, 1], {"R1 ": [4, 4]}, {}),
        ("black", "R1 ", [2, 2], {"R1 ": [4, 4]}, {}),
        ("black", "R1 ", [3, 3], {"R1 ": [4, 4]}, {}),
        ("black", "R1 ", [6, 6], {"R1 ": [4, 4]}, {}),
        ("black", "R1 ", [5, 6], {"R1 ": [4, 4]}, {}),
        ("black", "R1 ", [8, 0], {"R1 ": [4, 4]}, {}),
        ("black", "R1 ", [0, 2], {"R1 ": [4, 4]}, {}),
        ("black", "R1 ", [1, 3], {"R1 ": [4, 4]}, {}),
        ("black", "R1 ", [2, 3], {"R1 ": [4, 4]}, {}),
        ("black", "R1 ", [3, 5], {"R1 ": [4, 4]}, {}),
        ("black", "R1 ", [6, 7], {"R1 ": [4, 4]}, {}),
        ("black", "R1 ", [8, 7], {"R1 ": [4, 4]}, {}),
        ("black", "R1 ", [0, 3], {"R1 ": [4, 4]}, {}),
        ("black", "R1 ", [2, 7], {"R1 ": [4, 4]}, {}),
        ("white", "R1 ", [0, 0], {}, {"R1 ": [4, 4]}),
        ("white", "R1 ", [8, 8], {}, {"R1 ": [4, 4]}),
        ("white", "R1 ", [1, 1], {}, {"R1 ": [4, 4]}),
        ("white", "R1 ", [2, 2], {}, {"R1 ": [4, 4]}),
        ("white", "R1 ", [3, 3], {}, {"R1 ": [4, 4]}),
        ("white", "R1 ", [6, 6], {}, {"R1 ": [4, 4]}),
        ("white", "R1 ", [5, 6], {}, {"R1 ": [4, 4]}),
        ("white", "R1 ", [8, 0], {}, {"R1 ": [4, 4]}),
        ("white", "R1 ", [0, 2], {}, {"R1 ": [4, 4]}),
        ("white", "R1 ", [1, 3], {}, {"R1 ": [4, 4]}),
        ("white", "R1 ", [2, 3], {}, {"R1 ": [4, 4]}),
        ("white", "R1 ", [3, 5], {}, {"R1 ": [4, 4]}),
        ("white", "R1 ", [6, 7], {}, {"R1 ": [4, 4]}),
        ("white", "R1 ", [8, 7], {}, {"R1 ": [4, 4]}),
        ("white", "R1 ", [0, 3], {}, {"R1 ": [4, 4]}),
        ("white", "R1 ", [2, 7], {}, {"R1 ": [4, 4]}),
        ("black", "R1 ", [4, 1], {"R1 ": [4, 4]}, {"P1 ": [4, 2]}),
        ("black", "R1 ", [4, 8], {"R1 ": [4, 4]}, {"P1 ": [4, 6]}),
        ("black", "R1 ", [0, 4], {"R1 ": [4, 4]}, {"P1 ": [2, 4]}),
        ("black", "R1 ", [7, 4], {"R1 ": [4, 4]}, {"P1 ": [6, 4]}),
        ("white", "R1 ", [4, 1], {"P1 ": [4, 2]}, {"R1 ": [4, 4]}),
        ("white", "R1 ", [4, 8], {"P1 ": [4, 6]}, {"R1 ": [4, 4]}),
        ("white", "R1 ", [0, 4], {"P1 ": [2, 4]}, {"R1 ": [4, 4]}),
        ("white", "R1 ", [7, 4], {"P1 ": [6, 4]}, {"R1 ": [4, 4]}),
        ("black", "R1 ", [4, 1], {"R1 ": [4, 4], "P1 ": [4, 2]}, {}),
        ("black", "R1 ", [4, 8], {"R1 ": [4, 4], "P1 ": [4, 6]}, {}),
        ("black", "R1 ", [0, 4], {"R1 ": [4, 4], "P1 ": [2, 4]}, {}),
        ("black", "R1 ", [7, 4], {"R1 ": [4, 4], "P1 ": [6, 4]}, {}),
    ])
    def test_rook_move2(self, turn, piece, new_coords, example_black_coords, example_white_coords):
        example_black = Board_objects(example_black_coords)
        example_white = Board_objects(example_white_coords)
        self.assertFalse(self.moves.validate(turn, piece, new_coords, example_black, example_white))


if __name__ == "__main__":
    unittest.main()