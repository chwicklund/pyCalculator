import unittest
from src.calculator.calculator import Calculator


class CalcTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_result_is_zero_calculator(self):
        self.assertEqual(self.calculator.result, 0)

    def test_addition(self):
        add = Calculator.add(1, 2)
        self.assertIsInstance(add, Calculator)

    def test_subtraction(self):
        sub = Calculator.subtract(1, 2)
        self.assertIsInstance(sub, Calculator)

    def test_multiplication(self):
        mult = Calculator.multiply(1, 2)
        self.assertIsInstance(mult, Calculator)

    def test_division(self):
        div = Calculator.divide(1, 2)
        self.assertIsInstance(div, Calculator)


if __name__ == '__main__':
    unittest.main()



