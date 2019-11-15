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
        ("white", "P2 ", 4, 5, {}, {"P2 ": [[4, 4]], "P1": [[4, 5]]}),
        ("white", " R ", 4, 5, {}, {" R ": [[4, 4]], "P1": [[4, 5]]}),
        ("white", "L1 ", 4, 5, {}, {"L1 ": [[4, 4]], "P1": [[4, 5]]}),
        ("white", "KN1", 3, 6, {}, {"KN1": [[4, 4]], "P1": [[3, 6]]}),
        ("white", "SG1", 4, 5, {}, {"SG1": [[4, 4]], "P1": [[4, 5]]}),
        ("white", "GG1", 4, 5, {}, {"GG1": [[4, 4]], "P1": [[4, 5]]}),
        ("white", " B ", 3, 3, {}, {" B ": [[4, 4]], "P1": [[3, 3]]}),
        ("white", " K ", 4, 5, {}, {" K ": [[4, 4]], "P1": [[4, 5]]}),
        ("black", "P2 ", 4, 3, {"P2 ": [[4, 4]], "P1": [[4, 3]]}, {}),
        ("black", " R ", 4, 3, {" R ": [[4, 4]], "P1": [[4, 3]]}, {}),
        ("black", "L1 ", 4, 3, {"L1 ": [[4, 4]], "P1": [[4, 3]]}, {}),
        ("black", "KN1", 5, 2, {"KN1": [[4, 4]], "P1": [[5, 2]]}, {}),
        ("black", "SG1", 4, 3, {"SG1": [[4, 4]], "P1": [[4, 3]]}, {}),
        ("black", "GG1", 4, 3, {"GG1": [[4, 4]], "P1": [[4, 3]]}, {}),
        ("black", " B ", 3, 3, {" B ": [[4, 4]], "P1": [[3, 3]]}, {}),
        ("black", " K ", 4, 3, {" K ": [[4, 4]], "P1": [[4, 3]]}, {}),
    ])
    def test_validate_overlapping(self, turn, piece, x, y, example_black_coords, example_white_coords):
        example_black = Board_objects(example_black_coords)
        example_white = Board_objects(example_white_coords)
        self.assertFalse(self.moves.validate(turn, piece, 0, x, y, example_black, example_white))

    @parameterized.expand([
        ("white", "P2 ", 4, 5, {}, {"P2 ": [[4, 4]]}),
        ("white", " R ", 4, 5, {}, {" R ": [[4, 4]]}),
        ("white", "L1 ", 4, 5, {}, {"L1 ": [[4, 4]]}),
        ("white", "KN1", 3, 6, {}, {"KN1": [[4, 4]]}),
        ("white", "SG1", 4, 5, {}, {"SG1": [[4, 4]]}),
        ("white", "GG1", 4, 5, {}, {"GG1": [[4, 4]]}),
        ("white", " B ", 3, 3, {}, {" B ": [[4, 4]]}),
        ("white", " K ", 4, 5, {}, {" K ": [[4, 4]]}),
        ("black", "P2 ", 4, 3, {"P2 ": [[4, 4]]}, {}),
        ("black", " R ", 4, 3, {" R ": [[4, 4]]}, {}),
        ("black", "L1 ", 4, 3, {"L1 ": [[4, 4]]}, {}),
        ("black", "KN1", 5, 2, {"KN1": [[4, 4]]}, {}),
        ("black", "SG1", 4, 3, {"SG1": [[4, 4]]}, {}),
        ("black", "GG1", 4, 3, {"GG1": [[4, 4]]}, {}),
        ("black", " B ", 3, 3, {" B ": [[4, 4]]}, {}),
        ("black", " K ", 4, 3, {" K ": [[4, 4]]}, {}),
    ])
    def test_validate_overlapping1(self, turn, piece, x, y, example_black_coords, example_white_coords):
        example_black = Board_objects(example_black_coords)
        example_white = Board_objects(example_white_coords)
        self.assertTrue(self.moves.validate(turn, piece, 0, x, y, example_black, example_white))

    @parameterized.expand([
        ("white", "P2 ", 4, 5, {"P1 ": [[4, 5]]}, {"P2 ": [[4, 4]]}),
        ("white", " R ", 4, 5, {"P1 ": [[4, 5]]}, {" R ": [[4, 4]]}),
        ("white", "L1 ", 4, 5, {"P1 ": [[4, 5]]}, {"L1 ": [[4, 4]]}),
        ("white", "KN1", 3, 6, {"P1 ": [[3, 6]]}, {"KN1": [[4, 4]]}),
        ("white", "SG1", 4, 5, {"P1 ": [[4, 5]]}, {"SG1": [[4, 4]]}),
        ("white", "GG1", 4, 5, {"P1 ": [[4, 5]]}, {"GG1": [[4, 4]]}),
        ("white", " B ", 3, 3, {"P1 ": [[3, 3]]}, {" B ": [[4, 4]]}),
        ("white", " K ", 4, 5, {"P1 ": [[4, 5]]}, {" K ": [[4, 4]]}),
        ("black", "P2 ", 4, 3, {"P2 ": [[4, 4]]}, {"P1 ": [[4, 3]]}),
        ("black", " R ", 4, 3, {" R ": [[4, 4]]}, {"P1 ": [[4, 3]]}),
        ("black", "L1 ", 4, 3, {"L1 ": [[4, 4]]}, {"P1 ": [[4, 3]]}),
        ("black", "KN1", 5, 2, {"KN1": [[4, 4]]}, {"P1 ": [[5, 2]]}),
        ("black", "SG1", 4, 3, {"SG1": [[4, 4]]}, {"P1 ": [[4, 3]]}),
        ("black", "GG1", 4, 3, {"GG1": [[4, 4]]}, {"P1 ": [[4, 3]]}),
        ("black", " B ", 3, 3, {" B ": [[4, 4]]}, {"P1 ": [[3, 3]]}),
        ("black", " K ", 4, 3, {" K ": [[4, 4]]}, {"P1 ": [[4, 3]]}),
    ])
    def test_validate_overlapping2(self, turn, piece, x, y, example_black_coords, example_white_coords):
        example_black = Board_objects(example_black_coords)
        example_white = Board_objects(example_white_coords)
        self.assertTrue(self.moves.validate(turn, piece, 0, x, y, example_black, example_white))

