import unittest
from api import Api
from parameterized import parameterized


class test_Api(unittest.TestCase):
    def setUp(self):
        self.api = Api()

    def test_get_board_original(self):
        new_board = (" L KN SG GG  K GG SG KN  L    \n"
                     "    R                 B    \n"
                     " P  P  P  P  P  P  P  P  P \n"
                     "                           \n"
                     "                           \n"
                     "                           \n"
                     " P  P  P  P  P  P  P  P  P \n"
                     "    B                 R    \n"
                     " L KN SG GG  K GG SG KN  L    \n")
        self.assertEqual(self.api.get_board(), new_board)

    @parameterized.expand([
        ([0, 6], [0, 5], (" L KN SG GG  K GG SG KN  L    \n"
                          "    R                 B    \n"
                          " P  P  P  P  P  P  P  P  P \n"
                          "                           \n"
                          "                           \n"
                          " P                         \n"
                          "    P  P  P  P  P  P  P  P \n"
                          "    B                 R    \n"
                          " L KN SG GG  K GG SG KN  L    \n")),
        ([5, 5], [5, 5], (" L KN SG GG  K GG SG KN  L    \n"
                          "    R                 B    \n"
                          " P  P  P  P  P  P  P  P  P \n"
                          "                           \n"
                          "                           \n"
                          "                           \n"
                          " P  P  P  P  P  P  P  P  P \n"
                          "    B                 R    \n"
                          " L KN SG GG  K GG SG KN  L    \n"))
    ])
    def test_play(self, coords, new_coords, new_board):
        self.api.play(coords)
        self.assertEqual(self.api.play(new_coords)[0], new_board)

    @parameterized.expand([
        ([5, 5], [0, 6], [0, 5], [0, 0], (" L KN SG GG  K GG SG KN  L    \n"
                                          "    R                 B    \n"
                                          " P  P  P  P  P  P  P  P  P \n"
                                          "                           \n"
                                          "                           \n"
                                          " P                         \n"
                                          "    P  P  P  P  P  P  P  P \n"
                                          "    B                 R    \n"
                                          " L KN SG GG  K GG SG KN  L    \n")),
        ([0, 6], [0, 4], [0, 5], [0, 0], (" L KN SG GG  K GG SG KN  L    \n"
                                          "    R                 B    \n"
                                          " P  P  P  P  P  P  P  P  P \n"
                                          "                           \n"
                                          "                           \n"
                                          "                           \n"
                                          " P  P  P  P  P  P  P  P  P \n"
                                          "    B                 R    \n"
                                          " L KN SG GG  K GG SG KN  L    \n")),
        ([0, 6], [0, 5], [0, 2], [0, 3], (" L KN SG GG  K GG SG KN  L    \n"
                                          "    R                 B    \n"
                                          "    P  P  P  P  P  P  P  P \n"
                                          " P                         \n"
                                          "                           \n"
                                          " P                         \n"
                                          "    P  P  P  P  P  P  P  P \n"
                                          "    B                 R    \n"
                                          " L KN SG GG  K GG SG KN  L    \n"))
    ])
    def test_play_multiple(self, coords1, coords2, coords3,
                           coords4, new_board):
        self.api.play(coords1)
        self.api.play(coords2)
        self.api.play(coords3)
        self.assertEqual(self.api.play(coords4)[0], new_board)


if __name__ == "__main__":
    unittest.main()
