# https://github.com/Davin28/lab10-RR-DL
# Partner 1: David Leigue
# Partner 2: Renan Regalado
import math
import unittest
from calculator import add, subtract, mul, div, logarithm, hypotenuse, square_root

class TestCalculator(unittest.TestCase):
    # Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self): # 3 assertions
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(0, 5), -5)
        self.assertEqual(subtract(-2, -3), 1)
    ##########################

    # Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(3, 4), 12)
        self.assertEqual(mul(-2, 5), -10)
        self.assertEqual(mul(0, 100), 0)

    def test_divide(self): # 3 assertions
        self.assertEqual(div(2, 10), 5)
        self.assertEqual(div(1, 5), 5)
        self.assertAlmostEqual(div(0.5, 2), 4)
    ##########################

    # Partner 2
    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)

    def test_logarithm(self): # 3 assertions
        self.assertEqual(logarithm(2, 8), 3)
        self.assertEqual(logarithm(10, 100), 2)
        self.assertEqual(logarithm(3, 27), 3)

    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(1, 5)  # log base 1 is invalid
    ##########################
    
    # Partner 1
    def test_log_invalid_argument(self):  # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(10, -5)  # log of a negative number is invalid

    def test_hypotenuse(self):  # 3 assertions
        self.assertAlmostEqual(hypotenuse(3, 4), 5.0)
        self.assertAlmostEqual(hypotenuse(5, 12), 13.0)
        self.assertAlmostEqual(hypotenuse(0, 7), 7.0)

    def test_sqrt(self):  # 3 assertions
        self.assertAlmostEqual(square_root(4), 2.0)
        self.assertAlmostEqual(square_root(9), 3.0)
        with self.assertRaises(ValueError):
            math.sqrt(-1)
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()