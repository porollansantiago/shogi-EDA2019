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
        ("white", " P ", 4, 5, {}, {" P ": [[4, 4]], " P": [[4, 5]]}),
        ("white", " R ", 4, 5, {}, {" R ": [[4, 4]], " P": [[4, 5]]}),
        ("white", " L ", 4, 5, {}, {" L ": [[4, 4]], " P": [[4, 5]]}),
        ("white", "KN ", 3, 6, {}, {"KN ": [[4, 4]], " P": [[3, 6]]}),
        ("white", "SG ", 4, 5, {}, {"SG ": [[4, 4]], " P": [[4, 5]]}),
        ("white", "GG ", 4, 5, {}, {"GG ": [[4, 4]], " P": [[4, 5]]}),
        ("white", " B ", 3, 3, {}, {" B ": [[4, 4]], " P": [[3, 3]]}),
        ("white", " K ", 4, 5, {}, {" K ": [[4, 4]], " P": [[4, 5]]}),
        ("black", " P ", 4, 3, {" P ": [[4, 4]], " P": [[4, 3]]}, {}),
        ("black", " R ", 4, 3, {" R ": [[4, 4]], " P": [[4, 3]]}, {}),
        ("black", " L ", 4, 3, {" L ": [[4, 4]], " P": [[4, 3]]}, {}),
        ("black", "KN ", 5, 2, {"KN ": [[4, 4]], " P": [[5, 2]]}, {}),
        ("black", "SG ", 4, 3, {"SG ": [[4, 4]], " P": [[4, 3]]}, {}),
        ("black", "GG ", 4, 3, {"GG ": [[4, 4]], " P": [[4, 3]]}, {}),
        ("black", " B ", 3, 3, {" B ": [[4, 4]], " P": [[3, 3]]}, {}),
        ("black", " K ", 4, 3, {" K ": [[4, 4]], " P": [[4, 3]]}, {}),
    ])
    def test_validate_overlapping(self, turn, piece, x, y, example_black_coords, example_white_coords):
        example_black = Board_objects(example_black_coords)
        example_white = Board_objects(example_white_coords)
        self.assertFalse(self.moves.validate(turn, piece, 0, x, y, example_black, example_white))

    @parameterized.expand([
        ("white", " P ", 4, 5, {}, {" P ": [[4, 4]]}),
        ("white", " R ", 4, 5, {}, {" R ": [[4, 4]]}),
        ("white", " L ", 4, 5, {}, {" L ": [[4, 4]]}),
        ("white", "KN ", 3, 6, {}, {"KN ": [[4, 4]]}),
        ("white", "SG ", 4, 5, {}, {"SG ": [[4, 4]]}),
        ("white", "GG ", 4, 5, {}, {"GG ": [[4, 4]]}),
        ("white", " B ", 3, 3, {}, {" B ": [[4, 4]]}),
        ("white", " K ", 4, 5, {}, {" K ": [[4, 4]]}),
        ("black", " P ", 4, 3, {" P ": [[4, 4]]}, {}),
        ("black", " R ", 4, 3, {" R ": [[4, 4]]}, {}),
        ("black", " L ", 4, 3, {" L ": [[4, 4]]}, {}),
        ("black", "KN ", 5, 2, {"KN ": [[4, 4]]}, {}),
        ("black", "SG ", 4, 3, {"SG ": [[4, 4]]}, {}),
        ("black", "GG ", 4, 3, {"GG ": [[4, 4]]}, {}),
        ("black", " B ", 3, 3, {" B ": [[4, 4]]}, {}),
        ("black", " K ", 4, 3, {" K ": [[4, 4]]}, {}),
    ])
    def test_validate_overlapping1(self, turn, piece, x, y, example_black_coords, example_white_coords):
        example_black = Board_objects(example_black_coords)
        example_white = Board_objects(example_white_coords)
        self.assertTrue(self.moves.validate(turn, piece, 0, x, y, example_black, example_white))

    @parameterized.expand([
        ("white", " P ", 4, 5, {" P ": [[4, 5]]}, {" P ": [[4, 4]]}),
        ("white", " R ", 4, 5, {" P ": [[4, 5]]}, {" R ": [[4, 4]]}),
        ("white", " L ", 4, 5, {" P ": [[4, 5]]}, {" L ": [[4, 4]]}),
        ("white", "KN ", 3, 6, {" P ": [[3, 6]]}, {"KN ": [[4, 4]]}),
        ("white", "SG ", 4, 5, {" P ": [[4, 5]]}, {"SG ": [[4, 4]]}),
        ("white", "GG ", 4, 5, {" P ": [[4, 5]]}, {"GG ": [[4, 4]]}),
        ("white", " B ", 3, 3, {" P ": [[3, 3]]}, {" B ": [[4, 4]]}),
        ("white", " K ", 4, 5, {" P ": [[4, 5]]}, {" K ": [[4, 4]]}),
        ("black", " P ", 4, 3, {" P ": [[4, 4]]}, {" P ": [[4, 3]]}),
        ("black", " R ", 4, 3, {" R ": [[4, 4]]}, {" P ": [[4, 3]]}),
        ("black", " L ", 4, 3, {" L ": [[4, 4]]}, {" P ": [[4, 3]]}),
        ("black", "KN ", 5, 2, {"KN ": [[4, 4]]}, {" P ": [[5, 2]]}),
        ("black", "SG ", 4, 3, {"SG ": [[4, 4]]}, {" P ": [[4, 3]]}),
        ("black", "GG ", 4, 3, {"GG ": [[4, 4]]}, {" P ": [[4, 3]]}),
        ("black", " B ", 3, 3, {" B ": [[4, 4]]}, {" P ": [[3, 3]]}),
        ("black", " K ", 4, 3, {" K ": [[4, 4]]}, {" P ": [[4, 3]]}),
    ])
    def test_vaildate_overlapping2(self, turn, piece, x, y, example_black_coords, example_white_coords):
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
        ("black", " L ", 0, 7, {" L ": [[0, 8]]}, {}),
        ("black", " L ", 0, 6, {" L ": [[0, 8]]}, {}),
        ("black", " L ", 0, 5, {" L ": [[0, 8]]}, {}),
        ("black", " L ", 0, 4, {" L ": [[0, 8]]}, {}),
        ("black", " L ", 0, 3, {" L ": [[0, 8]]}, {}),
        ("black", " L ", 0, 2, {" L ": [[0, 8]]}, {}),
        ("black", " L ", 0, 1, {" L ": [[0, 8]]}, {}),
        ("black", " L ", 0, 0, {" L ": [[0, 8]]}, {}),
        ("white", " L ", 8, 8, {}, {" L ": [[8, 0]]}),
        ("white", " L ", 8, 1, {}, {" L ": [[8, 0]]}),
        ("white", " L ", 8, 2, {}, {" L ": [[8, 0]]}),
        ("white", " L ", 8, 3, {}, {" L ": [[8, 0]]}),
        ("white", " L ", 8, 4, {}, {" L ": [[8, 0]]}),
        ("white", " L ", 8, 5, {}, {" L ": [[8, 0]]}),
        ("white", " L ", 8, 6, {}, {" L ": [[8, 0]]}),
        ("white", " L ", 8, 7, {}, {" L ": [[8, 0]]}),

    ])
    def test_validate_Lance_move(self, turn, piece, x, y, example_black_coords, example_white_coords):
        example_black = Board_objects(example_black_coords)
        example_white = Board_objects(example_white_coords)
        self.assertTrue(self.moves.validate(turn, piece, 0, x, y, example_black, example_white))

    @parameterized.expand([
        ("black", " L ", 4, 8, {" L ": [[4, 5]]}, {}),
        ("black", " L ", 5, 7, {" L ": [[5, 5]]}, {}),
        ("black", " L ", 6, 6, {" L ": [[6, 5]]}, {}),
        ("black", " L ", 6, 6, {" L ": [[5, 5]]}, {}),
        ("black", " L ", 4, 4, {" L ": [[5, 5]]}, {}),
        ("black", " L ", 0, 0, {" L ": [[5, 5]]}, {}),
        ("black", " L ", 1, 1, {" L ": [[5, 5]]}, {}),
        ("black", " L ", 5, 6, {" L ": [[5, 5]]}, {}),
        ("black", " L ", 5, 7, {" L ": [[5, 5]]}, {}),
        ("black", " L ", 5, 8, {" L ": [[5, 5]]}, {}),
        ("white", " L ", 4, 3, {}, {" L ": [[5, 5]]}),
        ("white", " L ", 3, 4, {}, {" L ": [[5, 5]]}),
        ("white", " L ", 2, 5, {}, {" L ": [[5, 5]]}),
        ("white", " L ", 1, 6, {}, {" L ": [[5, 5]]}),
        ("white", " L ", 0, 7, {}, {" L ": [[5, 5]]}),
        ("white", " L ", 4, 4, {}, {" L ": [[5, 5]]}),
        ("white", " L ", 0, 0, {}, {" L ": [[5, 5]]}),
        ("white", " L ", 1, 5, {}, {" L ": [[5, 5]]}),
        ("black", " L ", 4, 1, {" L ": [[4, 4]]}, {" P ": [[4, 2]]}),
        ("black", " L ", 4, 0, {" L ": [[4, 4]]}, {" P ": [[4, 2]]}),
        ("black", " L ", 0, 0, {" L ": [[0, 8]]}, {" P ": [[0, 4]]}),
        ("black", " L ", 0, 0, {" L ": [[0, 8]], " P ": [[0, 4]]}, {}),
        ("white", " L ", 4, 7, {" P ": [[4, 6]]}, {" L ": [[4, 4]]}),
        ("white", " L ", 4, 8, {" P ": [[4, 6]]}, {" L ": [[4, 4]]}),
    ])
    def test_validate_Lance_move2(self, turn, piece, x, y, example_black_coords, example_white_coords):
        example_black = Board_objects(example_black_coords)
        example_white = Board_objects(example_white_coords)
        self.assertFalse(self.moves.validate(turn, piece, 0, x, y, example_black, example_white))