# PAWN
    @parameterized.expand([
        ("black", " P ", 0, 5, {" P ": [[0, 6]]}, {}),
        ("black", " P ", 2, 5, {" P ": [[2, 6]]}, {}),
        ("black", " P ", 3, 5, {" P ": [[3, 6]]}, {}),
        ("black", " P ", 4, 5, {" P ": [[4, 6]]}, {}),
        ("black", " P ", 5, 5, {" P ": [[5, 6]]}, {}),
        ("black", " P ", 6, 5, {" P ": [[6, 6]]}, {}),
        ("black", " P ", 7, 5, {" P ": [[7, 6]]}, {}),
        ("black", " P ", 8, 5, {" P ": [[8, 6]]}, {}),
        ("white", " P ", 1, 3, {}, {" P ": [[1, 2]]}),
        ("white", " P ", 2, 3, {}, {" P ": [[2, 2]]}),
        ("white", " P ", 3, 3, {}, {" P ": [[3, 2]]}),
        ("white", " P ", 4, 3, {}, {" P ": [[4, 2]]}),
        ("white", " P ", 5, 3, {}, {" P ": [[5, 2]]}),
        ("white", " P ", 6, 3, {}, {" P ": [[6, 2]]}),
        ("white", " P ", 7, 3, {}, {" P ": [[7, 2]]}),
        ("white", " P ", 8, 3, {}, {" P ": [[8, 2]]}),

    ])
    def test_validate_pawn_move(self, turn, piece, x, y, example_black_coords, example_white_coords):
        example_black = Board_objects(example_black_coords)
        example_white = Board_objects(example_white_coords)
        self.assertTrue(self.moves.validate(turn, piece, 0, x, y, example_black, example_white))
    @parameterized.expand([
        ("white", " P ", 0, 4),
        ("white", " P ", 1, 4),
        ("white", " P ", 2, 5),
        ("white", " P ", 3, 4),
        ("white", " P ", 4, 4),
        ("black", " P ", 0, 4),
        ("black", " P ", 1, 4),
        ("black", " P ", 2, 3),
        ("black", " P ", 3, 4),
        ("black", " P ", 4, 3)
    ])
    def test_validate_Pawn_move(self, turn, piece, x, y):
        self.assertFalse(self.moves.validate(turn, piece, 0, x, y, self.black, self.white))

