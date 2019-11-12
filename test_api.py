import unittest
from api import Api


class test_Api(unittest.TestCase):
    def setUp(self):
        self.api = Api()
    def test_get_board_original(self):
        new_board = ("L2 KN2SG2GG2 K GG1SG1KN1L1 \n"
                    "    R                 B    \n"
                    "P9 P8 P7 P6 P5 P4 P3 P2 P1 \n"
                    "                           \n"
                    "                           \n"
                    "                           \n"
                    "P1 P2 P3 P4 P5 P6 P7 P8 P9 \n"
                    "    B                 R    \n"
                    "L1 KN1SG1GG1 K GG2SG2KN2L2 \n")
        self.assertEqual(self.api.get_board(), new_board)


if __name__ == "__main__":
    unittest.main()