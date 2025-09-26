import unittest
import perfect_square

class TestPerfectSquare(unittest.TestCase):
    def test_that_is_not_a_list(self):
        perfect_square.get_Perfect_Square(24)
        self.assertRaises(ValueError)

    def test_that_is_a_list(self):
        result = perfect_square.get_Perfect_Square([])
        self.assertEqual(result, [])
        