# LANCE

    @parameterized.expand([
        ("black", "L1 ", 0, 7, {"L1 ": [[0, 8]]}, {}),
        ("black", "L1 ", 0, 6, {"L1 ": [[0, 8]]}, {}),
        ("black", "L1 ", 0, 5, {"L1 ": [[0, 8]]}, {}),
        ("black", "L1 ", 0, 4, {"L1 ": [[0, 8]]}, {}),
        ("black", "L1 ", 0, 3, {"L1 ": [[0, 8]]}, {}),
        ("black", "L1 ", 0, 2, {"L1 ": [[0, 8]]}, {}),
        ("black", "L1 ", 0, 1, {"L1 ": [[0, 8]]}, {}),
        ("black", "L1 ", 0, 0, {"L1 ": [[0, 8]]}, {}),
        ("white", "L1 ", 8, 8, {}, {"L1 ": [[8, 0]]}),
        ("white", "L1 ", 8, 1, {}, {"L1 ": [[8, 0]]}),
        ("white", "L1 ", 8, 2, {}, {"L1 ": [[8, 0]]}),
        ("white", "L1 ", 8, 3, {}, {"L1 ": [[8, 0]]}),
        ("white", "L1 ", 8, 4, {}, {"L1 ": [[8, 0]]}),
        ("white", "L1 ", 8, 5, {}, {"L1 ": [[8, 0]]}),
        ("white", "L1 ", 8, 6, {}, {"L1 ": [[8, 0]]}),
        ("white", "L1 ", 8, 7, {}, {"L1 ": [[8, 0]]}),

    ])
    def test_validate_Lance_move(self, turn, piece, x, y, example_black_coords, example_white_coords):
        example_black = Board_objects(example_black_coords)
        example_white = Board_objects(example_white_coords)
        self.assertTrue(self.moves.validate(turn, piece, 0, x, y, example_black, example_white))

    @parameterized.expand([
        ("black", "L1 ", 4, 8, {"L1 ": [[4, 5]]}, {}),
        ("black", "L1 ", 5, 7, {"L1 ": [[5, 5]]}, {}),
        ("black", "L1 ", 6, 6, {"L1 ": [[6, 5]]}, {}),
        ("black", "L1 ", 6, 6, {"L1 ": [[5, 5]]}, {}),
        ("black", "L1 ", 4, 4, {"L1 ": [[5, 5]]}, {}),
        ("black", "L1 ", 0, 0, {"L1 ": [[5, 5]]}, {}),
        ("black", "L1 ", 1, 1, {"L1 ": [[5, 5]]}, {}),
        ("black", "L1 ", 5, 6, {"L1 ": [[5, 5]]}, {}),
        ("black", "L1 ", 5, 7, {"L1 ": [[5, 5]]}, {}),
        ("black", "L1 ", 5, 8, {"L1 ": [[5, 5]]}, {}),
        ("white", "L1 ", 4, 3, {}, {"L1 ": [[5, 5]]}),
        ("white", "L1 ", 3, 4, {}, {"L1 ": [[5, 5]]}),
        ("white", "L1 ", 2, 5, {}, {"L1 ": [[5, 5]]}),
        ("white", "L1 ", 1, 6, {}, {"L1 ": [[5, 5]]}),
        ("white", "L1 ", 0, 7, {}, {"L1 ": [[5, 5]]}),
        ("white", "L1 ", 4, 4, {}, {"L1 ": [[5, 5]]}),
        ("white", "L1 ", 0, 0, {}, {"L1 ": [[5, 5]]}),
        ("white", "L1 ", 1, 5, {}, {"L1 ": [[5, 5]]}),
        ("black", "L1 ", 4, 1, {"L1 ": [[4, 4]]}, {"P1 ": [[4, 2]]}),
        ("black", "L1 ", 4, 0, {"L1 ": [[4, 4]]}, {"P1 ": [[4, 2]]}),
        ("white", "L1 ", 4, 7, {"P1 ": [[4, 6]]}, {"L1 ": [[4, 4]]}),
        ("white", "L1 ", 4, 8, {"P1 ": [[4, 6]]}, {"L1 ": [[4, 4]]}),
    ])
    def test_validate_Lance_move2(self, turn, piece, x, y, example_black_coords, example_white_coords):
        example_black = Board_objects(example_black_coords)
        example_white = Board_objects(example_white_coords)
        self.assertFalse(self.moves.validate(turn, piece, 0, x, y, example_black, example_white))

# KNIGHT

    @parameterized.expand([
        ("black", "KN1", 3, 3, {"KN1": [[4, 5]]}, {}),
        ("black", "KN1", 5, 3, {"KN1": [[4, 5]]}, {}),
        ("white", "KN1", 3, 7, {}, {"KN1": [[4, 5]]}),
        ("white", "KN1", 5, 7, {}, {"KN1": [[4, 5]]}),

    ])
    def test_validate_Knight_move(self, turn, piece, x, y, example_black_coords, example_white_coords):
        example_black = Board_objects(example_black_coords)
        example_white = Board_objects(example_white_coords)
        self.assertTrue(self.moves.validate(turn, piece, 0, x, y, example_black, example_white))

    @parameterized.expand([
        ("black", "KN1", 2, 3, {"KN1": [[4, 5]]}, {}),
        ("black", "KN1", 4, 3, {"KN1": [[4, 5]]}, {}),
        ("black", "KN1", 4, 7, {"KN1": [[4, 5]]}, {}),
        ("black", "KN1", 3, 7, {"KN1": [[4, 5]]}, {}),
        ("black", "KN1", 5, 7, {"KN1": [[4, 5]]}, {}),
        ("black", "KN1", 3, 6, {"KN1": [[4, 5]]}, {}),
        ("black", "KN1", 7, 8, {"KN1": [[4, 5]]}, {}),
        ("white", "KN1", 2, 3, {}, {"KN1": [[4, 5]]}),
        ("white", "KN1", 4, 3, {}, {"KN1": [[4, 5]]}),
        ("white", "KN1", 4, 7, {}, {"KN1": [[4, 5]]}),
        ("white", "KN1", 3, 3, {}, {"KN1": [[4, 5]]}),
        ("white", "KN1", 5, 3, {}, {"KN1": [[4, 5]]}),
        ("white", "KN1", 0, 0, {}, {"KN1": [[4, 5]]})

    ])
    def test_validate_Knight_move2(self, turn, piece, x, y, example_black_coords, example_white_coords):
        example_black = Board_objects(example_black_coords)
        example_white = Board_objects(example_white_coords)
        self.assertFalse(self.moves.validate(turn, piece, 0, x, y, example_black, example_white))

