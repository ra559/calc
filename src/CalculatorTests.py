import unittest
from Calculator import Calculator


class MytestCase(unittest.TestCase):
    def test_instance_calculator(self):
        calculator = Calculator()
        self.assertIsInstance(calculator, Calculator)

    def test_results_property_calculator(self):
        calculator = Calculator()
        self.assertEqual(calculator.result, 4)

    def test_add_method_calculator(self):
        calculator = Calculator()
        self.assertEqual(calculator.add(2, 2), 4)

    def test_subs_method_calculator(self):
        calculator = Calculator()
        self.assertEqual(calculator.subs(2, 2), 0)

    def test_mult_method_calculator(self):
        calculator = Calculator()
        self.assertEqual(calculator.mult(2, 2), 4)


if __name__ == '__main__':
    unittest.main()
