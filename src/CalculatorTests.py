import unittest
from Calculator import Calculator


class MytestCase(unittest.TestCase):
    def test_instance_calculator(self):
        calculator = Calculator()
        self.assertIsInstance(calculator, Calculator)

    def test_results_propterty_calculator(self):
        calculator = Calculator()
        self.assertEqual(calculator.result, 4)


if __name__ == '__main__':
    unittest.main()