# SILVER GENERAL

    @parameterized.expand([
        ("black", "SG1", 3, 3, {"SG1": [[4, 4]]}, {}),
        ("black", "SG1", 4, 3, {"SG1": [[4, 4]]}, {}),
        ("black", "SG1", 5, 3, {"SG1": [[4, 4]]}, {}),
        ("black", "SG1", 3, 5, {"SG1": [[4, 4]]}, {}),
        ("black", "SG1", 5, 5, {"SG1": [[4, 4]]}, {}),
        ("white", "SG1", 3, 5, {}, {"SG1": [[4, 4]]}),
        ("white", "SG1", 4, 5, {}, {"SG1": [[4, 4]]}),
        ("white", "SG1", 5, 5, {}, {"SG1": [[4, 4]]}),
        ("white", "SG1", 3, 3, {}, {"SG1": [[4, 4]]}),
        ("white", "SG1", 5, 3, {}, {"SG1": [[4, 4]]}),
    ])
    def test_silverGeneral_move(self, turn, piece, x, y, example_black_coords, example_white_coords):
        example_black = Board_objects(example_black_coords)
        example_white = Board_objects(example_white_coords)
        self.assertTrue(self.moves.validate(turn, piece, 0, x, y, example_black, example_white))

    @parameterized.expand([
        ("black", "SG1", 8, 8, {"SG1": [[4, 4]]}, {}),
        ("black", "SG1", 0, 0, {"SG1": [[4, 4]]}, {}),
        ("black", "SG1", 4, 5, {"SG1": [[4, 4]]}, {}),
        ("black", "SG1", 3, 4, {"SG1": [[4, 4]]}, {}),
        ("black", "SG1", 5, 4, {"SG1": [[4, 4]]}, {}),
        ("white", "SG1", 0, 0, {}, {"SG1": [[4, 4]]}),
        ("white", "SG1", 8, 8, {}, {"SG1": [[4, 4]]}),
        ("white", "SG1", 4, 3, {}, {"SG1": [[4, 4]]}),
        ("white", "SG1", 3, 4, {}, {"SG1": [[4, 4]]}),
        ("white", "SG1", 5, 4, {}, {"SG1": [[4, 4]]}),
    ])
    def test_silverGeneral_move2(self, turn, piece, x, y, example_black_coords, example_white_coords):
        example_black = Board_objects(example_black_coords)
        example_white = Board_objects(example_white_coords)
        self.assertFalse(self.moves.validate(turn, piece, 0, x, y, example_black, example_white))

# GOLD GENERAL

    @parameterized.expand([
        ("black", "GG1", 3, 3, {"GG1": [[4, 4]]}, {}),
        ("black", "GG1", 4, 3, {"GG1": [[4, 4]]}, {}),
        ("black", "GG1", 5, 3, {"GG1": [[4, 4]]}, {}),
        ("black", "GG1", 3, 4, {"GG1": [[4, 4]]}, {}),
        ("black", "GG1", 5, 4, {"GG1": [[4, 4]]}, {}),
        ("black", "GG1", 4, 5, {"GG1": [[4, 4]]}, {}),
        ("white", "GG1", 3, 5, {}, {"GG1": [[4, 4]]}),
        ("white", "GG1", 4, 5, {}, {"GG1": [[4, 4]]}),
        ("white", "GG1", 5, 5, {}, {"GG1": [[4, 4]]}),
        ("white", "GG1", 3, 4, {}, {"GG1": [[4, 4]]}),
        ("white", "GG1", 5, 4, {}, {"GG1": [[4, 4]]}),
        ("white", "GG1", 4, 3, {}, {"GG1": [[4, 4]]}),
    ]) 
    def test_goldGeneral_move(self, turn, piece, x, y, example_black_coords, example_white_coords):
        example_black = Board_objects(example_black_coords)
        example_white = Board_objects(example_white_coords)
        self.assertTrue(self.moves.validate(turn, piece, 0, x, y, example_black, example_white))

    @parameterized.expand([
        ("black", "GG1", 0, 0, {"GG1": [[4, 4]]}, {}),
        ("black", "GG1", 8, 8, {"GG1": [[4, 4]]}, {}),
        ("black", "GG1", 3, 5, {"GG1": [[4, 4]]}, {}),
        ("black", "GG1", 5, 5, {"GG1": [[4, 4]]}, {}),
        ("black", "GG1", 4, 2, {"GG1": [[4, 4]]}, {}),
        ("black", "GG1", 4, 6, {"GG1": [[4, 4]]}, {}),
        ("white", "GG1", 3, 3, {}, {"GG1": [[4, 4]]}),
        ("white", "GG1", 5, 3, {}, {"GG1": [[4, 4]]}),
        ("white", "GG1", 0, 0, {}, {"GG1": [[4, 4]]}),
        ("white", "GG1", 8, 8, {}, {"GG1": [[4, 4]]}),
        ("white", "GG1", 4, 2, {}, {"GG1": [[4, 4]]}),
        ("white", "GG1", 4, 6, {}, {"GG1": [[4, 4]]}),
    ])
    def test_goldGeneral_move2(self, turn, piece, x, y, example_black_coords, example_white_coords):
        example_black = Board_objects(example_black_coords)
        example_white = Board_objects(example_white_coords)
        self.assertFalse(self.moves.validate(turn, piece, 0, x, y, example_black, example_white))