# KNIGHT

    @parameterized.expand([
        ("black", "KN ", 3, 3, {"KN ": [[4, 5]]}, {}),
        ("black", "KN ", 5, 3, {"KN ": [[4, 5]]}, {}),
        ("white", "KN ", 3, 7, {}, {"KN ": [[4, 5]]}),
        ("white", "KN ", 5, 7, {}, {"KN ": [[4, 5]]}),

    ])
    def test_validate_Knight_move(self, turn, piece, x, y, example_black_coords, example_white_coords):
        example_black = Board_objects(example_black_coords)
        example_white = Board_objects(example_white_coords)
        self.assertTrue(self.moves.validate(turn, piece, 0, x, y, example_black, example_white))

    @parameterized.expand([
        ("black", "KN ", 2, 3, {"KN ": [[4, 5]]}, {}),
        ("black", "KN ", 4, 3, {"KN ": [[4, 5]]}, {}),
        ("black", "KN ", 4, 7, {"KN ": [[4, 5]]}, {}),
        ("black", "KN ", 3, 7, {"KN ": [[4, 5]]}, {}),
        ("black", "KN ", 5, 7, {"KN ": [[4, 5]]}, {}),
        ("black", "KN ", 3, 6, {"KN ": [[4, 5]]}, {}),
        ("black", "KN ", 7, 8, {"KN ": [[4, 5]]}, {}),
        ("white", "KN ", 2, 3, {}, {"KN ": [[4, 5]]}),
        ("white", "KN ", 4, 3, {}, {"KN ": [[4, 5]]}),
        ("white", "KN ", 4, 7, {}, {"KN ": [[4, 5]]}),
        ("white", "KN ", 3, 3, {}, {"KN ": [[4, 5]]}),
        ("white", "KN ", 5, 3, {}, {"KN ": [[4, 5]]}),
        ("white", "KN ", 0, 0, {}, {"KN ": [[4, 5]]})

    ])
    def test_validate_Knight_move2(self, turn, piece, x, y, example_black_coords, example_white_coords):
        example_black = Board_objects(example_black_coords)
        example_white = Board_objects(example_white_coords)
        self.assertFalse(self.moves.validate(turn, piece, 0, x, y, example_black, example_white))

