import unittest
from simple_calculator import SimpleCalculator


class testcalculator(unittest.TestCase):

    def setUp(self):
        self.calc = SimpleCalculator()

    def test_calculator(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.subtract(5, 2), 3)
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.divide(4, 2), 2)
        self.assertEqual(self.calc.divide(4, 0), None)


unittest.main()
