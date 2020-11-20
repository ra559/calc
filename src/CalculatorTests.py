import unittest
from Calculator import Calculator


class MytestCase(unittest.TestCase):
    def test_instance_calculator(self):
        calculator = Calculator()
        self.assertIsInstance(calculator, Calculator)


if __name__ == '__main__':
    unittest.main()