# SILVER GENERAL

    @parameterized.expand([
        ("black", "SG ", 3, 3, {"SG ": [[4, 4]]}, {}),
        ("black", "SG ", 4, 3, {"SG ": [[4, 4]]}, {}),
        ("black", "SG ", 5, 3, {"SG ": [[4, 4]]}, {}),
        ("black", "SG ", 3, 5, {"SG ": [[4, 4]]}, {}),
        ("black", "SG ", 5, 5, {"SG ": [[4, 4]]}, {}),
        ("white", "SG ", 3, 5, {}, {"SG ": [[4, 4]]}),
        ("white", "SG ", 4, 5, {}, {"SG ": [[4, 4]]}),
        ("white", "SG ", 5, 5, {}, {"SG ": [[4, 4]]}),
        ("white", "SG ", 3, 3, {}, {"SG ": [[4, 4]]}),
        ("white", "SG ", 5, 3, {}, {"SG ": [[4, 4]]}),
    ])
    def test_silverGeneral_move(self, turn, piece, x, y, example_black_coords, example_white_coords):
        example_black = Board_objects(example_black_coords)
        example_white = Board_objects(example_white_coords)
        self.assertTrue(self.moves.validate(turn, piece, 0, x, y, example_black, example_white))

    @parameterized.expand([
        ("black", "SG ", 8, 8, {"SG ": [[4, 4]]}, {}),
        ("black", "SG ", 0, 0, {"SG ": [[4, 4]]}, {}),
        ("black", "SG ", 4, 5, {"SG ": [[4, 4]]}, {}),
        ("black", "SG ", 3, 4, {"SG ": [[4, 4]]}, {}),
        ("black", "SG ", 5, 4, {"SG ": [[4, 4]]}, {}),
        ("white", "SG ", 0, 0, {}, {"SG ": [[4, 4]]}),
        ("white", "SG ", 8, 8, {}, {"SG ": [[4, 4]]}),
        ("white", "SG ", 4, 3, {}, {"SG ": [[4, 4]]}),
        ("white", "SG ", 3, 4, {}, {"SG ": [[4, 4]]}),
        ("white", "SG ", 5, 4, {}, {"SG ": [[4, 4]]}),
    ])
    def test_silverGeneral_move2(self, turn, piece, x, y, example_black_coords, example_white_coords):
        example_black = Board_objects(example_black_coords)
        example_white = Board_objects(example_white_coords)
        self.assertFalse(self.moves.validate(turn, piece, 0, x, y, example_black, example_white))