# KING

    @parameterized.expand([
        ("black", " K ", 3, 3, {" K ": [[4, 4]]}, {}),
        ("black", " K ", 4, 3, {" K ": [[4, 4]]}, {}),
        ("black", " K ", 5, 3, {" K ": [[4, 4]]}, {}),
        ("black", " K ", 3, 4, {" K ": [[4, 4]]}, {}),
        ("black", " K ", 5, 4, {" K ": [[4, 4]]}, {}),
        ("black", " K ", 3, 5, {" K ": [[4, 4]]}, {}),
        ("black", " K ", 4, 5, {" K ": [[4, 4]]}, {}),
        ("black", " K ", 5, 5, {" K ": [[4, 4]]}, {}),
        ("white", " K ", 3, 3, {}, {" K ": [[4, 4]]}),
        ("white", " K ", 4, 3, {}, {" K ": [[4, 4]]}),
        ("white", " K ", 5, 3, {}, {" K ": [[4, 4]]}),
        ("white", " K ", 3, 4, {}, {" K ": [[4, 4]]}),
        ("white", " K ", 5, 4, {}, {" K ": [[4, 4]]}),
        ("white", " K ", 3, 5, {}, {" K ": [[4, 4]]}),
        ("white", " K ", 4, 5, {}, {" K ": [[4, 4]]}),
        ("white", " K ", 5, 5, {}, {" K ": [[4, 4]]}),
    ])
    def test_king_move(self, turn, piece, x, y, example_black_coords, example_white_coords):
        example_black = Board_objects(example_black_coords)
        example_white = Board_objects(example_white_coords)
        self.assertTrue(self.moves.validate(turn, piece, 0, x, y, example_black, example_white))

    @parameterized.expand([
        ("black", " K ", 0, 0, {" K ": [[4, 4]]}, {}),
        ("black", " K ", 8, 8, {" K ": [[4, 4]]}, {}),
        ("black", " K ", 2, 2, {" K ": [[4, 4]]}, {}),
        ("black", " K ", 4, 2, {" K ": [[4, 4]]}, {}),
        ("black", " K ", 4, 6, {" K ": [[4, 4]]}, {}),
        ("black", " K ", 6, 4, {" K ": [[4, 4]]}, {}),
        ("black", " K ", 2, 4, {" K ": [[4, 4]]}, {}),
        ("black", " K ", 6, 6, {" K ": [[4, 4]]}, {}),
        ("white", " K ", 0, 0, {}, {" K ": [[4, 4]]}),
        ("white", " K ", 8, 8, {}, {" K ": [[4, 4]]}),
        ("white", " K ", 2, 2, {}, {" K ": [[4, 4]]}),
        ("white", " K ", 4, 2, {}, {" K ": [[4, 4]]}),
        ("white", " K ", 4, 6, {}, {" K ": [[4, 4]]}),
        ("white", " K ", 6, 4, {}, {" K ": [[4, 4]]}),
        ("white", " K ", 2, 4, {}, {" K ": [[4, 4]]}),
        ("white", " K ", 6, 6, {}, {" K ": [[4, 4]]}),
    ])
    def test_king_move2(self, turn, piece, x, y, example_black_coords, example_white_coords):
        example_black = Board_objects(example_black_coords)
        example_white = Board_objects(example_white_coords)
        self.assertFalse(self.moves.validate(turn, piece, 0, x, y, example_black, example_white))

