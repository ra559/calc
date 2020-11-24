import unittest
import Calculator
import csv

# CONSTANTS
'''
NOTE:
Always include the directory name for docker. By default docker will
look for the files in the home directory. 
'''
FILEADD = 'src/UnitTestAddition.csv'
FILESUB = 'src/UnitTestSubtraction.csv'
FILEMUL = 'src/UnitTestMultiplication.csv'
FILESQR = 'src/UnitTestSquareRoot.csv'
FILEDIV = 'src/UnitTestDivision.csv'
FILESQA = 'src/UnitTestSquare.csv'


class TestCalculator(unittest.TestCase):
    def test_add(self):
        c = open(FILEADD, 'r')  # opens file in read mode
        o = csv.reader(c)
        for r in o:
            if r[0] == 'Value 1':
                continue
            else:
                result = Calculator.add(int(r[0]), int(r[1]))
                self.assertEqual(result, int(r[2]))
        c.close()  # closes file

    def test_subtract(self):
        c = open(FILESUB, 'r')
        o = csv.reader(c)
        for r in o:
            if r[0] == 'Value 1':
                continue
            else:
                result = Calculator.subtract(int(r[1]), int(r[0]))
                self.assertEqual(result, int(r[2]))
        c.close()

    def test_multiply(self):
        c = open(FILEMUL, 'r')
        o = csv.reader(c)
        for r in o:
            if r[0] == 'Value 1':
                continue
            else:
                result = Calculator.multiply(int(r[0]), int(r[1]))
                self.assertEqual(result, int(r[2]))
        c.close()

    def test_divide(self):
        c = open(FILEDIV, 'r')
        o = csv.reader(c)
        for r in o:
            if r[0] == 'Value 1':
                continue
            else:
                result = Calculator.divide(int(r[1]), int(r[0]))
                self.assertEqual(result, float(r[2]))
        c.close()

    def test_square(self):
        c = open(FILESQA, 'r')
        o = csv.reader(c)
        for r in o:
            if r[0] == 'Value 1':
                continue
            else:
                result = Calculator.square(int(r[0]))
                self.assertEqual(result, float(r[1]))
        c.close()


    def test_squareRoot(self):
        c = open(FILESQR, 'r')
        o = csv.reader(c)
        for r in o:
            if r[0] == 'Value 1':
                continue
            else:
                result = Calculator.squareRoot(int(r[0]))
                self.assertEqual(result, float(r[1]))
        c.close()


if __name__ == '__main__':
    unittest.main()
