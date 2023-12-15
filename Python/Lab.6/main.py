import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    # Тест додавання
    def test_addition_positive(self):
        self.assertEqual(self.calculator.perform_calculation(10, 5, '+'), 15)

    def test_addition_negative(self):
        self.assertEqual(self.calculator.perform_calculation(-10, -5, '+'), -15)

    # Тест віднімання
    def test_subtraction_positive(self):
        self.assertEqual(self.calculator.perform_calculation(10, 5, '-'), 5)

    def test_subtraction_negative(self):
        self.assertEqual(self.calculator.perform_calculation(5, 10, '-'), -5)

    # Тести множення
    def test_multiplication_positive(self):
        self.assertEqual(self.calculator.perform_calculation(10, 5, '*'), 50)

    def test_multiplication_negative(self):
        self.assertEqual(self.calculator.perform_calculation(10, -5, '*'), -50)

    def test_multiplication_zero(self):
        self.assertEqual(self.calculator.perform_calculation(10, 0, '*'), 0)

    # Тести ділення
    def test_division(self):
        self.assertEqual(self.calculator.perform_calculation(10, 5, '/'), 2)

    def test_division_zero(self):
        with self.assertRaises(ZeroDivisionError):
            self.calculator.perform_calculation(10, 0, '/') 


    def test_invalid_operator(self):
        with self.assertRaises(ValueError):
            self.calculator.perform_calculation(10, 5, 'invalid_operator')

if __name__ == '__main__':
    unittest.main()