# GOLD GENERAL

    @parameterized.expand([
        ("black", "GG ", 3, 3, {"GG ": [[4, 4]]}, {}),
        ("black", "GG ", 4, 3, {"GG ": [[4, 4]]}, {}),
        ("black", "GG ", 5, 3, {"GG ": [[4, 4]]}, {}),
        ("black", "GG ", 3, 4, {"GG ": [[4, 4]]}, {}),
        ("black", "GG ", 5, 4, {"GG ": [[4, 4]]}, {}),
        ("black", "GG ", 4, 5, {"GG ": [[4, 4]]}, {}),
        ("white", "GG ", 3, 5, {}, {"GG ": [[4, 4]]}),
        ("white", "GG ", 4, 5, {}, {"GG ": [[4, 4]]}),
        ("white", "GG ", 5, 5, {}, {"GG ": [[4, 4]]}),
        ("white", "GG ", 3, 4, {}, {"GG ": [[4, 4]]}),
        ("white", "GG ", 5, 4, {}, {"GG ": [[4, 4]]}),
        ("white", "GG ", 4, 3, {}, {"GG ": [[4, 4]]}),
    ]) 
    def test_goldGeneral_move(self, turn, piece, x, y, example_black_coords, example_white_coords):
        example_black = Board_objects(example_black_coords)
        example_white = Board_objects(example_white_coords)
        self.assertTrue(self.moves.validate(turn, piece, 0, x, y, example_black, example_white))

    @parameterized.expand([
        ("black", "GG ", 0, 0, {"GG ": [[4, 4]]}, {}),
        ("black", "GG ", 8, 8, {"GG ": [[4, 4]]}, {}),
        ("black", "GG ", 3, 5, {"GG ": [[4, 4]]}, {}),
        ("black", "GG ", 5, 5, {"GG ": [[4, 4]]}, {}),
        ("black", "GG ", 4, 2, {"GG ": [[4, 4]]}, {}),
        ("black", "GG ", 4, 6, {"GG ": [[4, 4]]}, {}),
        ("white", "GG ", 3, 3, {}, {"GG ": [[4, 4]]}),
        ("white", "GG ", 5, 3, {}, {"GG ": [[4, 4]]}),
        ("white", "GG ", 0, 0, {}, {"GG ": [[4, 4]]}),
        ("white", "GG ", 8, 8, {}, {"GG ": [[4, 4]]}),
        ("white", "GG ", 4, 2, {}, {"GG ": [[4, 4]]}),
        ("white", "GG ", 4, 6, {}, {"GG ": [[4, 4]]}),
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
        ("black", " R ", 0, 4, {" R ": [[4, 4]]}, {" P ": [[0, 4]]}),
        ("white", " R ", 0, 4, {" P ": [[0, 4]]}, {" R ": [[4, 4]]}),
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
        ("white", " R ", 4, 1, {" P ": [[4, 2]]}, {" R ": [[4, 4]]}),
        ("white", " R ", 4, 8, {" P ": [[4, 6]]}, {" R ": [[4, 4]]}),
        ("white", " R ", 0, 4, {" P ": [[2, 4]]}, {" R ": [[4, 4]]}),
        ("white", " R ", 7, 4, {" P ": [[6, 4]]}, {" R ": [[4, 4]]}),
        ("black", " R ", 4, 1, {" R ": [[4, 4]], " P ": [[4, 2]]}, {}),
        ("black", " R ", 4, 8, {" R ": [[4, 4]], " P ": [[4, 6]]}, {}),
        ("black", " R ", 0, 4, {" R ": [[4, 4]], " P ": [[2, 4]]}, {}),
        ("black", " R ", 7, 4, {" R ": [[4, 4]], " P ": [[6, 4]]}, {}),
        ("black", " R ", 0, 4, {" R ": [[4, 4]], " P ": [[0, 4]]}, {}),
        ("white", " R ", 0, 4, {}, {" R ": [[4, 4]], " P ": [[0, 4]]}),
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

    # PROMOTED PAWN

    @parameterized.expand([
        ("black", "PP ", 3, 3, {"PP ": [[4, 4]]}, {}),
        ("black", "PP ", 4, 3, {"PP ": [[4, 4]]}, {}),
        ("black", "PP ", 5, 3, {"PP ": [[4, 4]]}, {}),
        ("black", "PP ", 3, 4, {"PP ": [[4, 4]]}, {}),
        ("black", "PP ", 5, 4, {"PP ": [[4, 4]]}, {}),
        ("black", "PP ", 4, 5, {"PP ": [[4, 4]]}, {}),
        ("white", "PP ", 3, 5, {}, {"PP ": [[4, 4]]}),
        ("white", "PP ", 4, 5, {}, {"PP ": [[4, 4]]}),
        ("white", "PP ", 5, 5, {}, {"PP ": [[4, 4]]}),
        ("white", "PP ", 3, 4, {}, {"PP ": [[4, 4]]}),
        ("white", "PP ", 5, 4, {}, {"PP ": [[4, 4]]}),
        ("white", "PP ", 4, 3, {}, {"PP ": [[4, 4]]}),
    ]) 
    def test_promoted_pawn(self, turn, piece, x, y, example_black_coords, example_white_coords):
        example_black = Board_objects(example_black_coords)
        example_white = Board_objects(example_white_coords)
        self.assertTrue(self.moves.validate(turn, piece, 0, x, y, example_black, example_white))

    @parameterized.expand([
        ("black", "PP ", 0, 0, {"PP ": [[4, 4]]}, {}),
        ("black", "PP ", 8, 8, {"PP ": [[4, 4]]}, {}),
        ("black", "PP ", 3, 5, {"PP ": [[4, 4]]}, {}),
        ("black", "PP ", 5, 5, {"PP ": [[4, 4]]}, {}),
        ("black", "PP ", 4, 2, {"PP ": [[4, 4]]}, {}),
        ("black", "PP ", 4, 6, {"PP ": [[4, 4]]}, {}),
        ("white", "PP ", 3, 3, {}, {"PP ": [[4, 4]]}),
        ("white", "PP ", 5, 3, {}, {"PP ": [[4, 4]]}),
        ("white", "PP ", 0, 0, {}, {"PP ": [[4, 4]]}),
        ("white", "PP ", 8, 8, {}, {"PP ": [[4, 4]]}),
        ("white", "PP ", 4, 2, {}, {"PP ": [[4, 4]]}),
        ("white", "PP ", 4, 6, {}, {"PP ": [[4, 4]]}),
    ])
    def test_promoted_pawn2(self, turn, piece, x, y, example_black_coords, example_white_coords):
        example_black = Board_objects(example_black_coords)
        example_white = Board_objects(example_white_coords)
        self.assertFalse(self.moves.validate(turn, piece, 0, x, y, example_black, example_white))

    # PROMOTED SILVER

    @parameterized.expand([
        ("black", "PSG", 3, 3, {"PSG": [[4, 4]]}, {}),
        ("black", "PSG", 4, 3, {"PSG": [[4, 4]]}, {}),
        ("black", "PSG", 5, 3, {"PSG": [[4, 4]]}, {}),
        ("black", "PSG", 3, 4, {"PSG": [[4, 4]]}, {}),
        ("black", "PSG", 5, 4, {"PSG": [[4, 4]]}, {}),
        ("black", "PSG", 4, 5, {"PSG": [[4, 4]]}, {}),
        ("white", "PSG", 3, 5, {}, {"PSG": [[4, 4]]}),
        ("white", "PSG", 4, 5, {}, {"PSG": [[4, 4]]}),
        ("white", "PSG", 5, 5, {}, {"PSG": [[4, 4]]}),
        ("white", "PSG", 3, 4, {}, {"PSG": [[4, 4]]}),
        ("white", "PSG", 5, 4, {}, {"PSG": [[4, 4]]}),
        ("white", "PSG", 4, 3, {}, {"PSG": [[4, 4]]}),
    ]) 
    def test_promoted_silver(self, turn, piece, x, y, example_black_coords, example_white_coords):
        example_black = Board_objects(example_black_coords)
        example_white = Board_objects(example_white_coords)
        self.assertTrue(self.moves.validate(turn, piece, 0, x, y, example_black, example_white))

    @parameterized.expand([
        ("black", "PSG", 0, 0, {"PSG": [[4, 4]]}, {}),
        ("black", "PSG", 8, 8, {"PSG": [[4, 4]]}, {}),
        ("black", "PSG", 3, 5, {"PSG": [[4, 4]]}, {}),
        ("black", "PSG", 5, 5, {"PSG": [[4, 4]]}, {}),
        ("black", "PSG", 4, 2, {"PSG": [[4, 4]]}, {}),
        ("black", "PSG", 4, 6, {"PSG": [[4, 4]]}, {}),
        ("white", "PSG", 3, 3, {}, {"PSG": [[4, 4]]}),
        ("white", "PSG", 5, 3, {}, {"PSG": [[4, 4]]}),
        ("white", "PSG", 0, 0, {}, {"PSG": [[4, 4]]}),
        ("white", "PSG", 8, 8, {}, {"PSG": [[4, 4]]}),
        ("white", "PSG", 4, 2, {}, {"PSG": [[4, 4]]}),
        ("white", "PSG", 4, 6, {}, {"PSG": [[4, 4]]}),
    ])
    def test_promoted_silver2(self, turn, piece, x, y, example_black_coords, example_white_coords):
        example_black = Board_objects(example_black_coords)
        example_white = Board_objects(example_white_coords)
        self.assertFalse(self.moves.validate(turn, piece, 0, x, y, example_black, example_white))

    # PROMOTED KNIGHT

    @parameterized.expand([
        ("black", "PKN", 3, 3, {"PKN": [[4, 4]]}, {}),
        ("black", "PKN", 4, 3, {"PKN": [[4, 4]]}, {}),
        ("black", "PKN", 5, 3, {"PKN": [[4, 4]]}, {}),
        ("black", "PKN", 3, 4, {"PKN": [[4, 4]]}, {}),
        ("black", "PKN", 5, 4, {"PKN": [[4, 4]]}, {}),
        ("black", "PKN", 4, 5, {"PKN": [[4, 4]]}, {}),
        ("white", "PKN", 3, 5, {}, {"PKN": [[4, 4]]}),
        ("white", "PKN", 4, 5, {}, {"PKN": [[4, 4]]}),
        ("white", "PKN", 5, 5, {}, {"PKN": [[4, 4]]}),
        ("white", "PKN", 3, 4, {}, {"PKN": [[4, 4]]}),
        ("white", "PKN", 5, 4, {}, {"PKN": [[4, 4]]}),
        ("white", "PKN", 4, 3, {}, {"PKN": [[4, 4]]}),
    ]) 
    def test_promoted_knight(self, turn, piece, x, y, example_black_coords, example_white_coords):
        example_black = Board_objects(example_black_coords)
        example_white = Board_objects(example_white_coords)
        self.assertTrue(self.moves.validate(turn, piece, 0, x, y, example_black, example_white))

    @parameterized.expand([
        ("black", "PKN", 0, 0, {"PKN": [[4, 4]]}, {}),
        ("black", "PKN", 8, 8, {"PKN": [[4, 4]]}, {}),
        ("black", "PKN", 3, 5, {"PKN": [[4, 4]]}, {}),
        ("black", "PKN", 5, 5, {"PKN": [[4, 4]]}, {}),
        ("black", "PKN", 4, 2, {"PKN": [[4, 4]]}, {}),
        ("black", "PKN", 4, 6, {"PKN": [[4, 4]]}, {}),
        ("white", "PKN", 3, 3, {}, {"PKN": [[4, 4]]}),
        ("white", "PKN", 5, 3, {}, {"PKN": [[4, 4]]}),
        ("white", "PKN", 0, 0, {}, {"PKN": [[4, 4]]}),
        ("white", "PKN", 8, 8, {}, {"PKN": [[4, 4]]}),
        ("white", "PKN", 4, 2, {}, {"PKN": [[4, 4]]}),
        ("white", "PKN", 4, 6, {}, {"PKN": [[4, 4]]}),
    ])
    def test_promoted_knight2(self, turn, piece, x, y, example_black_coords, example_white_coords):
        example_black = Board_objects(example_black_coords)
        example_white = Board_objects(example_white_coords)
        self.assertFalse(self.moves.validate(turn, piece, 0, x, y, example_black, example_white))

    # PROMOTED LANCE

    @parameterized.expand([
        ("black", "PL ", 3, 3, {"PL ": [[4, 4]]}, {}),
        ("black", "PL ", 4, 3, {"PL ": [[4, 4]]}, {}),
        ("black", "PL ", 5, 3, {"PL ": [[4, 4]]}, {}),
        ("black", "PL ", 3, 4, {"PL ": [[4, 4]]}, {}),
        ("black", "PL ", 5, 4, {"PL ": [[4, 4]]}, {}),
        ("black", "PL ", 4, 5, {"PL ": [[4, 4]]}, {}),
        ("white", "PL ", 3, 5, {}, {"PL ": [[4, 4]]}),
        ("white", "PL ", 4, 5, {}, {"PL ": [[4, 4]]}),
        ("white", "PL ", 5, 5, {}, {"PL ": [[4, 4]]}),
        ("white", "PL ", 3, 4, {}, {"PL ": [[4, 4]]}),
        ("white", "PL ", 5, 4, {}, {"PL ": [[4, 4]]}),
        ("white", "PL ", 4, 3, {}, {"PL ": [[4, 4]]}),
    ]) 
    def test_promoted_lance(self, turn, piece, x, y, example_black_coords, example_white_coords):
        example_black = Board_objects(example_black_coords)
        example_white = Board_objects(example_white_coords)
        self.assertTrue(self.moves.validate(turn, piece, 0, x, y, example_black, example_white))

    @parameterized.expand([
        ("black", "PL ", 0, 0, {"PL ": [[4, 4]]}, {}),
        ("black", "PL ", 8, 8, {"PL ": [[4, 4]]}, {}),
        ("black", "PL ", 3, 5, {"PL ": [[4, 4]]}, {}),
        ("black", "PL ", 5, 5, {"PL ": [[4, 4]]}, {}),
        ("black", "PL ", 4, 2, {"PL ": [[4, 4]]}, {}),
        ("black", "PL ", 4, 6, {"PL ": [[4, 4]]}, {}),
        ("white", "PL ", 3, 3, {}, {"PL ": [[4, 4]]}),
        ("white", "PL ", 5, 3, {}, {"PL ": [[4, 4]]}),
        ("white", "PL ", 0, 0, {}, {"PL ": [[4, 4]]}),
        ("white", "PL ", 8, 8, {}, {"PL ": [[4, 4]]}),
        ("white", "PL ", 4, 2, {}, {"PL ": [[4, 4]]}),
        ("white", "PL ", 4, 6, {}, {"PL ": [[4, 4]]}),
    ])
    def test_promoted_lance2(self, turn, piece, x, y, example_black_coords, example_white_coords):
        example_black = Board_objects(example_black_coords)
        example_white = Board_objects(example_white_coords)
        self.assertFalse(self.moves.validate(turn, piece, 0, x, y, example_black, example_white))

    # PROMOTED BISHOP

    @parameterized.expand([
        ("black", "PB ", 0, 0, {"PB ": [[4, 4]]}, {}),
        ("black", "PB ", 1, 1, {"PB ": [[4, 4]]}, {}),
        ("black", "PB ", 2, 2, {"PB ": [[4, 4]]}, {}),
        ("black", "PB ", 3, 3, {"PB ": [[4, 4]]}, {}),
        ("black", "PB ", 5, 5, {"PB ": [[4, 4]]}, {}),
        ("black", "PB ", 6, 6, {"PB ": [[4, 4]]}, {}),
        ("black", "PB ", 7, 7, {"PB ": [[4, 4]]}, {}),
        ("black", "PB ", 8, 8, {"PB ": [[4, 4]]}, {}),
        ("black", "PB ", 0, 8, {"PB ": [[4, 4]]}, {}),
        ("black", "PB ", 1, 7, {"PB ": [[4, 4]]}, {}),
        ("black", "PB ", 2, 6, {"PB ": [[4, 4]]}, {}),
        ("black", "PB ", 3, 5, {"PB ": [[4, 4]]}, {}),
        ("black", "PB ", 5, 3, {"PB ": [[4, 4]]}, {}),
        ("black", "PB ", 6, 2, {"PB ": [[4, 4]]}, {}),
        ("black", "PB ", 7, 1, {"PB ": [[4, 4]]}, {}),
        ("black", "PB ", 8, 0, {"PB ": [[4, 4]]}, {}),
        ("white", "PB ", 0, 0, {}, {"PB ": [[4, 4]]}),
        ("white", "PB ", 1, 1, {}, {"PB ": [[4, 4]]}),
        ("white", "PB ", 2, 2, {}, {"PB ": [[4, 4]]}),
        ("white", "PB ", 3, 3, {}, {"PB ": [[4, 4]]}),
        ("white", "PB ", 5, 5, {}, {"PB ": [[4, 4]]}),
        ("white", "PB ", 6, 6, {}, {"PB ": [[4, 4]]}),
        ("white", "PB ", 7, 7, {}, {"PB ": [[4, 4]]}),
        ("white", "PB ", 8, 8, {}, {"PB ": [[4, 4]]}),
        ("white", "PB ", 0, 8, {}, {"PB ": [[4, 4]]}),
        ("white", "PB ", 1, 7, {}, {"PB ": [[4, 4]]}),
        ("white", "PB ", 2, 6, {}, {"PB ": [[4, 4]]}),
        ("white", "PB ", 3, 5, {}, {"PB ": [[4, 4]]}),
        ("white", "PB ", 5, 3, {}, {"PB ": [[4, 4]]}),
        ("white", "PB ", 6, 2, {}, {"PB ": [[4, 4]]}),
        ("white", "PB ", 8, 0, {}, {"PB ": [[4, 4]]}),
        ("white", "PB ", 7, 1, {}, {"PB ": [[4, 4]]}),
        ("black", "PB ", 1, 0, {"PB ": [[2, 1]]}, {}),
        ("black", "PB ", 5, 4, {"PB ": [[2, 1]]}, {}),
        ("black", "PB ", 0, 3, {"PB ": [[2, 1]]}, {}),
        ("black", "PB ", 3, 0, {"PB ": [[2, 1]]}, {}),
        ("black", "PB ", 4, 0, {"PB ": [[1, 3]]}, {}),
        ("black", "PB ", 0, 4, {"PB ": [[1, 3]]}, {}),
        ("black", "PB ", 3, 5, {"PB ": [[1, 3]]}, {}),
        ("black", "PB ", 0, 2, {"PB ": [[1, 3]]}, {}),
        ("black", "PB ", 4, 1, {"PB ": [[6, 3]]}, {}),
        ("black", "PB ", 8, 1, {"PB ": [[6, 3]]}, {}),
        ("black", "PB ", 8, 5, {"PB ": [[6, 3]]}, {}),
        ("black", "PB ", 3, 6, {"PB ": [[6, 3]]}, {}),
        ("black", "PB ", 8, 3, {"PB ": [[6, 5]]}, {}),
        ("black", "PB ", 8, 7, {"PB ": [[6, 5]]}, {}),
        ("black", "PB ", 3, 2, {"PB ": [[6, 5]]}, {}),
        ("black", "PB ", 4, 7, {"PB ": [[6, 5]]}, {}),
        ("black", "PB ", 8, 5, {"PB ": [[6, 7]]}, {}),
        ("black", "PB ", 7, 8, {"PB ": [[6, 7]]}, {}),
        ("black", "PB ", 3, 4, {"PB ": [[6, 7]]}, {}),
        ("black", "PB ", 5, 8, {"PB ": [[6, 7]]}, {}),
        ("black", "PB ", 5, 4, {"PB ": [[3, 6]]}, {}),
        ("black", "PB ", 5, 8, {"PB ": [[3, 6]]}, {}),
        ("black", "PB ", 1, 4, {"PB ": [[3, 6]]}, {}),
        ("black", "PB ", 1, 8, {"PB ": [[3, 6]]}, {}),

        ("white", "PB ", 4, 3, {}, {"PB ": [[4, 4]]}),
        ("white", "PB ", 5, 4, {}, {"PB ": [[4, 4]]}),
        ("white", "PB ", 4, 5, {}, {"PB ": [[4, 4]]}),
        ("white", "PB ", 3, 4, {}, {"PB ": [[4, 4]]}),
        ("black", "PB ", 3, 5, {"PB ": [[3, 6]]}, {}),
        ("black", "PB ", 4, 6, {"PB ": [[3, 6]]}, {}),
        ("black", "PB ", 3, 7, {"PB ": [[3, 6]]}, {}),
        ("black", "PB ", 2, 6, {"PB ": [[3, 6]]}, {}),
    ])
    def test_promoted_bishop_move(self, turn, piece, x, y, example_black_coords, example_white_coords, piece_index=0):
        example_black = Board_objects(example_black_coords)
        example_white = Board_objects(example_white_coords)
        self.assertTrue(self.moves.validate(turn, piece, piece_index, x, y, example_black, example_white))

    @parameterized.expand([
        ("black", "PB ", 0, 4, {"PB ": [[4, 4]]}, {}),
        ("black", "PB ", 8, 4, {"PB ": [[4, 4]]}, {}),
        ("black", "PB ", 4, 0, {"PB ": [[4, 4]]}, {}),
        ("black", "PB ", 4, 8, {"PB ": [[4, 4]]}, {}),
        ("black", "PB ", 6, 0, {"PB ": [[4, 4]]}, {}),
        ("black", "PB ", 8, 2, {"PB ": [[4, 4]]}, {}),
        ("white", "PB ", 0, 4, {}, {"PB ": [[4, 4]]}),
        ("white", "PB ", 8, 4, {}, {"PB ": [[4, 4]]}),
        ("white", "PB ", 4, 0, {}, {"PB ": [[4, 4]]}),
        ("white", "PB ", 4, 8, {}, {"PB ": [[4, 4]]}),
        ("white", "PB ", 6, 0, {}, {"PB ": [[4, 4]]}),
        ("white", "PB ", 8, 2, {}, {"PB ": [[4, 4]]}),
    ])
    def test_promoted_bishop(self, turn, piece, x, y, example_black_coords, example_white_coords, piece_index=0):
        example_black = Board_objects(example_black_coords)
        example_white = Board_objects(example_white_coords)
        self.assertFalse(self.moves.validate(turn, piece, piece_index, x, y, example_black, example_white))

    # PROMOTED ROOK

    @parameterized.expand([
        ("black", "PR ", 4, 1, {"PR ": [[4, 4]]}, {}),
        ("black", "PR ", 4, 2, {"PR ": [[4, 4]]}, {}),
        ("black", "PR ", 4, 3, {"PR ": [[4, 4]]}, {}),
        ("black", "PR ", 4, 0, {"PR ": [[4, 4]]}, {}),
        ("black", "PR ", 4, 5, {"PR ": [[4, 4]]}, {}),
        ("black", "PR ", 4, 6, {"PR ": [[4, 4]]}, {}),
        ("black", "PR ", 4, 7, {"PR ": [[4, 4]]}, {}),
        ("black", "PR ", 4, 8, {"PR ": [[4, 4]]}, {}),
        ("black", "PR ", 0, 4, {"PR ": [[4, 4]]}, {}),
        ("black", "PR ", 1, 4, {"PR ": [[4, 4]]}, {}),
        ("black", "PR ", 2, 4, {"PR ": [[4, 4]]}, {}),
        ("black", "PR ", 3, 4, {"PR ": [[4, 4]]}, {}),
        ("black", "PR ", 5, 4, {"PR ": [[4, 4]]}, {}),
        ("black", "PR ", 6, 4, {"PR ": [[4, 4]]}, {}),
        ("black", "PR ", 7, 4, {"PR ": [[4, 4]]}, {}),
        ("black", "PR ", 8, 4, {"PR ": [[4, 4]]}, {}),
        ("white", "PR ", 4, 0, {}, {"PR ": [[4, 4]]}),
        ("white", "PR ", 4, 1, {}, {"PR ": [[4, 4]]}),
        ("white", "PR ", 4, 2, {}, {"PR ": [[4, 4]]}),
        ("white", "PR ", 4, 3, {}, {"PR ": [[4, 4]]}),
        ("white", "PR ", 4, 5, {}, {"PR ": [[4, 4]]}),
        ("white", "PR ", 4, 6, {}, {"PR ": [[4, 4]]}),
        ("white", "PR ", 4, 7, {}, {"PR ": [[4, 4]]}),
        ("white", "PR ", 4, 8, {}, {"PR ": [[4, 4]]}),
        ("white", "PR ", 0, 4, {}, {"PR ": [[4, 4]]}),
        ("white", "PR ", 1, 4, {}, {"PR ": [[4, 4]]}),
        ("white", "PR ", 2, 4, {}, {"PR ": [[4, 4]]}),
        ("white", "PR ", 3, 4, {}, {"PR ": [[4, 4]]}),
        ("white", "PR ", 5, 4, {}, {"PR ": [[4, 4]]}),
        ("white", "PR ", 6, 4, {}, {"PR ": [[4, 4]]}),
        ("white", "PR ", 7, 4, {}, {"PR ": [[4, 4]]}),
        ("white", "PR ", 8, 4, {}, {"PR ": [[4, 4]]}),
        ("black", "PR ", 0, 4, {"PR ": [[4, 4]]}, {" P ": [[0, 4]]}),
        ("white", "PR ", 0, 4, {" P ": [[0, 4]]}, {"PR ": [[4, 4]]}),
        ("black", "PR ", 5, 5, {"PR ": [[4, 4]]}, {}),
        ("black", "PR ", 5, 3, {"PR ": [[4, 4]]}, {}),
        ("black", "PR ", 3, 3, {"PR ": [[4, 4]]}, {}),
        ("black", "PR ", 3, 5, {"PR ": [[4, 4]]}, {}),
        ("white", "PR ", 5, 5, {}, {"PR ": [[4, 4]]}),
        ("white", "PR ", 5, 3, {}, {"PR ": [[4, 4]]}),
        ("white", "PR ", 3, 3, {}, {"PR ": [[4, 4]]}),
        ("white", "PR ", 3, 5, {}, {"PR ": [[4, 4]]}),
    ])
    def test_promoted_rook_move(self, turn, piece, x, y, example_black_coords, example_white_coords):
        example_black = Board_objects(example_black_coords)
        example_white = Board_objects(example_white_coords)
        self.assertTrue(self.moves.validate(turn, piece, 0, x, y, example_black, example_white))

    @parameterized.expand([
        ("black", " R ", 0, 0, {" R ": [[4, 4]]}, {}),
        ("black", " R ", 8, 8, {" R ": [[4, 4]]}, {}),
        ("black", " R ", 1, 1, {" R ": [[4, 4]]}, {}),
        ("black", " R ", 2, 2, {" R ": [[4, 4]]}, {}),
        ("black", " R ", 0, 8, {" R ": [[4, 4]]}, {}),
        ("black", " R ", 6, 6, {" R ": [[4, 4]]}, {}),
        ("black", " R ", 5, 6, {" R ": [[4, 4]]}, {}),
        ("black", " R ", 8, 0, {" R ": [[4, 4]]}, {}),
        ("black", " R ", 0, 2, {" R ": [[4, 4]]}, {}),
        ("black", " R ", 1, 3, {" R ": [[4, 4]]}, {}),
        ("black", " R ", 2, 3, {" R ": [[4, 4]]}, {}),
        ("black", " R ", 8, 8, {" R ": [[4, 4]]}, {}),
        ("black", " R ", 6, 7, {" R ": [[4, 4]]}, {}),
        ("black", " R ", 2, 7, {" R ": [[4, 4]]}, {}),
        ("black", " R ", 8, 7, {" R ": [[4, 4]]}, {}),
        ("black", " R ", 0, 3, {" R ": [[4, 4]]}, {}),
        ("white", " R ", 0, 0, {}, {" R ": [[4, 4]]}),
        ("white", " R ", 8, 8, {}, {" R ": [[4, 4]]}),
        ("white", " R ", 1, 1, {}, {" R ": [[4, 4]]}),
        ("white", " R ", 2, 2, {}, {" R ": [[4, 4]]}),
        ("white", " R ", 0, 8, {}, {" R ": [[4, 4]]}),
        ("white", " R ", 6, 6, {}, {" R ": [[4, 4]]}),
        ("white", " R ", 5, 6, {}, {" R ": [[4, 4]]}),
        ("white", " R ", 8, 0, {}, {" R ": [[4, 4]]}),
        ("white", " R ", 0, 2, {}, {" R ": [[4, 4]]}),
        ("white", " R ", 1, 3, {}, {" R ": [[4, 4]]}),
        ("white", " R ", 2, 3, {}, {" R ": [[4, 4]]}),
        ("white", " R ", 8, 8, {}, {" R ": [[4, 4]]}),
        ("white", " R ", 6, 7, {}, {" R ": [[4, 4]]}),
        ("white", " R ", 2, 7, {}, {" R ": [[4, 4]]}),
        ("white", " R ", 8, 7, {}, {" R ": [[4, 4]]}),
        ("white", " R ", 0, 3, {}, {" R ": [[4, 4]]}),
        ("black", " R ", 4, 1, {" R ": [[4, 4]]}, {"P1 ": [[4, 2]]}),
        ("black", " R ", 4, 8, {" R ": [[4, 4]]}, {"P1 ": [[4, 6]]}),
        ("black", " R ", 0, 4, {" R ": [[4, 4]]}, {"P1 ": [[2, 4]]}),
        ("black", " R ", 7, 4, {" R ": [[4, 4]]}, {"P1 ": [[6, 4]]}),
        ("white", " R ", 4, 1, {" P ": [[4, 2]]}, {" R ": [[4, 4]]}),
        ("white", " R ", 4, 8, {" P ": [[4, 6]]}, {" R ": [[4, 4]]}),
        ("white", " R ", 0, 4, {" P ": [[2, 4]]}, {" R ": [[4, 4]]}),
        ("white", " R ", 7, 4, {" P ": [[6, 4]]}, {" R ": [[4, 4]]}),
        ("black", " R ", 4, 1, {" R ": [[4, 4]], " P ": [[4, 2]]}, {}),
        ("black", " R ", 4, 8, {" R ": [[4, 4]], " P ": [[4, 6]]}, {}),
        ("black", " R ", 0, 4, {" R ": [[4, 4]], " P ": [[2, 4]]}, {}),
        ("black", " R ", 7, 4, {" R ": [[4, 4]], " P ": [[6, 4]]}, {}),
        ("black", " R ", 0, 4, {" R ": [[4, 4]], " P ": [[0, 4]]}, {}),
        ("white", " R ", 0, 4, {}, {" R ": [[4, 4]], " P ": [[0, 4]]}),
    ])
    def test_promoted_rook_move2(self, turn, piece, x, y, example_black_coords, example_white_coords):
        example_black = Board_objects(example_black_coords)
        example_white = Board_objects(example_white_coords)
        self.assertFalse(self.moves.validate(turn, piece, 0, x, y, example_black, example_white))


if __name__ == "__main__":
    unittest.main(verbosity=2)