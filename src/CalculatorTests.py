import unittest
import Calculator
import csv

FILEADD = 'UnitTestAddition.csv'
FILESUB = 'UnitTestSubtraction.csv'
FILEMUL = 'UnitTestMultiplication.csv'
FILESQR = 'UnitTestSquareRoot.csv'


class TestCalculator(unittest.TestCase):
    def test_add(self):
        result = Calculator.add(2, 2)
        self.assertEqual(result, 4)

    def test_subtract(self):
        result = Calculator.subtract(2, 2)
        self.assertEqual(result, 0)

    def test_multiply(self):
        result = Calculator.multiply(2, 2)
        self.assertEqual(result, 4)

    def test_divide(self):
        result = Calculator.divide(4, 2)
        self.assertEqual(result, 2)

    def test_square(self):
        result = Calculator.square(2, 2)
        self.assertEqual(result, 4)

    def test_squareRoot(self):
        result = Calculator.squareRoot(9)
        self.assertEqual(result, 3)


if __name__ == '__main__':
    unittest.main()
