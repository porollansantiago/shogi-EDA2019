import unittest

modules_to_test = (
    "test_board",
    "test_api",
    "test_board_objects",
    "test_moves"
)


def suite():
    tests = unittest.TestSuite()
    for module in map(__import__, modules_to_test):
        tests.addTest(unittest.findTestCases(module))
    return tests


if __name__ == "__main__":
    unittest.TextTestRunner(verbosity=2).run(suite())