# ROOK

    @parameterized.expand([
        ("black", " R ", 4, 1, {" R ": [[4, 4]]}, {}),
        ("black", " R ", 4, 2, {" R ": [[4, 4]]}, {}),
        ("black", " R ", 4, 3, {" R ": [[4, 4]]}, {}),
        ("black", " R ", 4, 0, {" R ": [[4, 4]]}, {}),
        ("black", " R ", 4, 5, {" R ": [[4, 4]]}, {}),
        ("black", " R ", 4, 6, {" R ": [[4, 4]]}, {}),
        ("black", " R ", 4, 7, {" R ": [[4, 4]]}, {}),
        ("black", " R ", 4, 8, {" R ": [[4, 4]]}, {}),
        ("black", " R ", 0, 4, {" R ": [[4, 4]]}, {}),
        ("black", " R ", 1, 4, {" R ": [[4, 4]]}, {}),
        ("black", " R ", 2, 4, {" R ": [[4, 4]]}, {}),
        ("black", " R ", 3, 4, {" R ": [[4, 4]]}, {}),
        ("black", " R ", 5, 4, {" R ": [[4, 4]]}, {}),
        ("black", " R ", 6, 4, {" R ": [[4, 4]]}, {}),
        ("black", " R ", 7, 4, {" R ": [[4, 4]]}, {}),
        ("black", " R ", 8, 4, {" R ": [[4, 4]]}, {}),
        ("white", " R ", 4, 0, {}, {" R ": [[4, 4]]}),
        ("white", " R ", 4, 1, {}, {" R ": [[4, 4]]}),
        ("white", " R ", 4, 2, {}, {" R ": [[4, 4]]}),
        ("white", " R ", 4, 3, {}, {" R ": [[4, 4]]}),
        ("white", " R ", 4, 5, {}, {" R ": [[4, 4]]}),
        ("white", " R ", 4, 6, {}, {" R ": [[4, 4]]}),
        ("white", " R ", 4, 7, {}, {" R ": [[4, 4]]}),
        ("white", " R ", 4, 8, {}, {" R ": [[4, 4]]}),
        ("white", " R ", 0, 4, {}, {" R ": [[4, 4]]}),
        ("white", " R ", 1, 4, {}, {" R ": [[4, 4]]}),
        ("white", " R ", 2, 4, {}, {" R ": [[4, 4]]}),
        ("white", " R ", 3, 4, {}, {" R ": [[4, 4]]}),
        ("white", " R ", 5, 4, {}, {" R ": [[4, 4]]}),
        ("white", " R ", 6, 4, {}, {" R ": [[4, 4]]}),
        ("white", " R ", 7, 4, {}, {" R ": [[4, 4]]}),
        ("white", " R ", 8, 4, {}, {" R ": [[4, 4]]}),
        ("black", " R ", 0, 4, {" R ": [[4, 4]]}, {"P1": [[0, 4]]}),
        ("white", " R ", 0, 4, {"P1": [[0, 4]]}, {" R ": [[4, 4]]}),
    ])
    def test_rook_move(self, turn, piece, x, y, example_black_coords, example_white_coords):
        example_black = Board_objects(example_black_coords)
        example_white = Board_objects(example_white_coords)
        self.assertTrue(self.moves.validate(turn, piece, 0, x, y, example_black, example_white))

    @parameterized.expand([
        ("black", " R ", 0, 0, {" R ": [[4, 4]]}, {}),
        ("black", " R ", 8, 8, {" R ": [[4, 4]]}, {}),
        ("black", " R ", 1, 1, {" R ": [[4, 4]]}, {}),
        ("black", " R ", 2, 2, {" R ": [[4, 4]]}, {}),
        ("black", " R ", 3, 3, {" R ": [[4, 4]]}, {}),
        ("black", " R ", 6, 6, {" R ": [[4, 4]]}, {}),
        ("black", " R ", 5, 6, {" R ": [[4, 4]]}, {}),
        ("black", " R ", 8, 0, {" R ": [[4, 4]]}, {}),
        ("black", " R ", 0, 2, {" R ": [[4, 4]]}, {}),
        ("black", " R ", 1, 3, {" R ": [[4, 4]]}, {}),
        ("black", " R ", 2, 3, {" R ": [[4, 4]]}, {}),
        ("black", " R ", 3, 5, {" R ": [[4, 4]]}, {}),
        ("black", " R ", 6, 7, {" R ": [[4, 4]]}, {}),
        ("black", " R ", 2, 7, {" R ": [[4, 4]]}, {}),
        ("black", " R ", 8, 7, {" R ": [[4, 4]]}, {}),
        ("black", " R ", 0, 3, {" R ": [[4, 4]]}, {}),
        ("white", " R ", 0, 0, {}, {" R ": [[4, 4]]}),
        ("white", " R ", 8, 8, {}, {" R ": [[4, 4]]}),
        ("white", " R ", 1, 1, {}, {" R ": [[4, 4]]}),
        ("white", " R ", 2, 2, {}, {" R ": [[4, 4]]}),
        ("white", " R ", 3, 3, {}, {" R ": [[4, 4]]}),
        ("white", " R ", 6, 6, {}, {" R ": [[4, 4]]}),
        ("white", " R ", 5, 6, {}, {" R ": [[4, 4]]}),
        ("white", " R ", 8, 0, {}, {" R ": [[4, 4]]}),
        ("white", " R ", 0, 2, {}, {" R ": [[4, 4]]}),
        ("white", " R ", 1, 3, {}, {" R ": [[4, 4]]}),
        ("white", " R ", 2, 3, {}, {" R ": [[4, 4]]}),
        ("white", " R ", 3, 5, {}, {" R ": [[4, 4]]}),
        ("white", " R ", 6, 7, {}, {" R ": [[4, 4]]}),
        ("white", " R ", 8, 7, {}, {" R ": [[4, 4]]}),
        ("white", " R ", 0, 3, {}, {" R ": [[4, 4]]}),
        ("white", " R ", 2, 7, {}, {" R ": [[4, 4]]}),
        ("black", " R ", 4, 1, {" R ": [[4, 4]]}, {"P1 ": [[4, 2]]}),
        ("black", " R ", 4, 8, {" R ": [[4, 4]]}, {"P1 ": [[4, 6]]}),
        ("black", " R ", 0, 4, {" R ": [[4, 4]]}, {"P1 ": [[2, 4]]}),
        ("black", " R ", 7, 4, {" R ": [[4, 4]]}, {"P1 ": [[6, 4]]}),
        ("white", " R ", 4, 1, {"P1 ": [[4, 2]]}, {" R ": [[4, 4]]}),
        ("white", " R ", 4, 8, {"P1 ": [[4, 6]]}, {" R ": [[4, 4]]}),
        ("white", " R ", 0, 4, {"P1 ": [[2, 4]]}, {" R ": [[4, 4]]}),
        ("white", " R ", 7, 4, {"P1 ": [[6, 4]]}, {" R ": [[4, 4]]}),
        ("black", " R ", 4, 1, {" R ": [[4, 4]], "P1 ": [[4, 2]]}, {}),
        ("black", " R ", 4, 8, {" R ": [[4, 4]], "P1 ": [[4, 6]]}, {}),
        ("black", " R ", 0, 4, {" R ": [[4, 4]], "P1 ": [[2, 4]]}, {}),
        ("black", " R ", 7, 4, {" R ": [[4, 4]], "P1 ": [[6, 4]]}, {}),
        ("black", " R ", 0, 4, {" R ": [[4, 4]], "P1 ": [[0, 4]]}, {}),
        ("white", " R ", 0, 4, {}, {" R ": [[4, 4]], "P1 ": [[0, 4]]}),
    ])
    def test_rook_move2(self, turn, piece, x, y, example_black_coords, example_white_coords):
        example_black = Board_objects(example_black_coords)
        example_white = Board_objects(example_white_coords)
        self.assertFalse(self.moves.validate(turn, piece, 0, x, y, example_black, example_white))

