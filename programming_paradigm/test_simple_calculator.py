import unittest
from simple_calculator import SimpleCalculator

class calculator_test(unittest.TestCase):
    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()
    def test_addition(self):
        """Test the addition method."""
        result = self.calc.add(2,5)
        self.assertEqual(result,7)
        self.assertEqual(self.calc.add(-2,2),0)
    def test_subtraction(self):
        """Test the subtraction method"""
        self.assertEqual(self.calc.subtract(5,3),2)
        self.assertEqual(self.calc.subtract(-5,-3),-2)
    def test_multiply(self):
        """Test the Multiplication method"""
        self.assertEqual(self.calc.multiply(2,10),20)
        self.assertEqual(self.calc.multiply(0,10),0)
    def test_divide(self):
        """Test the Division method"""
        self.assertEqual(self.calc.divide(4,2),2)
        self.assertEqual(self.calc.divide(2,0), None)