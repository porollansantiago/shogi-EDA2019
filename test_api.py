import unittest
from api import Api
from parameterized import parameterized

class test_Api(unittest.TestCase):
    def setUp(self):
        self.api = Api()
    def test_get_board_original(self):
        new_board = ("L2 KN2SG2GG2 K GG1SG1KN1L1    \n"
                    "    R                 B    \n"
                    "P9 P8 P7 P6 P5 P4 P3 P2 P1 \n"
                    "                           \n"
                    "                           \n"
                    "                           \n"
                    "P1 P2 P3 P4 P5 P6 P7 P8 P9 \n"
                    "    B                 R    \n"
                    "L1 KN1SG1GG1 K GG2SG2KN2L2    \n")
        self.assertEqual(self.api.get_board(), new_board)

    @parameterized.expand([
        ([0, 6], [0, 5], ("L2 KN2SG2GG2 K GG1SG1KN1L1    \n"
                          "    R                 B    \n"
                          "P9 P8 P7 P6 P5 P4 P3 P2 P1 \n"
                          "                           \n"
                          "                           \n"
                          "P1                         \n"
                          "   P2 P3 P4 P5 P6 P7 P8 P9 \n"
                          "    B                 R    \n"
                          "L1 KN1SG1GG1 K GG2SG2KN2L2    \n")),
        ([5, 5], [5, 5], ("L2 KN2SG2GG2 K GG1SG1KN1L1    \n"
                          "    R                 B    \n"
                          "P9 P8 P7 P6 P5 P4 P3 P2 P1 \n"
                          "                           \n"
                          "                           \n"
                          "                           \n"
                          "P1 P2 P3 P4 P5 P6 P7 P8 P9 \n"
                          "    B                 R    \n"
                          "L1 KN1SG1GG1 K GG2SG2KN2L2    \n"))
    ])
    def test_play(self, coords, new_coords, new_board):
        self.api.play(coords)
        self.assertEqual(self.api.play(new_coords), new_board)

    @parameterized.expand([
        ([5, 5], [0, 6], [0, 5], [0, 0], ("L2 KN2SG2GG2 K GG1SG1KN1L1    \n"
                                          "    R                 B    \n"
                                          "P9 P8 P7 P6 P5 P4 P3 P2 P1 \n"
                                          "                           \n"
                                          "                           \n"
                                          "P1                         \n"
                                          "   P2 P3 P4 P5 P6 P7 P8 P9 \n"
                                          "    B                 R    \n"
                                          "L1 KN1SG1GG1 K GG2SG2KN2L2    \n")),
        ([0, 6], [0, 4], [0, 5], [0, 0], ("L2 KN2SG2GG2 K GG1SG1KN1L1    \n"
                                          "    R                 B    \n"
                                          "P9 P8 P7 P6 P5 P4 P3 P2 P1 \n"
                                          "                           \n"
                                          "                           \n"
                                          "                           \n"
                                          "P1 P2 P3 P4 P5 P6 P7 P8 P9 \n"
                                          "    B                 R    \n"
                                          "L1 KN1SG1GG1 K GG2SG2KN2L2    \n")),
        ([0, 6], [0, 5], [0, 2], [0, 3], ("L2 KN2SG2GG2 K GG1SG1KN1L1    \n"
                                          "    R                 B    \n"
                                          "   P8 P7 P6 P5 P4 P3 P2 P1 \n"
                                          "P9                         \n"
                                          "                           \n"
                                          "P1                         \n"
                                          "   P2 P3 P4 P5 P6 P7 P8 P9 \n"
                                          "    B                 R    \n"
                                          "L1 KN1SG1GG1 K GG2SG2KN2L2    \n"))
    ])
    def test_play_multiple(self, coords1, coords2, coords3, coords4, new_board):
        self.api.play(coords1)
        self.api.play(coords2)
        self.api.play(coords3)
        self.assertEqual(self.api.play(coords4), new_board)

if __name__ == "__main__":
    unittest.main()