import math
import unittest
from calculator import add, sub, mul, div, log, exp

class TestCalculator(unittest.TestCase):
    # Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self): # 3 assertions
        self.assertEqual(sub(5, 3), 2)
        self.assertEqual(sub(0, 5), -5)
        self.assertEqual(sub(-2, -3), 1)
    ##########################

    # Partner 1
    def test_multiply(self): # 3 assertions
        pass

    def test_divide(self): # 3 assertions
        pass
    ##########################

    # Partner 2
    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)

    def test_logarithm(self): # 3 assertions
        self.assertEqual(log(2, 8), 3)
        self.assertEqual(log(10, 100), 2)
        self.assertEqual(log(3, 27), 3)

    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            log(1, 5)  # log base 1 is invalid
    ##########################
    
    # Partner 1
    def test_log_invalid_argument(self):  # 1 assertion
        with self.assertRaises(ValueError):
            log(10, -5)  # log of a negative number is invalid

    def test_hypotenuse(self):  # 3 assertions
        self.assertAlmostEqual(math.hypot(3, 4), 5.0)
        self.assertAlmostEqual(math.hypot(5, 12), 13.0)
        self.assertAlmostEqual(math.hypot(0, 7), 7.0)

    def test_sqrt(self):  # 3 assertions
        self.assertAlmostEqual(math.sqrt(4), 2.0)
        self.assertAlmostEqual(math.sqrt(9), 3.0)
        with self.assertRaises(ValueError):
            math.sqrt(-1)
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()