# BISHOP

    @parameterized.expand([
        ("black", " B ", 0, 0, {" B ": [[4, 4]]}, {}),
        ("black", " B ", 1, 1, {" B ": [[4, 4]]}, {}),
        ("black", " B ", 2, 2, {" B ": [[4, 4]]}, {}),
        ("black", " B ", 3, 3, {" B ": [[4, 4]]}, {}),
        ("black", " B ", 5, 5, {" B ": [[4, 4]]}, {}),
        ("black", " B ", 6, 6, {" B ": [[4, 4]]}, {}),
        ("black", " B ", 7, 7, {" B ": [[4, 4]]}, {}),
        ("black", " B ", 8, 8, {" B ": [[4, 4]]}, {}),
        ("black", " B ", 0, 8, {" B ": [[4, 4]]}, {}),
        ("black", " B ", 1, 7, {" B ": [[4, 4]]}, {}),
        ("black", " B ", 2, 6, {" B ": [[4, 4]]}, {}),
        ("black", " B ", 3, 5, {" B ": [[4, 4]]}, {}),
        ("black", " B ", 5, 3, {" B ": [[4, 4]]}, {}),
        ("black", " B ", 6, 2, {" B ": [[4, 4]]}, {}),
        ("black", " B ", 7, 1, {" B ": [[4, 4]]}, {}),
        ("black", " B ", 8, 0, {" B ": [[4, 4]]}, {}),
        ("white", " B ", 0, 0, {}, {" B ": [[4, 4]]}),
        ("white", " B ", 1, 1, {}, {" B ": [[4, 4]]}),
        ("white", " B ", 2, 2, {}, {" B ": [[4, 4]]}),
        ("white", " B ", 3, 3, {}, {" B ": [[4, 4]]}),
        ("white", " B ", 5, 5, {}, {" B ": [[4, 4]]}),
        ("white", " B ", 6, 6, {}, {" B ": [[4, 4]]}),
        ("white", " B ", 7, 7, {}, {" B ": [[4, 4]]}),
        ("white", " B ", 8, 8, {}, {" B ": [[4, 4]]}),
        ("white", " B ", 0, 8, {}, {" B ": [[4, 4]]}),
        ("white", " B ", 1, 7, {}, {" B ": [[4, 4]]}),
        ("white", " B ", 2, 6, {}, {" B ": [[4, 4]]}),
        ("white", " B ", 3, 5, {}, {" B ": [[4, 4]]}),
        ("white", " B ", 5, 3, {}, {" B ": [[4, 4]]}),
        ("white", " B ", 6, 2, {}, {" B ": [[4, 4]]}),
        ("white", " B ", 8, 0, {}, {" B ": [[4, 4]]}),
        ("white", " B ", 7, 1, {}, {" B ": [[4, 4]]}),
        ("black", " B ", 1, 0, {" B ": [[2, 1]]}, {}),
        ("black", " B ", 5, 4, {" B ": [[2, 1]]}, {}),
        ("black", " B ", 0, 3, {" B ": [[2, 1]]}, {}),
        ("black", " B ", 3, 0, {" B ": [[2, 1]]}, {}),
        ("black", " B ", 4, 0, {" B ": [[1, 3]]}, {}),
        ("black", " B ", 0, 4, {" B ": [[1, 3]]}, {}),
        ("black", " B ", 3, 5, {" B ": [[1, 3]]}, {}),
        ("black", " B ", 0, 2, {" B ": [[1, 3]]}, {}),
        ("black", " B ", 4, 1, {" B ": [[6, 3]]}, {}),
        ("black", " B ", 8, 1, {" B ": [[6, 3]]}, {}),
        ("black", " B ", 8, 5, {" B ": [[6, 3]]}, {}),
        ("black", " B ", 3, 6, {" B ": [[6, 3]]}, {}),
        ("black", " B ", 8, 3, {" B ": [[6, 5]]}, {}),
        ("black", " B ", 8, 7, {" B ": [[6, 5]]}, {}),
        ("black", " B ", 3, 2, {" B ": [[6, 5]]}, {}),
        ("black", " B ", 4, 7, {" B ": [[6, 5]]}, {}),
        ("black", " B ", 8, 5, {" B ": [[6, 7]]}, {}),
        ("black", " B ", 7, 8, {" B ": [[6, 7]]}, {}),
        ("black", " B ", 3, 4, {" B ": [[6, 7]]}, {}),
        ("black", " B ", 5, 8, {" B ": [[6, 7]]}, {}),
        ("black", " B ", 5, 4, {" B ": [[3, 6]]}, {}),
        ("black", " B ", 5, 8, {" B ": [[3, 6]]}, {}),
        ("black", " B ", 1, 4, {" B ": [[3, 6]]}, {}),
        ("black", " B ", 1, 8, {" B ": [[3, 6]]}, {}),
    ])
    def test_bishop_move(self, turn, piece, x, y, example_black_coords, example_white_coords, piece_index=0):
        example_black = Board_objects(example_black_coords)
        example_white = Board_objects(example_white_coords)
        self.assertTrue(self.moves.validate(turn, piece, piece_index, x, y, example_black, example_white))

    @parameterized.expand([
        ("black", " B ", 0, 4, {" B ": [[4, 4]]}, {}),
        ("black", " B ", 4, 5, {" B ": [[4, 4]]}, {}),
        ("black", " B ", 4, 3, {" B ": [[4, 4]]}, {}),
        ("black", " B ", 3, 4, {" B ": [[4, 4]]}, {}),
        ("black", " B ", 5, 4, {" B ": [[4, 4]]}, {}),
        ("black", " B ", 8, 2, {" B ": [[4, 4]]}, {}),
        ("white", " B ", 0, 4, {}, {" B ": [[4, 4]]}),
        ("white", " B ", 4, 5, {}, {" B ": [[4, 4]]}),
        ("white", " B ", 4, 3, {}, {" B ": [[4, 4]]}),
        ("white", " B ", 3, 4, {}, {" B ": [[4, 4]]}),
        ("white", " B ", 5, 4, {}, {" B ": [[4, 4]]}),
        ("white", " B ", 8, 2, {}, {" B ": [[4, 4]]}),
    ])
    def test_bishop_move2(self, turn, piece, x, y, example_black_coords, example_white_coords, piece_index=0):
        example_black = Board_objects(example_black_coords)
        example_white = Board_objects(example_white_coords)
        self.assertFalse(self.moves.validate(turn, piece, piece_index, x, y, example_black, example_white))


if __name__ == "__main__":
    unittest.main()