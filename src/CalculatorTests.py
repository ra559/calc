import unittest
from Calculator import Calculator


class MytestCase(unittest.TestCase):
    def test_instance_calculator(self):
        calculator = Calculator()
        self.assertIsInstance(calculator, Calculator)

    def test_add_method_calculator(self):
        calculator = Calculator()
        self.assertEqual(calculator.add(2, 2), 4)
        self.assertEqual(calculator.result, 4)

    def test_subs_method_calculator(self):
        calculator = Calculator()
        self.assertEqual(calculator.subs(2, 2), 0)
        self.assertEqual(calculator.result, 0)

    def test_mult_method_calculator(self):
        calculator = Calculator()
        self.assertEqual(calculator.mult(2, 2), 4)
        self.assertEqual(calculator.result, 4)

    def test_div_method_calculator(self):
        calculator = Calculator()
        self.assertEqual(calculator.div(4, 2), 2)
        self.assertEqual(calculator.result, 2)


if __name__ == '__main__':
    unittest.main()
